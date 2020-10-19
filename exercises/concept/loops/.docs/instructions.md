You are a teacher and you are correcting papers of your students who wrote an exam you just conducted. You are tasked with the following activities.

## 1. Failed Students

Create the function `count_failed_students()` that takes one parameter: `student_marks`. This function should count the number of students who have failed the subject, returning the count as an integer. We say that a student has failed if their mark is less than or equal to **40**.

Note: `Iterate` through the student marks to find out your answer.
​
Result should be an `int`.

```python
>>> count_failed_students(student_marks=[90,40,55,70,30]))
2
```

## 2. Top Marks

The Headmaster wants to find the group of top students. What qualifies student marks as `top marks` fluctuates, and you will need to find the student marks that are **greater than or equal to** the current threshold.

Create the function `above_threshold()` where `student_marks` and `threshold` are the two required parameters:

1. `student_marks` are a list of marks for each student
2. `threshold` is the top mark threshold. Marks greater than or equal to this number are considered "top marks" .

This function should return a `list` of all marks that are greater than or equal to a scoring threshold.

**Note:** If you find a mark which is less than the threshold, you should `continue` to evaluating the next mark.​

```python
>>> above_threshold(student_marks=[90,40,55,70,30], 70)
[90, 70]
```

## 3. First K Students.

Create the function `first_k_student_marks()` with parameters `student_marks` and `k`

1. Student marks are a list of marks of each student
2. k is the number of students.

You need to return the first K number of student Marks. Once you reach K number of students, you should exit out of the loop.

```python
>>> first_k_student_marks(student_marks=[90,80,100], k=1)
[90]
```

## 4. Full Marks

Create the function `perfect_score()` with parameter `student_info`.
`student_info` is a dictionary containing the names and marks of the students `{"Charles": 90, "Tony": 80}`

Find if we have any students who scored "full marks"(_100%_)on the exam. If we don't find any "full marks" in `student_info`, we should return "No hundreds"

Return the first student who has scored full marks - 100.

```python
>>> perfect_score(student_info={"Charles": 90, "Tony": 80, "Alex":100})
Alex
>>> perfect_score(student_info={"Charles": 90, "Tony": 80})
No hundreds
```
