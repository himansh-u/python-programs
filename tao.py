#to print fibonacci series upto n terms using a user defined function
def fib(n):
  a,b=-1,1
  for i in range(n):
    print(a+b,end="")
    a,b=b,a+b
n=int(input("enter the no in terms of fibonacci series"))
fib(n)
