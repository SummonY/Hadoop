#!/bin/sh

for year in ../../data/193[0-9]
do
    echo -ne `basename $year/ .tar`"\t"
    

done
