#!/usr/bin/env bash
rm images.txt
ex1=1
for f in lectures/*.md; do
    #echo $f $ex1
    python3 py/lecture.py post --date 2021-10-$ex1 $f;
    let ex1++;
done
