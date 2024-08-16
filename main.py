#!/usr/bin/env python3
import os
import re
import sys
import argparse
import pandas

def fix_all_names(directory: str):
  regex = re.compile("\\s*\\(.*\\)$")
  for file in os.listdir(directory):
    stem, ext = os.path.splitext(file)
    if ext in [".m4a"]:
      match = regex.search(stem)
      if match is not None:
        new_name = stem[:match.span()[0]]
        os.rename(os.path.join(directory, file), os.path.join(directory, "%s%s" % (new_name, ext)))

def ffmpeg_edit_metadata(input_path: str, metadata: dict, output_path: str):
  stringified_metadata = " ".join("-metadata %s=\"%s\"" % (k,v) for (k,v) in metadata.items())
  os.system("ffmpeg -i \"%s\" %s -codec copy \"%s\"" % (input_path, stringified_metadata, output_path))

def open_routes(directory: str):
  agency = pandas.read_csv(os.path.join(directory, 'agency.csv'))
  files = ["%s.csv" % agency_code for agency_code in agency.agency_code]
  routes: list = []
  for file in files:
    df = pandas.read_csv(os.path.join(directory, file))
    length = len(df)
    for i in range(length):
      routes.append({
        'agency_id': df.agency_id[i],
        'short_name': df.route_short_name[i],
        'long_name': df.route_long_name[i].replace("/", "\\/")
      })
  return routes

def routing(directory: str):
  routes = open_routes(directory)
  for route in routes:
    print("%s - %s: %s" % (
      route['agency_id'],
      route['short_name'],
      route['long_name']
    ))

def enumerate(directory: str):
  metadatas: list[dict] = []
  for file in os.listdir(directory):
    stem, ext = os.path.splitext(file)
    if ext in [".m4a"]:
      data = [_.strip() for _ in stem.split('-')]
      if len(data) < 2:
        data = (*data, "")
      if len(data) < 3:
        data = (*data, "")
      metadatas.append({'file': file, 'title': data[0], 'author': data[1], 'album': data[2]})
  return metadatas

def correct(input_directory: str):
  files = enumerate(input_directory)
  for file in files:
    metadata = {
      'author': 'franc',
      'album': file['album'],
      'artist': file['author'],
      'title': file['title']
    }
    input_path = os.path.join(input_directory, file['file'])
    output_path = 'tmp.m4a'
    ffmpeg_edit_metadata(input_path, metadata, output_path)
    os.rename(output_path, input_path)

def produce(routes_directory: str, input_directory: str, output_directory: str):
  dump={
    'agency_id': [],
    'short_name': [],
    'long_name': [],
    'title': [],
    'author': [],
    'album': []
  }

  os.makedirs(output_directory, exist_ok=True)
  routes = open_routes(routes_directory)
  files = enumerate(input_directory)

  for file in files:
    route = routes.pop(0)
    dump['agency_id'].append(route['agency_id'])
    dump['short_name'].append(route['short_name'])
    dump['long_name'].append(route['long_name'])
    dump['title'].append(file['title'])
    dump['author'].append(file['author'])
    dump['album'].append(file['album'])
    metadata = {
      'author': 'franc',
      'album': route['agency_id'],
      'artist': file['author'],
      'title': "Linea %s - %s" % (route['short_name'], route['long_name']),
      'comment': "%s - %s - %s" % (file['title'], file['author'], file['album'])
    }
    input_path = os.path.join(input_directory, file['file'])
    output_path = os.path.join(output_directory, "%s - %s - %s.m4a" % (route['agency_id'], route['short_name'], route['long_name']))
    ffmpeg_edit_metadata(input_path, metadata, output_path)
  pandas.DataFrame(dump).to_csv('dump.csv', index=False)

if __name__ == "__main__":
  cli = argparse.ArgumentParser()
  cli.add_argument('-F', '--fix-all-names', action='store_true', default=False, help='fix_all_names($InputDir)')
  cli.add_argument('-E', '--enumerate', action='store_true', default=False, help='enumerate($InputDir)')
  cli.add_argument('-R', '--routing', action='store_true', default=False, help='routing($InputDir/routes)')
  cli.add_argument('-C', '--correct', action='store_true', default=False, help='correct($InputDir)')
  cli.add_argument('-P', '--produce', action='store_true', default=False, help='produce($InputDir/routes, $InputDir, $OutputDir)')
  cli.add_argument('-i', '--input', type=str, default='input', help='input directory')
  cli.add_argument('-r', '--routes', type=str, default='routes', help='routes directory')
  cli.add_argument('-o', '--output', type=str, default='output', help='output directory')
  config = cli.parse_args(sys.argv[1:])

  if config.fix_all_names:
    fix_all_names(config.input)
  if config.enumerate:
    enumerate(config.input)
  if config.routing:
    routing(config.routes)
  if config.correct:
    correct(config.input)
  if config.produce:
    produce(config.routes, config.input, config.output)
