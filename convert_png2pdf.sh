#!/bin/bash


convert homework/tmp/*.png homework/$1.pdf

rm  homework/tmp/*
rm -r homework/tmp

