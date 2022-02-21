def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    rounded = []
    while student_scores:
        rounded.append(round(student_scores.pop()))
    return rounded


def count_failed_students(student_scores):
    """Count the number of failing students in the provided list.

    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    non_passing = 0
    for score in student_scores:
        if score <= 40:
            non_passing += 1
    return non_passing


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    above = []

    for score in student_scores:
        if score >= threshold:
            above.append(score)
    return above


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    increment = round((highest - 40)/4)
    scores = []
    for score in range(41, highest, increment):
        scores.append(score)
    return scores


def student_ranking(student_scores, student_names):
    """Create a list of strings that contain the student's rank, name, and grade in ascending order.

     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    results = []
    for index, name in enumerate(student_names):
        rank_string = str(index + 1) + ". " + name + ": " + str(student_scores[index])
        results.append(rank_string)

    return results


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    result = []

    for item in student_info:
        if item[1] == 100:
            result = item
            break

    return result
