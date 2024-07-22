import os

for file in os.listdir('.'):
  if ".mp3" in file:
    out = file.replace(".mp3", ".m4a")
    os.system("ffmpeg -i \"%s\" -c:a aac -b:a 192k -c:v copy \"%s\"" % (file, out))
