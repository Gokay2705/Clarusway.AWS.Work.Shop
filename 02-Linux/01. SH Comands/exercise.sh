#!/bin/bash

function print_age(){
        local birth_year
        read -p "Enter your birth year :" birth_year
        age=0
        let age=$1-birth_year
        echo "You are $age years old."
}

print_age 2020
