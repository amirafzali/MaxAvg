def processData(*args):
    grades = args[0][0]
    weights = args[0][1]
    d_grade = int(args[0][2][0])
    d_weight = int(args[0][3][0])
    total_marks, total_weight = 0, 0
    for i in range(len(grades)):
        total_marks += float(grades[i]) * float(weights[i])
    curr_weight = sum(map(float, weights))
    total_weight = curr_weight + d_weight
    currentAvg = current_average(total_marks, curr_weight)
    desiredAvg = desired_average(total_marks, total_weight, d_grade, d_weight)

    return [currentAvg, desiredAvg]


def current_average(total_marks, curr_weight):
    return total_marks / curr_weight


def desired_average(total_marks, total_weight, d_grade, d_weight):
    mark = ((d_grade * total_weight) - total_marks) / d_weight
    return mark
