# Program szuka pierwszej liczby podzielnej przez 7 w zakresie od 1 do 100
for i in range(1, 101):
    if i % 7 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 7
        print(f"Pierwsza liczba podzielna przez 7 to: {i}")
        break  # Kończymy działanie programu po znalezieniu pierwszej liczby
