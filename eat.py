from random import randint, shuffle
import subprocess
import os



overlays = os.listdir("overlays")
print(overlays)

minwidth = 100
maxwidth = 400



def overlay(page, overlay, width):
  width = str(width)
  output = subprocess.run(["./convert_identify.sh", page], capture_output=True).stdout
  size = output.decode().split()
  x = randint(-150, int(size[0]))
  y = randint(-150, int(size[1]))
  coor = "+" + str(x) + "+" + str(y)
  rotation = str(randint(0, 360))
  subprocess.run(["./convert_overlay.sh", page, overlay, width, coor, rotation])

def bite(filename):
  i = randint(0, len(overlays)-1)
  bitemark = overlays[i]

  width = randint(minwidth, maxwidth)

  if("paw" in bitemark):
    width = 150
 
  overlay(filename, "overlays/" + bitemark, width)

def eatPage(filename):
  bites = randint(5, 13)

  for i in range(0, bites):
    bite(filename)

def shufflepages(files):
  numbers = range(len(files))
  shuffle(numbers)

  for i in range(len(files)):
    subprocess.run(["mv", files[i], str(numbers[i])+".png"])  

def eatFile(filename):
  subprocess.run(["./convert_pdf2png.sh", filename])

  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)
  for file in tmpFiles:
    eatPage(file)

  shufflepages(tmpFiles)
  tmpFiles = os.listdir("homework/tmp")
  print(tmpFiles)


  subprocess.run(["./convert_png2pdf.sh", "eaten/" + filename])


def main():
  subprocess.run(["rm", '-r', "homework/eaten"])
  files = os.listdir("homework")
  subprocess.run(["mkdir", "homework/eaten"])

  for file in files:
    filename = file.split(".")[0]
    eatFile(filename)


main()