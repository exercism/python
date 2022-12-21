# Instructions

The company you work for want to reduce their carbon footprint, so they wants you to write a program which calculates the power usage of their electronics and the cost of running them.

1. Get extra hours

Your employer wants a program that calculates the time it takes to run different electronics.
Currently the time is stored in hours.
When your employer added the hours they noticed that the time was not correct and they want you to add 3 extra hours to the time data.
They also would like to know how many hours needs to be removed to get the data in full days(24 hours).
The time given doesn't have to be in full days.

Implement a function `get_extra_hours()` that accepts an integer which holds the number of hours.
The function should then `return` an integer with how many hours which has to be removed to get the time in full days.

```python
>>> get_extra_hours(25)
4
```

2. Get kW value

Your employer wants to know the power usage of the different electronics.
They want to know the power usage in kW.
kW stands for kilowatt, there watts is a unit of power.
Kilo in the unit name is a prefix in the metric system meaning 1000.
So 1 kilowatt is equal to 1000 watts.

Implement a function `get_kW_value()` that accepts an integer which holds the number of watts.
The function should then `return` the watts as kilowatts rounded to 1 decimal.

```python
>>> get_kW_value(1150)
1.2
```

3. Get kwh value

To be able to calculate the cost of running the electronics your employer wants to know the power usage in kWh.
kWh stands for kilowatt-hour, there hour is a unit of time.
So 1 kilowatt-hour is equal to 1000 watts used for 1 hour.
An hour is made of 60 minutes and a minute is made of 60 seconds.
So 1 hour is equal to 3600 seconds.
To get the kWh value you have to have to convert the watts to kW and then floor-divide it by 3600.

Implement a function `get_kWh_value()` that accepts an integer which holds the number of watts.
The function should then `return` the watts as an integer.

```python
>>> get_kWh_value(5000000)
1
```

4. Get efficiency

Electronics are not 100% efficient.
Therefore your employer wants to know the efficiency of the electronics.
To get efficiency you have to divide the power factor by 100.
The power factor is a float between 0 and 100.

Implement a function `get_efficiency()` that accepts a float that holds the power factor.
The function should then `return` the power factor as a float.

```python
>>> get_efficiency(80)
0.8
```

5. Get cost

Your employer wants to know the cost of running the electronics.
The power used is the power given divided by the efficiency.
The cost of running the electronics is the power used multiplied by the cost per kWh.

Implement a function `get_cost()` that accepts an integer that holds the number of watts and a float that has the power factor and a float that holds the cost per kwh.
The function should then `return` the cost of running the electronics as a float rounded to 2 decimals.

```python
>>> get_cost(5000000, 80, 0.25)
0.3125
```
