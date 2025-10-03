print("Today is day one")
print("Today is day one")
flower=[]

for i in range(11):
  flower.append(i)
  print (flower[i-1])
for i in range(1,51):
    print(i)

for i in range(6):
    print(i)

j=1
while (j < 6):
    print(j)
    j=j+1
    
    j=51
while (j < 51):
    print(j)
    j=j+1
    
n=int(input("Enter a Number:"))
if n%2==0:
    print("It is an even number")
else:
    print("It is an odd number")
    
name1=input("Enter your name")
print(name1)
name2=input("Enter your name")
print(name2)
    
name1=input("Enter your name in a capital:")
name2=input("Enter your name:")
Bothnames=name1+name2
print(Bothnames)
small_letters=Bothnames.lower()
print(small_letters)

a=10
print(type(a))
s=str(a)
print(type(s))
k=float(s)
print(type(k))

list=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
k=set(list)
print(k)
k.add(12)
k.add(12)
print(k)
