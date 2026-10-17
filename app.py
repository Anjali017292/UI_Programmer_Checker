
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Multiplication Table
@app.route("/table", methods=["POST"])
def table():
    number = int(request.form.get("number"))

    result = [
        f"{number} x {i} = {number * i}"
        for i in range(1, 11)
    ]

    return render_template("index.html", table=result)


# Positive, Negative or Zero
@app.route("/check-number", methods=["POST"])
def check_number():
    number = float(request.form.get("number"))

    if number > 0:
        result = "Number is Positive"
    elif number < 0:
        result = "Number is Negative"
    else:
        result = "Number is Zero"

    return render_template(
        "index.html",
        number_result=result
    )


# Prime Number
@app.route("/check-prime", methods=["POST"])
def check_prime():
    number = int(request.form.get("number"))

    if number < 2:
        result = "Number is not Prime"
    else:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            result = "Number is Prime"
        else:
            result = "Number is not Prime"

    return render_template(
        "index.html",
        prime_result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
