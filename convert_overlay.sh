#!/bin/bash



# Overlay star.png to input.png
composite  \( -geometry $3 $2 \) -geometry $4  homework/tmp/$1 homework/tmp/$1



