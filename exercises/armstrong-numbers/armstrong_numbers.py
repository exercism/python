def is_armstrong_number(number):
    org_num = number
    sum = 0
    try:
        while (number!=0):
            digit = number%10
            sum = sum+ digit**len(str(org_num))
            number = number//10
        if sum == org_num:
            return True
        else:
            return False

    except Exception as e:
        print("Input is not a number. Please Enter a number", e)





