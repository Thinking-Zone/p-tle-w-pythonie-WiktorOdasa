import random

# Funkcja do losowania pogody (True = pada, False = nie pada)
def losuj_pogode():
    return random.choice([True, False])  # Wybiera losowo True (pada) lub False (nie pada)

# Program główny
def pytaj_o_pogode():
    print("Zgadnij, czy pada deszcz (odpowiedz 'tak' lub 'nie').")

    # Losowanie pogody
    czy_pada = losuj_pogode()

    # Pętla, dopóki użytkownik nie zgadnie
    while True:
        odpowiedz = input("Czy pada? ").strip().lower()  # Odczytujemy odpowiedź, ignorując wielkość liter i białe znaki

        # Sprawdzanie odpowiedzi
        if (odpowiedz == "tak" and czy_pada) or (odpowiedz == "nie" and not czy_pada):
            print("Brawo! Zgadłeś!")
            break  # Kończymy pętlę, jeśli odpowiedź jest poprawna
        else:
            print("Nie zgadłeś. Spróbuj ponownie!")

# Uruchomienie programu
pytaj_o_pogode()
