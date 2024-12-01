#!/bin/bash

day=$(printf "%02d" $1)
folder=day$day

if test -d $folder; then
    echo "Day already created"
else
    mkdir $folder
    cp template.py $folder/$folder.py
    touch $folder/sample.txt
    curl -b session=$(cat .aocrc) --user-agent "github.com/RaymondLiu777/AdventOfCode by raymondliu4414@gmail.com" https://adventofcode.com/2024/day/$1/input > $folder/input.txt
fi

