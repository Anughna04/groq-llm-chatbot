#Strings &numeric values can operate togetheer with *
a,b=2,3
txt="@"
print(2*txt*3)#output is:@@@@@@

#STRING AND STRING CAN OPERATE WITH +:this is concatenation
a,b="2",3
txt="@"
print((a+txt)*b)#output:2@2@2@

#arithmetic expression with integer and float will result in float
#result of division operator with two integers will be float
#integer division(floor division//) with float and int will give int displayed as float
a,b=1.5,3
c=a//b
print(c,a/b)#OUTPUT:0.0 0.5

#floor gives closest integer,which is lesser than or equal to the float value

#remainder(%) is negative when the denominator is -ve

#TERNARY OPERATOR
#way 1:::<var>=<val1> if<condition>else<val2>
food=input("food:")
eat="Yes" if food=="cake" else "no"
print(eat)
#way2:::<stt1> if<condition>else<stt2>
food=input("food:")
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")
#Clever if
#var>=(false_val,true_val)[<condition>]..you can keep the condition in the square brackets
age=int(input("age:"))
vote=("no","yes") [age>=18]

sal=float(input("salary:"))
tax=sal*(0.1,0.2) [sal<=50000]
print(tax)

