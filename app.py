from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operations=request.form['operations']

        if operations=='add':
            result = num1 + num2

        elif operations=='sub':
            result= num1-num2
        elif operations=='mulit':
            result = num1 * num2
        elif operations=='div':
            result= num1//num2

        else:
            result="invalid value"

    return render_template('index.html', result=result)

app.run(debug=True)