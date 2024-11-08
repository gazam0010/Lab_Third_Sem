#!/bin/bash

greet_user(){
    echo "Hello, $name! Welcome"
}

echo "Enter your name:"
read name

greet_user "$name"