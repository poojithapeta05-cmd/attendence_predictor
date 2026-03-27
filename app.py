from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        total = int(request.form['total'])
        attended = int(request.form['attended'])

        percentage = (attended / total) * 100

        if percentage >= 75:
            result = f"Your attendance is {percentage:.2f}%. You are safe!"
        else:
            needed = int(((75 * total) - (attended * 100)) / 25 + 1)
            result = f"Your attendance is {percentage:.2f}%. Attend next {needed} classes."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)