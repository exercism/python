<!--
Date: 26 Jan 2021
This is a draft to see if this is question theme is suitable or not and will change according to
review feedback

Date : 27 Jan 2021
Second Review, the task are satisfactory. Now Improving the first review
 -->

In this exercise, we will develop a simple control system for a nuclear reactor.

For a reactor to produce the power it must be in a state of criticality.
If the reactor becomes less than criticality it can damage the reactor.
If it goes beyond criticality it can result in a meltdown.

You have three task, all related to maintaining the criticality of the reactor.

<!-- Problem 1 to teach basic if condition -->

## 1. Check for criticality

The first thing a control system must do is to check if the reactor is critical.
A reactor is said to be critical if it satisfies the following conditions.

- Temperature less than 800
- Number of neutrons emitted per second greater than 500
- The product of temperature and neutrons emitted per second less than 500000

Implement a function called `is_criticality_balanced()` that takes in 2 arguments the temperature
and neutrons emitted per second and returns a boolean True or False

```python
>>> is_criticality_balanced(750, 600)
True
```

<!-- For teaching elif -->

## 2. Determine the Power output range

Now that the reactor has started producing power we need to determine the efficiency of
the reactor.
The efficency can be grouped into 4 bands.

- green -> 80-100% efficency
- orange -> 60-79% efficency
- red -> 30-59% efficency
- black -> <30% efficent

efficency is calculated as `(generated power/ theoretical max power)*100`
where generated `power = voltage * current`

Implement a function called `reactor_efficency()` that takes in 3 arguments: `voltage`,
`current`, and `theoretical_max_power`. The function returns the efficiency band of the
reactor either 'green', 'orange', 'red', 'black'

```python
>>> reactor_efficency(200,50,1500)
'orange'
```

<!-- Intention is to teach use of if, elif and else -->

## 3. Fail Safe Mechanism

The final part involves creating a fail-safe mechanism. We can increase/decrease or stop the
criticality state of a reactor by inserting control rods into the reactor.

Implement a function called `fail_safe()` which takes in 3 parameters: `temperature`,
`neutrons produced per second`, and `threshold` to outputs status codes.

- If `temperature * neutrons per second` < 40% of threshold, output a status code of 'LOW'
  indicating that the control rods must be removed to make it go critical and produce power

- If `temperature * neutrons per second` are within plus or minus 10% of the `threshold`
  the reactor is in criticality and outputs a status code of 'NORMAL' , indicating that the
  reactor is in optimum condition and control rods are in an idea position

- If `temperature * neutron per second` is not in the above-stated ranges. The reactor is
  going into meltdown and a status code of 'DANGER' must be passed to immediately shut down the reactor
