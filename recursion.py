
def recursion(num):
    for i in range(len(num)):
        print(num[i])
        
def recursion2(num,summ):
    summ += num
    num = num-1
    if num ==0:
        print(summ)
    else:
        recursion2(num,summ)
        
def recursion3(num):
    if num <=1:
        return 1
    else:
        return num+recursion3(num-1)
        
def recursion4(num,expo):
    if expo <=1:
        return num
    else:
        return num* recursion4(num,expo-1)
    
def recursion5(num):
    if num/10 < 1:
        return num
    else:
        return num%10+recursion5(int(num/10))



    
    

def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

#factorial(4)
#recursion("351")
summ= 0
recursion2(5,summ)
print(recursion3(5))
print(recursion4(2,4))
print(recursion5(234))
