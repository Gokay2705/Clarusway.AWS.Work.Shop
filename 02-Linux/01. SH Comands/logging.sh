#!/bin/bash

read -p "Enter number 1 :" num1
read -p "Enter number 2 :" num2
read -p "Enter number 3 :" num3


if(((( num2 > num1 )) && (( num2 < num3)))); then echo "$num2 is between $num1 and $num3"
elif ((((num2 == num1)) && ((num2 < num3)))); then echo "$num2 is equal $num1 and < $num3"
elif ((((num2 == num3)) && ((num2 < num1)))); then echo "$num2 is equal $num3 and < $num1"
elif ((((num2 == num1)) && ((num2 > num3)))); then echo "$num2 is equal $num1 and > $num3"
else
        echo "$num2 is equal $num1 and > $num1"