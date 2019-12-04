def fizz_buzz(num):
    # If remainder of number after being divided by 3 and 5 is 0 then return Bizzuu
    if num%3 == 0 and num%5 == 0:
        return 'Bizzuu'
    # If remainder of number after being divided by 3 then return Bizz
    if num%3 == 0:
        return 'Bizz'
    # If remainder of number after being divided by 5 then return Fizz
    if num%5 == 0:
        return 'Fizz'
    else:
        return 'Loser'