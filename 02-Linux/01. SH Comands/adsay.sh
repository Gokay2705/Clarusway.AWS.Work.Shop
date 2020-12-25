#!/bin/bash
sum=0
for (( Hakan=1; Hakan<25; Hakan++ ))
do
    let sum+=$Hakan
    echo "sayac: $Hakan    toplam:$sum"
done