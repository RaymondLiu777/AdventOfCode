#!/bin/bash
year=2025
day=$(printf "%02d" $1)
folder=day$day

# Check if day has already been created (look for folder)
if test -d $folder; then
    echo "Day already created"
    exit 1
fi

# Get input
curl -b session=$(cat .aocrc) -f --user-agent "github.com/RaymondLiu777/AdventOfCode by raymondliu4414@gmail.com" --connect-timeout 3 https://adventofcode.com/$year/day/$1/input -o input.txt
if [ $? -ne 0 ]; then
    echo "Unable to get input, exiting"
    rm input.txt > /dev/null 2>&1
    exit 1
fi

# Get problem text
curl -b session=$(cat .aocrc) -f --user-agent "github.com/RaymondLiu777/AdventOfCode by raymondliu4414@gmail.com" --connect-timeout 3 https://adventofcode.com/$year/day/$1 -o $folder-data.txt
if [ $? -ne 0 ]; then
    echo "Unable to get sample, exiting"
    rm $folder-data.txt > /dev/null 2>&1
    exit 1
fi

# Parse out sample
python3 sample_finder.py $folder-data.txt > sample.txt
rm $folder-data.txt

# Create day with template, sample and input
mkdir $folder
cp template.py $folder/$folder.py
touch $folder/$folder.hs
mv sample.txt $folder/
mv input.txt $folder/