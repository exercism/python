Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed with currency exchange during his trip - and he wants you to make a currency calculator for him. Here's his specification for the app:

## 1. Estimate value after exchange

Create the `estimate_value()` function, where `budget` & `exchange_rate` are the two required parameters:

1. `budget` : the amount of money you are planning to exchange.
2. `exchange_rate` : unit value of the foreign currency.

This function should return the estimated value of the foreign currency you can receive based on your `budget` and the current `exchange rate`.

**Note:** If your currency is USD and you want to exchange USD for EUR with an exchange rate of `1.20`, then `1.20 USD` == `1 EUR`.

```python
>>> estimate_value(127.5, 1.2)
106.25
```

## 2. Calculate currency left after an exchange

Create the `get_change()` function, where `budget` & `exchanging_value` are the two required parameters:

1. `budget` : amount of money you own.
2. `exchanging_value` : amount of your money you want to exchange now.

This function should return the amount left of your starting currency after exchanging `exchanging_value`.

```python
>>> get_change(127.5, 120)
7.5
```

## 3. Calculate value of bills

Create the `get_value()` function, with parameters `denomination` & `number_of_bills`

1. `denomination` : the value of a single bill.
2. `number_of_bills` : amount of bills you received.

This function should return the total value of bills you now have.

```python
>>> get_value(5, 128)
640
```

## 4. Calculate number of bills

Create the `get_number_of_bills()` function, with parameters `budget` & `denomination`

1. `budget` : amount of money you are planning to exchange.
2. `denomination` : the value of a single bill.

This function should return the number of bills after exchanging all your money.

```python
>>> get_number_of_bills(127.5, 5)
25
```

## 5. Calculate value after exchange

Create the `exchangeable_value()` function, with parameter `budget`, `exchange_rate`, `spread`, & `denomination`.

1. `budget` : amount of your money you are planning to exchange.
2. `exchange_rate` : unit value of the foreign currency.
3. `spread` : percentage taken as exchange fee.
4. `denomination` : the value of a single bill.

This function should return the maximum value you can get considering the `budget`, `exchange_rate`, `spread`, & `denomination`.

**Note:** If `1 EUR` == `1.20 USD` and the spread is `10%`, the _actual exchange rate_ becomes `1 EUR` == `1.32 USD`.

```python
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
>>> exchangeable_value(127.25, 1.20, 10, 5)
95
```

## 6. Calculate unexchangeable value

Create the `unexchangeable_value()` function, with parameter `budget`, `exchange_rate`, `spread`, & `denomination`.

1. `budget` : amount of your money you are planning to exchange.
2. `exchange_rate` : unit value of the foreign currency.
3. `spread` : percentage taken as exchange fee.
4. `denomination` : the value of a single bill.

This function should return the unexchangeable value considering the `budget`, `exchange_rate`, `spread`, & `denomination`.

**Note:** Returned value should be `int` type.

```python
>>> unexchangeable_value(127.25, 1.20, 10, 20)
16
>>> unexchangeable_value(127.25, 1.20, 10, 5)
1
```
