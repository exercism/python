For loops are traditionally used for repeating the code(written inside the loop) for fixed number of times.
example:-
for i in range(5):
    print(i)
in the above example of a for loop, the loop will run for 5 times, printing the value of i each time the loop code is processed.So the output of the above example will be:-
0
1
2
3
4
Loop can also be terminated in between by the use of any specified condition. Let's say for the same example now we want break the loop once the value of i is equal to 2, so we can achieve this condition by using 'break' command as follows:-
for i in range(5):
   if i == 2:
       break
   else:
       print(i)
Output of the above code will  be:-
0
1
2
as you can see, once the value of i is reached to 2 the loop is terminated.
