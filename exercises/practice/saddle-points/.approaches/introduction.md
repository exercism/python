# Introduction

There are several  Pythonic ways to solve the Saddle Points exercise.
Among them are:

- Use `loops` and appending to `lists`
- Use `list-comprehensions` for max/min and a nested `loop` for results.
- Use `list-comprehensions` for max/min and a nested `list comprehension` for results.
- Use nested `list-comprehensions` for max/min _with_ coordinates and a `list-comprehension` for results.
- Use nested `set-comprehensions` for max/min  _with_ coordinates and a `list-comprehension` for results.


## General guidance


The goal of the Saddle Points exercise is to identify points in a number matrix (_modeled here as a `list` of `lists`_) where:

* The point is the **maximum** value in its row.
* The point is the **minimum** value in its column.

Points are returned as a list of _coordinate dictionaries_ `{'row':<row number>, 'column': <column number>}`.
The challenge here is to find an efficient method of extracting the coordinates from the matrix that match the max/min criteria.

In core Python, a loop-within-loop cannot be easily avoided, due to the nested nature of the matrix representation.
All strategies here employ nested loops  either in calculating the min/max, or in finding the row/column coordinates within the input matrix.


## Approach: Use Loops & Nested Loops and Append To Lists

```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    else:
        row_maxima = []
        column_minima = []
        results = []

        for row in matrix:
            row_maxima.append(max(row))

        for column in zip(*matrix):
            column_minima.append(min(column))
            
        for idx, value in enumerate(matrix[0]):
            for index, value in enumerate(matrix):
                if row_maxima[index] == column_minima[idx]:
                    results.append({'row': index+1, 'column': idx+1})

        return results
```

This approach uses a series of loops and nested loops to iterate row-wise for max values, column-wise for min values, and matrix-wise for coordinates.
As max/min values are found, they are appended to row_maxima and column_minima lists.
Once the max and min lists are compiled, the matrix is traversed in a nested loop.
Where a row_maxima is also a column_minima, the resulting coordinates are appended to the _restults_ list.
For more information, see the [Loop and Append to List][loop-and-append] approach.


## Approach: Use List Comprehensions for Max/Min and a Nested Loop for Finding Coordinates

```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    else:
        row_maxima = [max(row) for row in matrix]
        column_minima = [min(col) for col in zip(*matrix)]
        
        results = []

        for idx, value in enumerate(matrix[0]):
            for index, element in enumerate(matrix):
                if row_maxima[index] == column_minima[idx]:
                    results.append({'row': index+1, 'column': idx+1})
        

    return results or []
```

This approach uses [`list comprehensions`][list-comprehensions] to compile the row_maxima and column_minima lists.
Once the max/min `lists` are compiled, the matrix is traversed in a nested loop, and the coordinates where row_maxima == column_minima are appended to the _results_ `list`.
For details, check out the [List Comprehensions and Nested Loop][ list-comprehension-and-nested-loop] approach.


## Approach: Use List Comprehensions for Max/Min & A Nested List Comprehension for Finding Coordinates


```python
def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("irregular matrix")
        
    row_maxima = [max(row) for row in matrix]
    col_minima = [min(col) for col in zip(*matrix)]
    
    return [{"row": rindex, "column": cindex} for 
            rindex, row in enumerate(matrix, start=1) for
            cindex, _ in enumerate(row, start=1) if
            row_maxima[rindex-1] == col_minima[cindex-1]]
```


Like the approach above, two `list comprehensions` are used to compile row_maxima and column_minima.
Once the two lists are compiled, a nested `list comprehension` is then used to both traverse the matrix and compile the coordinate result list.
For more information, read the [List Comprehensions and Nested list Comprehension][list-comprehension-and-nested-list-comprehension] approach.



## Approach: Use Nested List Comprehensions for Max/Min/Coordinates and a List Comprehension for Results



```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(item) != len(matrix[0]) for item in matrix):
        raise ValueError("irregular matrix")
    
    else:
        row_maxima = [(index, eindex, element) for index, row in
                       enumerate(matrix) for eindex, element in 
                       enumerate(row) if max(row) == element]


        col_minima = [(eindex, index, element) for index, col in
                       enumerate(zip(*matrix)) for eindex, element in
                       enumerate(col) if min(col) == element]


    return [{'row': item[0]+1, 'column': item[1]+1} for 
            item in col_minima if item in row_maxima]
```

In this approach, the nested loops appear in the row_maxima and column_minima `list comprehensions`, which also compile the coordinates of each max/min 'point'.
The results are then compiled in a list comprehension that matches row entries to column entries.
For more information, see the [nested list comprehensions with coordinates][nested-list-comprehensions-with-coordinates] approach.


## Approach: Use Nested Set Comprehensions for Max/Min/Coordinates and a List Comprehension for Results

```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    else:
        row_maxima = {(index, eindex, element) for index, row in
                       enumerate(matrix, start=1) for eindex, element in 
                       enumerate(row, start=1) if max(row) == element}


        column_minima = {(eindex, index, element) for index, col in
                          enumerate(zip(*matrix), start=1) for eindex, element in
                          enumerate(col, start=1) if min(col) == element}


    return [{'row': item[0], 'column': item[1]} for 
            item in row_maxima & column_minima]
```

This approach is very similar to the one above, but uses nested  `set comprehensions` to compile row_maxima, column_minima, and 'point' coordinates.
The results are then compiled in a `list comprehension` that iterates over the set intersection of  row_maxima & column_minima.
For details, see the [nested set comprehension with coordinates][nested-set-comprehensions-with-coordinates] approach.



## Other approaches


Beside these five idiomatic approaches, there are a multitude of possible variations using different combinations of loops, comprehensions, and filtering methods.

However, it is very difficult to avoid nested loops, as each column of each row (_or vice-versa_) has to be identified by (row, column) coordinates and checked  to see if the 'point' fulfills the Max/Min requirements.


## Which approach to use?


All of these approaches are roughly equivalent given the nested nature of the data.

Using comprehensions and sets might still give a slight performance boost, but they may also be harder to read or understand for others.
The naive approach of loops and list-append is most likely the easiest to follow for those not familiar with the comprehension form.


[ list-comprehension-and-nested-loop]:https://exercism.org/tracks/python/exercises/saddle-points/approaches/list-comprehension-and-nested-loop
[ loop-and-append]:  https://exercism.org/tracks/python/exercises/saddle-points/approaches/loop-and-append
[list-comprehension-and-nested-list-comprehension ]:https://exercism.org/tracks/python/exercises/saddle-points/approaches/list-comprehension-and-nested-list-comprehension
[list-comprehensions]: https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/#:~:text=What%20are%20list%20comprehensions%3F,can%20be%20transformed%20as%20needed.
[nested-list-comprehensions-with-coordinates ]:https://exercism.org/tracks/python/exercises/saddle-points/approaches/nested-list-comprehensions-with-coordinates
[nested-set-comprehensions-with-coordinates ]:https://exercism.org/tracks/python/exercises/saddle-points/approaches/nested-set-comprehensions-with-coordinates

