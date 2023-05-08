def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if x <=100 and x >=85:
            grade_counter[0] += 1
        elif x <=84 and x >=70:
            grade_counter[1] += 1
        elif x <=69 and x >=55:
            grade_counter[2] += 1
        elif x <=54 and x >=40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter