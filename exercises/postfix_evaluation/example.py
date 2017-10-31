# importing the liberary
from postfix_evaluation import postfix_evaluation

exp = "43+1"
ev = postfix_evaluation(exp)
ans = ev.evaluate()
print("main ans : ",ans)
