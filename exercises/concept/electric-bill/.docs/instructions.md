# Instructions

The company you work for wants to reduce their carbon footprint, so they want you to write a program to calculate the power usage and cost of running their electronics.

## 1. Get extra hours

Your employer has a program that calculates the time it takes to run different electronics.
Currently, the time is stored in hours.
When your employer added the hours, they noticed that the time duration was not correct.
They want you to add 3 extra hours to the time data.
They would also like to know how many "extra" hours there are after converting the data to "full" days (a day is 24 hours).
The time to convert may not be in full days.

Implement a function `get_extra_hours()` that accepts an integer which holds the number of hours.
The function should make the appropriate "extra hours" adjustment, and then `return` an integer representing how many hours needs to be removed from the total to get the time in "full" days.

```python
>>> get_extra_hours(25)
4
```

## 2. Get kW value

Your employer wants to know the power usage of the different electronics in kW.
kW stands for kilowatt, where watts are a unit of power.
Kilo in the unit name is a prefix in the metric system meaning 1000.
One kilowatt == 1000 watts.

Implement a function `get_kW_value()` that accepts an integer which holds the number of watts.
The function should then `return` the watts as kilowatts rounded to 1 decimal place.

```python
>>> get_kW_value(1150)
1.2
```

## 3. Get kWh value

To be able to calculate the cost of running the electronics, your employer needs to know the power usage in kWh.
kWh stands for kilowatt-hour, where hour is a unit of time.
One kilowatt-hour == 1000 watts used for 1 hour.
An hour is made up of 60 minutes and a minute is made up of 60 seconds.
One hour is equal to 3600 seconds.
To calculate the kWh value, you must convert watts to kW, and then floor-divide the result by 3600.

Implement a function `get_kWh_value()` that accepts an integer which holds the number of watts.
The function should then `return` the kilowatt-hours as an integer.

```python
>>> get_kWh_value(5000000)
1
```

## 4. Get efficiency

Electronics are not 100% efficient.
Therefore, your employer wants you to calculate the _efficiency_ of the electronics.
To get efficiency, you must divide the power factor (_a float between 0 and 100_) by 100.

Implement a function `get_efficiency()` that accepts a float that holds the power factor.
The function should then `return` the calculated efficiency as a float.

```python
>>> get_efficiency(80)
0.8
```

## 5. Get cost

Your employer wants to know the cost of running the electronics.
The cost of running the electronics is the power used multiplied by the cost per kWh.
The power used is the power given divided by the calculated efficiency.

Implement a function `get_cost(<watts>,<power_factor>,<price>)` that accepts an integer that holds the number of watts, a float that has the power factor, and a float that holds the cost per kWh.
The function should then `return` the cost of running the electronics as a float.

```python
>>> get_cost(5000000, 80, 0.25)
0.3125
```
