import lapindrome as lap

st=str(input("Enter String:"))
A=lap.lapindrome(st)
if A.chk_lapindrome():
    print("lapindrome")
else:
    print("not lapindrome")
