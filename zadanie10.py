# Zadanie:
# Napisz program, który wypisze sumę wszystkich liczb, które są podzielne przez 3 lub 5 w zakresie od 1 do 100.
# Program powinien wykorzystać pętlę, aby przejść przez liczby w tym zakresie, a potem dodać je do zmiennej sumy.
# Na końcu program wypisze wynik.

print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

# Rozwiązanie:

suma = 0  # Zmienna do przechowywania sumy

# Przechodzimy przez liczby od 1 do 100
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 3 lub 5
        suma += i  # Dodajemy liczbę do sumy

# Wypisujemy wynik
print(f"Suma liczb podzielnych przez 3 lub 5 w zakresie od 1 do 100 wynosi: {suma}")
