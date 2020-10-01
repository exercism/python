def is_armstrong_number(num):
    # Changed num variable to string, 
    # and calculated the length (number of digits)
    order = len(str(num))

    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

    # display the result
    if num == sum:
       return (num,"is an Armstrong number")
    else:
       return (num,"is not an Armstrong number")
print(is_armstrong_number(int(input())))
