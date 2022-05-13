from operator import sub
import subprocess
import os
from turtle import width

from sqlalchemy import over


inputfile = "input2"


def overlay(page, overlay, width, x, y):
  width = str(width)
  coor = "+" + str(x) + "+" + str(y)
  subprocess.run(["./convert_overlay.sh", page, overlay, width, coor])


def eatPage(filename):
  width = 70
  x = 100
  y = 200
  overlay(filename, "overlays/star.png", width, x, y)


def main():
  subprocess.run(["./convert_pdf2png.sh", inputfile])

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)
  for file in tmpFiles:
    eatPage(file)

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)

  subprocess.run(["./convert_png2pdf.sh"])


main()