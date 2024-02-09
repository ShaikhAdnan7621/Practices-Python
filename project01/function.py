def saprate_num(s):
    oprator="+*-/%"
    k=[]
    temp=""
    for i in range(0,len(s)):
        if s[i] in oprator:
            k.append(temp)
            temp=""
            k.append(s[i])
        else:
            temp=temp+s[i]
        if i ==len(s)-1:
            k.append(temp)
    return k
def division_str(b):
    d=0
    for i in b:
        if i=="/":
            d+=1
    if d==0:
        return b
    for i in range(0,len(b)):
        if b[i]=="/":
            x=float(b[i-1])
            y=float(b[i+1])
            b.pop(i+1)
            b.pop(i)
            b[i-1]=str((x/y))
            division_str(b)
            return (b)
def multyply_str(b):
    d=0
    for i in b:
        if i=="*":
            d+=1
    if d==0:
        return b
    for i in range(0,len(b)):
        if b[i]=="*":
            x=float(b[i-1])
            y=float(b[i+1])
            b.pop(i+1)
            b.pop(i)
            b[i-1]=str((x*y))
            multyply_str(b)
            return (b)
def addition_str(b):
    d=0
    for i in b:
        if i=="+":
            d+=1
    if d==0:
        return b
    for i in range(0,len(b)):
        if b[i]=="+":
            x=float(b[i-1])
            y=float(b[i+1])
            b.pop(i+1)
            b.pop(i)
            b[i-1]=str((x+y))
            addition_str(b)
            return (b)
def subtraction_str(b):
    d=0
    for i in b:
        if i=="-":
            d+=1
    if d==0:
        return b
    for i in range(0,len(b)):
        if b[i]=="-":
            x=float(b[i-1])
            y=float(b[i+1])
            b.pop(i+1)
            b.pop(i)
            b[i-1]=str((x-y))
            subtraction_str(b)
            return (b)
def convert_in_str(s):
    s=list(s[0])
    p=""
    for i in s:
        p=p+i
    return p


def result_str(b):
    s=0
    for i in b:
        if i in "+-*/%":
            s=1
    if s==0:
        return b
    if len(b)<=2:
        return b
    if b[-1] in "+-*/%":
        b=b[:-1]
    b=saprate_num(b)
    b=division_str(b)
    b=multyply_str(b)
    b=addition_str(b)
    b=subtraction_str(b)
    b=convert_in_str(b)
    b=float(b)
    if b%1==0.0:
        b=int(b)
        b=str(b)
        return b
    else:
        b=str(b)
        return b