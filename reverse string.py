
def get_str1(str1):
    leg_str1=len(str1)
    print(leg_str1)
    c=0
    for i in range(len(str1)):
        num= (len(str1)-1) -i
        if str1[i]==str1[(len(str1)-1)-i]:
           continue
        else:
            c=1
    return c ==0
print(get_str1("BOB"))
