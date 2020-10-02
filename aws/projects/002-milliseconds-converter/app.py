from flask import Flask, render_template, request
from datetime import timedelta

app = Flask(__name__)

# Convert 600000ms (10 minutes) back to duration value. 
def convert(milliseconds):
    milliseconds = int(milliseconds)
    seconds=(milliseconds/1000)%60
    seconds = int(seconds)
    minutes=(milliseconds/(1000*60))%60
    minutes = int(minutes)
    hours=(milliseconds/(1000*60*60))%24

    if milliseconds < 1000:
        print("Just %d millisecond/s" % (milliseconds))
    elif milliseconds < 60000:
        print("%d second/s" % (seconds))
    elif milliseconds < 360000:
        print("%d minute/s %d second/s" % (minutes, seconds))
    elif milliseconds < (24*360000):
        print("%d hour/s %d minute/s %d second/s" % (hours, minutes, seconds))
    return
        
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