#!/bin/bash


# convert pdf to png
convert input.pdf input.png


# Convert pdf to png with white background
convert input.pdf -background white -alpha remove -alpha off input.png


# Overlay star.png to input.png
composite  \( -geometry 70 star.png \) -geometry +12+50  input.png output.png


# convert png to pdf
convert output.png output.pdf


# if multiple pages:
convert output-*.png output.pdf

