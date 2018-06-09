# Routers
# PL
# Projekt wykonany na zaliczenie przedmiotu Sztuczna Inteligencja

Biblioteki/narzędzia niezbędne do uruchomienia programu:
- środowisko Python 3.x
- pip
- biblioteka NumPy
- biblioteka csv do eksportu pliku

Instrukcja instalacji bibliotek:
Środowisko Pythona można pobrać z następującej strony: https://www.python.org/downloads/. 
Najwygodniejszą wersją do odtwarzania programu jest instalacja programu PyCharm: https://www.jetbrains.com/pycharm/download/#section=windows. Wersja Community jest darmowa.Otwieramy plik RoutersConnection.py. Po wejściu w ustawienia (Settings), wybieramy opcję Project:<nazwa projektu> -> Project Interpreter. Wyświetla nam się lista z zainstalowanymi bibliotekami. W celu dodania powyższych bibliotek, klikamy znaczek "+" i wyszukujemy instalujące nas biblioteki. Istnieje również instalacja przez konsolę, jednak jest ona bardziej skomplikowana, dlatego zaleca się 1-szą opcję. Projekt uruchamiamy poprzez przycisk "Run".

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
