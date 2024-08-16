#!/usr/bin/env python3
import pandas
import os

def download_audio(url: str, output: str):
  os.system("yt-dlp -x \"%s\" --audio-format m4a --output \"%s\"" % (url, output))


def download_files(path: str):
  df: pandas.DataFrame = pandas.read_csv(os.path.join(path, 'downlist.csv'))
  for index, row in df.iterrows():
    url = row['url']
    output = "%s - %s - %s" % (row['title'], row['author'], row['album'])
    filepath = "%s.m4a" % output
    if os.path.exists(filepath):
      print("Skipping \"%s\"" % filepath)
    else:
      download_audio(url, output)

download_files('.')
