'''print("Hello World!")
a,b,c,d = 10,5.5,True,1+2j
print(type(a), type(b), type(c), type(d))'''

numbers = [12,13,14,15,16,17]
odd = []
even = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        odd.append(number)
    else:
        even.append(number)
print(odd)
print(even)

