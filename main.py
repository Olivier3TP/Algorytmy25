def nwd_1(liczba_a, liczba_b):
    while liczba_a != liczba_b:
        if liczba_a < liczba_b:
            liczba_b = liczba_b - liczba_a
        else:
            liczba_a = liczba_a - liczba_b
    return liczba_a

print(nwd_1(18, 24)) # nwd(18,24) = 6

def nwd_2(liczba_a, liczba_b):
    while liczba_b != 0:
        dzielnik = liczba_b
        liczba_b = liczba_a % liczba_b
        liczba_a = dzielnik
    return liczba_a

print(nwd_2(36,126)) # nwd(26,126) = 18

# liczba pierwsa