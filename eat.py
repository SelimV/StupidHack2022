from random import randint
import subprocess
import os



overlays = ["bite1.png", "star.png"]

minwidth = 100
maxwidth = 400



def overlay(page, overlay, width):
  width = str(width)
  output = subprocess.run(["./convert_identify.sh", page], capture_output=True).stdout
  print(output.decode())
  size = output.decode().split()
  print(size)
  x = randint(-100, 200+int(size[0]))
  y = randint(-100, 200+int(size[1]))
  coor = "+" + str(x) + "+" + str(y)
  subprocess.run(["./convert_overlay.sh", page, overlay, width, coor])

def bite(filename):
  i = randint(0, len(overlays)-1)
  bitemark = overlays[i]
  
  width = randint(minwidth, maxwidth)
 
  overlay(filename, "overlays/" + bitemark, width)

def eatPage(filename):
  bites = randint(0, 10)

  for i in range(0, bites):
    bite(filename)

def eatFile(filename):
  subprocess.run(["./convert_pdf2png.sh", filename])

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)
  for file in tmpFiles:
    eatPage(file)

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)


  subprocess.run(["./convert_png2pdf.sh", "eaten/" + filename])


def main():
  files = os.listdir("homework")
  subprocess.run(["mkdir", "homework/eaten"])

  for file in files:
    filename = file.split(".")[0]
    eatFile(filename)


main()