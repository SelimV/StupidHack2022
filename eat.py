import subprocess
import os
import sys



def overlay(page, overlay, width, x, y):
  width = str(width)
  coor = "+" + str(x) + "+" + str(y)
  subprocess.run(["./convert_overlay.sh", page, overlay, width, coor])


def eatPage(filename):
  width = 70
  x = 100
  y = 200
  overlay(filename, "overlays/star.png", width, x, y)

def eatFile(filename):
  subprocess.run(["./convert_pdf2png.sh", filename])

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)
  for file in tmpFiles:
    eatPage(file)

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)

  subprocess.run(["mkdir", "homework/eaten"])

  subprocess.run(["./convert_png2pdf.sh", "eaten/" + filename])


def main():
  files = os.listdir("homework")
  for file in files:
    filename = file.split(".")[0]
    eatFile(filename)


main()