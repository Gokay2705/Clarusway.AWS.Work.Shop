#!/bin/bash

number=10
let new_number=number++
echo "Number = $number"
echo "New_number = $new_number"

number=10
let new_number=--number
echo "Number = $number"
echo "New_number = $new_number"

number=10
let new_number=++number
echo "Number = $number"
echo "New_number = $new_number"

number=10
let new_number=number--
echo "Number = $number"
echo "New_number = $new_number"