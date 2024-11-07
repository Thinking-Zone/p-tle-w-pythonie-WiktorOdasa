def pytaj_o_pogode():
    liczba_nie = 0  # Zmienna do liczenia odpowiedzi "nie"

    print("Zgadnij, czy pada deszcz (odpowiedz 'tak', 'nie' lub 'nie wiem').")

    while True:
        odpowiedz = input("Czy pada? ").strip().lower()  # Odczytujemy odpowiedź, ignorując wielkość liter i białe znaki
        
        if odpowiedz == "tak":
            print(f"Zakończono. Liczba odpowiedzi 'nie' wynosi: {liczba_nie}")
            break  # Kończymy pętlę, jeśli użytkownik odpowiedział "tak"
        
        elif odpowiedz == "nie":
            liczba_nie += 1  # Zwiększamy licznik odpowiedzi "nie"
        
        elif odpowiedz == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz.")
        
        else:
            print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")

# Uruchomienie programu
pytaj_o_pogode()
