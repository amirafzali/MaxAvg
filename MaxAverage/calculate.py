def processData(*args):
    grades = args[0][0]
    weights = args[0][1]
    dGrade = args[0][2]
    dWeight = args[0][3]
    totalMarks, totalWeight= 0,0
    for i in range(len(grades)):
        totalMarks += float(grades[0])*float(weights[0])
    totalWeight = sum(map(float, weights))
    print(grades,weights)
    print(totalWeight, totalMarks, dWeight, dGrade)
