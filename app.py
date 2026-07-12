from flask import Flask, render_template, request

app = Flask(__name__)

# Store calculation history
history = []

@app.route('/', methods=['GET', 'POST'])
def calculator():

    result = ""
    symbol = ""

    if request.method == 'POST':

        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operations']

            if operation == "add":
                result = num1 + num2
                symbol = "+"

            elif operation == "sub":
                result = num1 - num2
                symbol = "-"

            elif operation == "mul":
                result = num1 * num2
                symbol = "×"

            elif operation == "div":
                if num2 != 0:
                    result = num1 / num2
                    symbol = "÷"
                else:
                    result = "Cannot divide by zero"

            else:
                result = "Please select an operation"

            # Save only valid calculations
            if symbol:
                history.append(
                    f"{num1} {symbol} {num2} = {round(result, 2) if isinstance(result, (int, float)) else result}"
                )

        except ValueError:
            result = "Please enter valid numbers."

    return render_template(
        "index.html",
        result=result,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)