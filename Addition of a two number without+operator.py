def Add_no(x,y):
    while(y!=0):
        carry = x&y
        x=x^y
        y= carry<<1
    return x

Add_no(2,4)

