#!/bin/bash
base_value=5
read -p "Enter a number" user_input
total=$((base_value + user_input))
echo "Total value is: $total"