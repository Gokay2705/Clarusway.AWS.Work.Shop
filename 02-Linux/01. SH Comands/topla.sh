#!/bin/bash
read -p "first number: " num1
read -p "second number: " num2
let total=num1+num2
echo $(( total++ ))
echo $total
echo $(( total - num1 ))