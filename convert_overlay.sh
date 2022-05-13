#!/bin/bash



# Overlay star.png to input.png
composite  \( -geometry 70 $2 \) -geometry +12+50  homework/tmp/$1 homework/tmp/output_$1



