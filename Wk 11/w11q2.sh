#!/bin/bash

echo 'Enter a limit for factorial: '
read upto

factorial=1

for i in $(seq 1 $upto)
do
    factorial=$((factorial * i))
done

echo $factorial