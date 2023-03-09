# Truthy and Falsey Values with f-strings

```python
def convert(number):
    threes = '' if number % 3 else 'Pling' # Empty string if there is a remainder
    fives =  '' if number % 5 else 'Plang'
    sevens = '' if number % 7 else 'Plong'
    
    return f'{threes}{fives}{sevens}' or str(number)
  
  #OR#
  
def convert(number):
    threes = 'Pling' if not number % 3 else '' # Sound if there is NOT a remainder
    fives =  'Plang' if not number % 5 else ''
    sevens = 'Plong' if not number % 7 else ''
    
    return f'{threes}{fives}{sevens}' or str(number)
```
