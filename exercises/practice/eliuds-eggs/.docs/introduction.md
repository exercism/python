# Introduction

Your friend Eliud inherited a farm from her grandma Tigist.
Her granny was an inventor and had a tendency to build things in an overly complicated manner.
The chicken coop has a digital display showing an encoded number representing the positions of all eggs that could be picked up.

Eliud is asking you to write a program that shows the actual number of eggs in the coop.

The position information encoding is calculated as follows:

1. Scan the potential egg-laying spots and mark down a `1` for an existing egg or a `0` for an empty spot.
2. Convert the number from binary to decimal.
3. Show the result on the display.

## Example 1

![Seven individual nest boxes arranged in a row whose first, third, fourth and seventh nests each have a single egg.](https://assets.exercism.org/images/exercises/eliuds-eggs/example-1-coop.svg)

```text
 _ _ _ _ _ _ _
|E| |E|E| | |E|
```

### Resulting Binary

![1011001](https://assets.exercism.org/images/exercises/eliuds-eggs/example-1-binary.svg)

```text
 _ _ _ _ _ _ _
|1|0|1|1|0|0|1|
```

### Decimal number on the display

89

### Actual eggs in the coop

4

## Example 2

![Seven individual nest boxes arranged in a row where only the fourth nest has an egg.](https://assets.exercism.org/images/exercises/eliuds-eggs/example-2-coop.svg)

```text
 _ _ _ _ _ _ _
| | | |E| | | |
```

### Resulting Binary

![0001000](https://assets.exercism.org/images/exercises/eliuds-eggs/example-2-binary.svg)

```text
 _ _ _ _ _ _ _
|0|0|0|1|0|0|0|
```

### Decimal number on the display

8

### Actual eggs in the coop

1
