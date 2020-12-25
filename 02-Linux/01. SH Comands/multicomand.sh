
#/bin/bash

num1=2227
num2=2150
code=$(cat<<ENT
print($num1)
print($num2)
print($num1+$num2)
ENT
)
#python3 -c "print($num1+$num2)"
python3 -c "$code"