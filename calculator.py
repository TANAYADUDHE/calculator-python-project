a=int(input("enter the first value"))
b=input("enter th operator")
c=int(input("enter the second value"))
d=0
if b=="+":
  d=a+c
elif b=="-":
   d=a-c
elif b=="*":
   d=a*c
elif b=="/":
   if c!=0:
      d=a/c
   else:
      print("can not divided by 0")
else:
   print("invalid")
  
print(f"result {d}")