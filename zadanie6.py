# Pętla `for`:
# Pętla `for` jest zwykle używana, gdy z góry znamy liczbę iteracji, np. iterowanie po elementach listy, ciągu czy w zakresie liczb.
# Dzięki konstrukcji `range()` pętla `for` świetnie nadaje się do wykonywania operacji określoną liczbę razy.
# Pętla ta jest bardziej "sztywna" i pozwala na bezpośrednie określenie warunków iteracji.
# Przykład:
# for i in range(5):
#     print(i)
# Wynik: 0 1 2 3 4

# Pętla `while`:
# Pętla `while` jest używana, gdy nie znamy dokładnej liczby iteracji z góry, ale mamy warunek, który musi być spełniony.
# Pętla ta działa dopóki warunek pozostaje prawdziwy. Jest bardziej "elastyczna", ale wymaga ostrożności, by nie stworzyć pętli nieskończonej.
# W przypadku tej pętli warunek jest sprawdzany przed każdą iteracją.
# Przykład:
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# Wynik: 0 1 2 3 4
