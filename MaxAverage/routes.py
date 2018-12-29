from flask import Flask, render_template, request, jsonify
from MaxAverage import app, calculate


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        grades = request.form.getlist('grades[]')
        weights = request.form.getlist('weights[]')
        dGrade = request.form.getlist('dGrade')
        dWeight = request.form.getlist('dWeight')
        processed = calculate.processData([grades, weights, dGrade, dWeight])
        currAvg = round(processed[0], 2)
        reqAvg = round(processed[1], 2)

        return jsonify({'currAvg':currAvg, 'reqAvg':reqAvg})
    return render_template('grade.html')
