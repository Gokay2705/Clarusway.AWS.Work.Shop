#!/bin/bash
read -p "Enter your name:" name
read -p "Enter your age:" age
read -p "Enter your average life expectancy:" ale
if ((age<18))
then
        echo "$name  is a student."
        echo "At least $((18-age)) years to becaome a worker"
elif ((((age > 17))&&((age<65))))
then
        echo "$name you're a worker."
        echo "$((65-age)) years to retire."
elif ((((age>=65))&&((age<ale))))
then
        echo "$name you're retired."
        echo "$((ale-age)) years to die."
else
        echo "!!!Already died!!!"
        echo "!!!Already died!!!"
        echo "!!!Already died!!!"
fi