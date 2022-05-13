from operator import sub
import subprocess
import os


inputfile = "input2"


def eatPage(filename):
  subprocess.run(["./convert_overlay.sh", filename, "overlays/star.png"])


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