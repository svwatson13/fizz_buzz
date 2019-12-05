# Write a bizz and fizz game ##project


# In loop
while True:
    num = int(input('Whats your number? '))
    if num == 0:
        break
    if num % 3 == 0 and num % 5 == 0:
        print('Bizzizz')
        # If remainder of number after being divided by 3 then return Bizz
    elif num % 3 == 0:
        print('Bizz')
    elif num % 5 == 0:
        print('Fizz')
    else:
        print(num)


# print user input number and the function output
print(num, (fizz_buzz(num)))





