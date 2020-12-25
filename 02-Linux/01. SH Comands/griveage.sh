#!/bin/bash

read -p "How old are you?" age

if [ $age -ge 18 ]
then
        echo "You can drive! :-)"
elif [ $age -eq 17 ]
then
        echo "You can drive next year! :-|"
else
        echo "You can't drive. :-("
fi