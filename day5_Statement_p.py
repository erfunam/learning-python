n = int(input("Enter number : "))

if (n % 3 == 0) and (n % 5 == 0) :
    print ("افسانه ای")
elif n % 3 == 0 :
    print ("جادویی")
elif n % 5 == 0 :
    print ("نفرین شده")
elif not (1 <= n < 1000) :
    print ("out of range!")
else :
    print ("معمولی")