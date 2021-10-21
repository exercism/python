# Instructions

Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency calculator for him. Here are his specifications for the app:

## 1. Estimate value after exchange

Create the `exchange_money()` function, taking 2 parameters:

1. `budget` : The amount of money you are planning to exchange.
2. `exchange_rate` : Unit value of the foreign currency.

This function should return the value of the exchanged currency.

**Note:** If your currency is USD and you want to exchange USD for EUR with an exchange rate of `1.20`, then `1.20 USD == 1 EUR`.

```python
>>> exchange_money(127.5, 1.2)
106.25
```

## 2. Calculate currency left after an exchange

Create the `get_change()` function, taking 2 parameters:

1. `budget` : Amount of money before exchange.
2. `exchanging_value` : Amount of money that is *taken* from the budget to be exchanged.

This function should return the amount of money that *is left* from the budget.

```python
>>> get_change(127.5, 120)
7.5
```

## 3. Calculate value of bills

Create the `get_value_of_bills()` function, taking 2 parameters:

1. `denomination` : The value of a single bill.
2. `number_of_bills` : Amount of bills you received.

This function should return the total value of the given *bills*.

```python
>>> get_value_of_bills(5, 128)
640
```

## 4. Calculate number of bills

Create the `get_number_of_bills()` function, taking `budget` and `denomination`.

This function should return the *number of bills* that you can get using the *budget*.
**Note: ** You can only receive _whole bills_, not fractions of bills,  so remember to divide accordingly.
```python
>>> get_number_of_bills(127.5, 5)
25
```

## 5. Calculate value after exchange

Create the `exchangeable_value()` function, taking `budget`, `exchange_rate`, `spread`, and `denomination`.

Parameter `spread` is the *percentage taken* as an exchange fee.
If `1.00 EUR == 1.20 USD` and the *spread* is `10`, the actual exchange will be: `1.00 EUR == 1.32 USD`.

This function should return the maximum value of the new currency after calculating the *exchange rate* plus the *spread*.
Remember that the currency *denomination* is a whole number, and cannot be sub-divided.

**Note:** Returned value should be `int` type.

```python
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
>>> exchangeable_value(127.25, 1.20, 10, 5)
95
```

## 6. Calculate non-exchangeable value

Create the `non_exchangeable_value()` function, taking `budget`, `exchange_rate`, `spread`, and `denomination`.

This function should return the value that is *not* exchangeable due to the *denomination* of the bills.

**Note:** Returned value should be `int` type.

```python
>>> non_exchangeable_value(127.25, 1.20, 10, 20)
16
>>> non_exchangeable_value(127.25, 1.20, 10, 5)
1
```
