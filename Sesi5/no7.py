a = 1 
b = 1
c = b 
r = 9

for i in range(r):
    a = b 
    b = c 
    c = a + b
    print(a, end=" ")
