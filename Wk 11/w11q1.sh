#!/bin/bash

FILE="w10q4.sh"

if [ -f "$FILE" ]; then
    echo "File $FILE exists."
else
    echo "File $FILE does not exist."
fi
