from flask import Flask, render_template, request
from MaxAverage import app, calculate


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        grades = request.form.getlist('grades[]')
        weights = request.form.getlist('weights[]')
        dGrade = request.form.getlist('dGrade')
        dWeight = request.form.getlist('dWeight')
        calculate.processData([grades, weights, dGrade, dWeight])
        return render_template('grade.html')
    return render_template('grade.html')
