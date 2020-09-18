# Import Flask modules

from flask import Flask, render_template, request

# Create an object named app

app = Flask (__name__)

@app.route("/")
def home ():
    if request.method == "POST" "GET":
        number = request.form.get(number)
        return render_template ("index.html", name = "Mustafa")

    else:    
        return render_template("result.html")

    



if __name__ == "__main__":
    app.run (debug=True)
