def round_scores(student_scores):
    rounded = []
    while student_scores:
        rounded.append(round(student_scores.pop()))
    return rounded


def count_failed_students(student_scores):
    non_passing = 0
    for score in student_scores:
        if score <= 40:
            non_passing += 1
    return non_passing


def above_threshold(student_scores, threshold):
    above_threshold = []
    for score in student_scores:
        if score >= threshold:
            above_threshold.append(score)
    return above_threshold


def letter_grades(highest):
    increment = round((highest - 40)/4)
    scores = []
    for score in range(41, highest, increment):
        scores.append(score)
    return scores


def student_ranking(student_scores, student_names):
    results = []
    for index, name in enumerate(student_names):
        rank_string = str(index + 1) + ". " + name + ": " + str(student_scores[index])
        results.append(rank_string)
        #results.append(f"{index + 1}. {name}: {student_scores[index]}")
    return results


def perfect_score(student_info):
    result = "No perfect score."
    for item in student_info:
        if item[1] == 100:
            result = item
            break
        else:
            continue
    return result
