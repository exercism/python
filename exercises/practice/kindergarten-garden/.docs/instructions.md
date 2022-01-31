# Instructions

Given a diagram, determine which plants each child in the kindergarten class is
responsible for.

The kindergarten class is learning about growing plants. The teacher
thought it would be a good idea to give them actual seeds, plant them in
actual dirt, and grow actual plants.

They've chosen to grow grass, clover, radishes, and violets.

To this end, the children have put little cups along the window sills, and
planted one type of plant in each cup, choosing randomly from the available
types of seeds.

```text
[window][window][window]
........................ # each dot represents a cup
........................
```

There are 12 children in the class:

- Alice, Bob, Charlie, David,
- Eve, Fred, Ginny, Harriet,
- Ileana, Joseph, Kincaid, and Larry.

Each child gets 4 cups, two on each row. Their teacher assigns cups to
the children alphabetically by their names.

The following diagram represents Alice's plants:

```text
[window][window][window]
VR......................
RG......................
```

In the first row, nearest the windows, she has a violet and a radish.  In the
second row she has a radish and some grass.

Your program will be given a diagram of plants from left-to-right starting with
the row nearest the windows. The plant diagram will be a single string,
with a newline character separating the rows. Optionally, your program will get a list of 
students other than the 12 listed above. Your program should be able to determine
which plants belong to a particular student.

For example, suppose it's told that the garden looks like so:

```text
[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
```

Assuming the students are the 12 listed above, if asked for Alice's plants, 
the program should return this list:

- \["Violets", "Radishes", "Violets", "Radishes"\]

While asking for Bob's plants would yield:

- \["Clover", "Grass", "Clover", "Clover"\]

If your program is given a list of students other than the twelve listed above,
the students will be assigned two plants per row each, starting from the left,
in alphabetical order by name (even if the names are out of order on the list).
