from random import randint
import subprocess
import os


borderOverlays = ["bite1.png"]
centerOverlays = ["star.png"]

minwidth = 50
maxwidth = 100



def overlay(page, overlay, width, x, y):
  width = str(width)
  coor = "+" + str(x) + "+" + str(y)
  subprocess.run(["./convert_overlay.sh", page, overlay, width, coor])

def biteBorder(filename):
  i = randint(0, len(borderOverlays)-1)
  bitemark = borderOverlays[i]
  width = randint(minwidth, maxwidth)
  x = 0
  y = 0
  overlay(filename, "overlays/" + bitemark, width, x, y)

def biteCenter(filename):
  i = randint(0, len(centerOverlays)-1)
  bitemark = centerOverlays[i]
  
  width = randint(minwidth, maxwidth)
  x = 400
  y = 30
  overlay(filename, "overlays/" + bitemark, width, x, y)

def eatPage(filename):
  centerBites = randint(0, 5)
  borderBites = randint(0, 5)

  for i in range(0, centerBites):
    biteCenter(filename)

  for i in range(0, borderBites):
    biteBorder(filename)

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