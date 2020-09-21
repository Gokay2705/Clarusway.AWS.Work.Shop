

from flask import Flask, render_template, request, url_for 

app = Flask (__name__)

def Dec_to_Roman(number_decimal):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    number_roman = ''
    i = 0
        
    while  number_decimal > 0 and number_decimal < 4000:
        for _ in range(number_decimal // val[i]):
            number_roman += syb[i]
            number_decimal -= val[i]
        i += 1
    return number_roman



@app.route("/", methods = ["GET", "POST"])
def index():
    developer_name = "E2193 Mustafa"
    if request.method == "POST":
        number_decimal = request.form.get("number_decimal")
        number_roman = Dec_to_Roman(int(number_decimal))
        return render_template("result.html", developer_name = developer_name, number_decimal = number_decimal, number_roman = number_roman)
    else:
        return render_template("index.html", developer_name = developer_name)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
