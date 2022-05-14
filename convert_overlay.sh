#!/bin/bash



# Overlay star.png to input.png
composite  \(  -geometry $3 -background 'rgba(0,0,0,0)'  -rotate $5  $2 \) -geometry $4  homework/tmp/$1 homework/tmp/$1



