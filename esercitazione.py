x1 = 9 #numero inero
z = 12.4 #float
y = 3
print(type(x1))
print(type(y))
print(type(z))

x2 = "Francesco" #stringa
c = True #bool o False
print(type(x2))
print(type(c))

x3 = [1,2,3] #list
y1 = (3,4,5) #tuple
v = range(10) 
k = {5,9,6} #set
p = {"Nome" : "Francesco", "Cognome" :" Tedesco"} #dict un valore accompagnato da una parola chiave
print(type(x3))
print(type(y1))
print(type(v))
print(type(k))
print(type(p))

aa = "5"
bb = 5
print(int(aa)+ bb) #casting far diventare un numero una stringa e viceversa

r = "Ciao sono Luca"
print(r.upper())
print(r.find("Luca"))
print(r.replace("Luca", "Francesco"))

a = 10
b = 25
a += 30
print(a) #operatori di asseganment

A = 30
B = 20
print(A + B)
print(A * B)
print(A / B)
print(A % B)
print(A ** B) #esponenziale
print(A // B) #divisione sena resto

import math 
D = 256
F = -16
L = [1,2,5,9,10,7]
print(math.sqrt(D))
print(abs(F))
print(min(L))
print(max(L))

x4 = 10
if x4 == 5:
  print("x è 5")
elif x4 == 6:
  print("x è 6")
else:
  print("x è sicuramente un altro numero")

x5 = 2
if x5 % 2 == 0:
  print("é un numero pari")
  if x5 > 3:
    print("è maggiore di 3")
  else:
    print("non è maggiore di 3")
else:
  print("è un numero dispari")


i = 1
while i < 6:
  print(i)
  i +=1


i = 0
while i < 6:
    i += 1
    if i == 3:
      continue
    print(i)
  

i = 1
while i < 6:
  if i == 3:
    break
  print(i)
  i += 1


prodotti = ["pane ", "nutella ", "biscotti "]
aggettivi = ["caro", "economico", "normale"]


for prodotto in prodotti:
    for aggettivo in aggettivi:

      print(prodotto + aggettivo)


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



q = input("Come ti chiami") 
print("Ciao" + q)