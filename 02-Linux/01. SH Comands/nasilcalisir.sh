
#!/bin/bash
echo"1.ornek"
number=5
python3 -c "print($number)"
# ***************
echo "2.ornek"
num1=5
num2=4
python3 -c "print( $num1 + $num2 )"
# ******************
echo "3.ornek"
n1=5
n2=4
code=$(cat << END
print("$n1")
print($n2)
print($n1 + $n2)
END
)
python3 -c “$code“
# ******************
# python3 -c “./mycode.py” mycode.py dosyasini cagirip calistirma.
# **************