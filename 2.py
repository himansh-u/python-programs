def isprime(n):
  c=1
  for i in range(2,n):
    if n%1==0:
      c=0
  if c==1:
    return 1
  else:
    return 0
n=int(input("enter any number"))
if isprime(n):
  print("number is prime")
else:
  print("number is not prime")
 
#to input a number and check whether it is aprime no or not using a user defined function.
