from flask import Flask, url_for, render_template, request

app = Flask(__name__)

def convert(milliseconds):
    # one hour in milliseconds
    hour_in_milliseconds = 60*60*1000
    # calculate the hours within given milliseconds
    hours = milliseconds // hour_in_milliseconds
    # calculate milliseconds left over when hours subtracted
    milliseconds_left = milliseconds % hour_in_milliseconds
    # one minute in milliseconds
    minutes_in_milliseconds = 60*1000
    # calculate the minutes within remainder milliseconds
    minutes = milliseconds_left // minutes_in_milliseconds
    # calculate milliseconds left over when minutes subtracted
    milliseconds_left %= minutes_in_milliseconds
    # calculate the seconds within remainder milliseconds
    seconds = milliseconds_left // 1000
    # format the output string
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)


@app.route("/", methods = ["POST", "GET"])
def index():
    developer_name = "E2193 Mustafa"
    if request.method == "POST":
        milliseconds = request.form.get("number")
        result = convert(milliseconds)
        return render_template("result.html", milliseconds = milliseconds , result = result, developer_name = developer_name)
    else:
        return render_template("index.html", developer_name = developer_name)

if __name__ == "__main__":
    app.run(debug = True)
    #app.run(host="0.0.0.0", port=80)