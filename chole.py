f.open("t.txt","w")
N=["Anjali\n","Suhana\n"]
f.writelines(N)
f.close

#to add 5 student name
f.open("a.txt","w")
L=[]
for i in range(5):
  L.append(input("enter the name of the student"))
  f.writelines(L)
f.close()  

#wap to store adno name and marks in 3 sub of n stu in a text file result.txt

f=open("result.txt","w")
n=int(input("enter the number of students"))
for i in range(n):
  adno=int(input("enter the adno"))
  name=input("enter the names")
  print("enter marks in 3 subjects")
  a,b,c=int(input()),int(input()),int(input())
  R=str(adno)+','+name+','+str(a)+','+str(b)+','+str(c)+'\n'
  f.write(R)
f.close()  

#wap to read test.txt line by line and print each line on screen

f=open("test.txt","r")
a=" "
while a:
    a=f.readline()
    print(a)
f.close()    
#
f=open("test.txt","r")
a=" "
while a:
    a=f.readline()
    print(a.strip())
f.close()    
#
X=open('test.txt','r')
for i in X:
  print(X)
X.close()  

#4

f=open("student.txt","r")
L=f.readlines()
s=1
for i in L:
  print(str(s)+'.',i,end=""
  s+=1
f.close()        
  
#5
f=open('RESULT.txt','r')
print('adno','name','total',sep ='\t')  
for i in f:
        a=i.split(',')
        print(a[0],a[1],int(a[2]),int(a[3]),int(a[4]), sep ='\t')
f.close()        
#
f=open('result.txt')
print('students scoring more than 75 percent are:')
for i in f:
        a=split(',')
        t=0
for j in range(2,5):
        t+=int(a[j])
p=t/3
if p>75:
        print(a[1])
f.close()
        
##
f=open(poem.txt)
c=c1=0
words=f.read().split()
for i in words:
        if i.lower()=="the":
             c+=1
        if i .lower()=="to":
             c1=c+1
print("count of word the",c)
print("count of word to",c1)
f.close()        

def DISPLAYWORDS():
    f=open('story.txt')
    print("those words which are less than char 4:")
    for word in f.read().split():
        if len(word)<4:
            print(word)
    f.close()            
 
        
