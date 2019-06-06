def check(num):
    one,two,three=False,False,False
    a=num
    while a!=0:
        if a%10==1: one=True
        elif a%10==2: two=True
        elif a%10==3: three=True
        a=a/10
    return one and two and three

def findQualifiedNumbers(numberArray):
    result=[]
    for i in numberArray:
        if check(i): result.append(i)
    return ','.join(map(str,sorted(result)))

print findQualifiedNumbers([2])