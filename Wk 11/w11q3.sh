#!/bin/bash

echo 'Enter a number from 1 to 10 (or greater than 10):'
read input

if [ "$input" -gt 10 ]; then
    echo "You have entered wrong!"
else
    echo "You have entered correct!"
fi