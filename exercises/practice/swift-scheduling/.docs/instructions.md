# Instructions

Your task is to convert delivery date descriptions to _actual_ delivery dates, based on when the meeting started.

There are two types of delivery date descriptions:

1. Fixed: a predefined set of words.
2. Variable: words that have a variable component, but follow a predefined set of patterns.

## Fixed delivery date descriptions

There are three fixed delivery date descriptions:

- `"NOW"`
- `"ASAP"` (As Soon As Possible)
- `"EOW"` (End Of Week)

The following table shows how to translate them:

| Description | Meeting start                 | Delivery date                       |
| ----------- | ----------------------------- | ----------------------------------- |
| `"NOW"`     | -                             | Two hours after the meeting started |
| `"ASAP"`    | Before 13:00                  | Today at 17:00                      |
| `"ASAP"`    | After or at 13:00             | Tomorrow at 13:00                   |
| `"EOW"`     | Monday, Tuesday, or Wednesday | Friday at 17:00                     |
| `"EOW"`     | Thursday or Friday            | Sunday at 20:00                     |

## Variable delivery date descriptions

There are two variable delivery date description patterns:

- `"<N>M"` (N-th month)
- `"Q<N>"` (N-th quarter)

| Description | Meeting start             | Delivery date                                             |
| ----------- | ------------------------- | --------------------------------------------------------- |
| `"<N>M"`    | Before N-th month         | At 8:00 on the _first_ workday of this year's N-th month  |
| `"<N>M"`    | After or in N-th month    | At 8:00 on the _first_ workday of next year's N-th month  |
| `"Q<N>"`    | Before or in N-th quarter | At 8:00 on the _last_ workday of this year's N-th quarter |
| `"Q<N>"`    | After N-th quarter        | At 8:00 on the _last_ workday of next year's N-th quarter |

~~~~exercism/note
A workday is a Monday, Tuesday, Wednesday, Thursday, or Friday.

A year has four quarters, each with three months:
1. January/February/March
2. April/May/June
3. July/August/September
4. October/November/December.
~~~~
