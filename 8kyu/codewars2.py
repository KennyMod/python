#Even or Odd

#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

#solution

#number, integer,positive
#return even or odd if number gives a remainder of 0

#even_or_odd(2), "Even")
#even_or_odd(1), "Odd")
#even_or_odd(0), "Even")
#even_or_odd(1545452), "Even")
#even_or_odd(7), "Odd")
#even_or_odd(78), "Even")
#even_or_odd(17), "Odd")
#even_or_odd(74156741), "Odd")
#even_or_odd(100000), "Even")
#even_or_odd(-123), "Odd")
#even_or_odd(-456), "Even")

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2)) # "Even")
print(even_or_odd(1)) # "Odd")
print(even_or_odd(0)) # "Even")
print(even_or_odd(1545452)) # "Even")
print(even_or_odd(7)) # "Odd")
print(even_or_odd(78)) # "Even")
print(even_or_odd(17)) # "Odd")
print(even_or_odd(74156741)) # "Odd")
print(even_or_odd(100000)) # "Even")
print(even_or_odd(-123)) # "Odd")
print(even_or_odd(-456)) # "Even")