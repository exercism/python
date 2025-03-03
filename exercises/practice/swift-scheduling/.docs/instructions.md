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
| `"ASAP"`    | Before 12:00                  | Today at 17:00                      |
| `"ASAP"`    | After 12:00                   | Tomorrow at 12:00                   |
| `"EOW"`     | Monday, Tuesday, or Wednesday | Friday at 17:00                     |
| `"EOW"`     | Thursday or Friday            | Sunday at 20:00                     |

## Variable delivery date descriptions

There are two variable delivery date description patterns:

- `"<N>M"` (N-th month)
- `"Q<N>"` (N-th quarter)

| Description | Meeting start              | Delivery date                                               |
| ----------- | -------------------------- | ----------------------------------------------------------- |
| `"<N>M"`    | Before N-th month          | At 8:00 on the _first_ workday¹ of this year's N-th month   |
| `"<N>M"`    | After or in N-th month     | At 8:00 on the _first_ workday¹ of next year's N-th month   |
| `"Q<N>"`    | Before or in N-th quarter² | At 8:00 on the _last_ workday¹ of this year's N-th quarter² |
| `"Q<N>"`    | After N-th quarter²        | At 8:00 on the _last_ workday¹ of next year's N-th quarter² |

¹ A workday is a Monday, Tuesday, Wednesday, Thursday, or Friday.
² A year has four quarters, each with three months: January/February/March, April/May/June, July/August/September, and October/November/December.
