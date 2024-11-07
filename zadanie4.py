suma = 0  # Zmienna do przechowywania sumy

for i in range(1, 101):  # Przechodzimy przez liczby od 1 do 100
    if i % 2 != 0:  # Sprawdzamy, czy liczba jest nieparzysta (reszta z dzielenia przez 2 różna od 0)
        suma += i  # Dodajemy liczbę do sumy

print(f"Suma liczb nieparzystych od 1 do 100 wynosi: {suma}")
