from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 25487895, number2 = 99885555)

@app.route('/sum')
def number():
    var1, var2 = 458810,42278727260
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1+var2)


if __name__ == '__main__':
    app.run(debug=True)
white_check_mark
eyes
raised_hands












