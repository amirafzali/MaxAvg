from flask import Flask, render_template, request
from MaxAverage import app, calculate


@app.route('/', methods=['GET','POST'])
def home():
    test = "hello"
    print(test)
    if request.method == 'POST':
        grades = request.form.getlist('grades[]')
        weights = request.form.getlist('weights[]')
        calculate.processData([grades, weights])
        return render_template('grade.html')
    print("test")
    return render_template('grade.html', test=test)
