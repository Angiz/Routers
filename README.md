# Routers
# PL

Biblioteki/narzędzia niezbędne do uruchomienia programu:
- środowisko Python 3.x
- pip
- biblioteka NumPy
- biblioteka csv do eksportu pliku

Zasada działania programu:
Program pobiera od użytkownika liczbę routerów oraz liczbę stacji. Jeśli użytkownik poda nieprawidłowe parametry, program wyrzuca błąd. 
Następnie w pętli dodajemy stację, routery i odpowiednie im przepustowości. Jeśli przypustowość jest ujemna, program dodaje dużą liczbę, 
żeby nie był brany pod uwagę przy wyszukiwaniu najkrótszej ścieżki. Jeśli użytkownik poda liczbę ujemną, program wyrzuca błąd wartości
i następuje zakończenie programu. Następnie przypisujemy przepustowości do stacji na zasadzie prawdopodobieństwa (dla każdej stacji i 
dla każdego routera). Parametry dla tablicy stations działają analogicznie jak dla routers. Następnie jest liczona umowna waga
podana jako wektor, łącząca przepustowość, czas połączenia z routerem oraz odległość stanowiska od routera. Następnie wektor jest 
eksportowany do macierzy (matrix), która jest potem badana przez algorytm Dijkstry. Jest również tworzona analogiczna macierz z pomocą
biblioteki NumPy, która jest potem eksportowana do pliku tekstowego. W macierzach znajdują się wartości wag przypisane na zasadzie 1-sza
wartość to waga 1-szego routera do 1-szej stacji, 2-ga wartość to waga 1-szego routera do 2-giej stacji itd. Po przeanalizowaniu macierzy
przez algorytm Dijkstry, macierz jest eksportowana do pliku txt w formacie %<wartości z tablicy stations> i poniżej macierz. Dane te można
zanalizować przez program Neural Applet. 
