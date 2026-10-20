choise1 = input(" What do you want to change. Binary, Octal, Decimal, Hexadecimal are the options choose wisely or something... " )


liczba = int(input("Input a number to change:"))



Liczba_bin = f"{liczba:b}"
Liczba_oct = f"{liczba:o}"
Liczba_hex = f"{liczba:x}"
Liczba_dec = f"{liczba:d}"
print(f" Binary: {Liczba_bin} ")
print(f" Octal: {Liczba_oct}")
print(f" Decimal: {Liczba_dec}")
print(f" Hexadecimal: {Liczba_hex}")