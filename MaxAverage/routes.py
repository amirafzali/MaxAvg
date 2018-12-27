from flask import Flask, render_template, request
from MaxAverage import app


@app.route('/', methods=['GET','POST'])
def home():
    test = "hello"
    print(test);
    if request.method == 'POST':
        date = request.form;
    return render_template('grade.html', test=test)
