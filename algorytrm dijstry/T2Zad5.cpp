/*Zadanie 5 (Algorytm Dijkstry) (patrz [CLR], [SDK], [LW])
Zaimplementuj algorytm Dijkstry wyznaczania najkrótszych ścieżek z ustalonego źródła w ważonym grafie
skierowanym. Za strukturę danych do reprezentacji grafu przyjmij macierz wag krawędzi.
Dane:
¨ Graf G=<E,V> skończony, spójny, skierowany, z wagami nieujemnymi; s - wierzchołek początkowy (źródło)
¨ Pierwsza linia zawiera dwie liczby n, mÎN+ (oddzielone spacją). n oznacza ilość wierzchołków, m – źródło s.
¨ W następnych n liniach zapisana jest macierz wag krawędzi grafu.
¨ ¥ oznacza liczbę dużo większą od największej wagi w grafie
Wyjście:
¨ dist[n] - tablica zawierająca długości najkrótszych dróg od źródła s do pozostałych wierzchołków grafu
¨ pred[n] - tablica poprzedników (na najkrótszych drogach), służąca do uzyskania kolejnych wierzchołków drogi
z s do i (iÎV-{s})
¨ W pierwszej linii pliku Out0306.txt umieść wartości tablicy dist, w drugiej - tablicy pred.*/

#include <cstdlib>
#include <fstream>

using namespace std;

int main() {
	ifstream wejscie("In0205_2.txt");
	ofstream wyjscie("Out0205.txt");
	int ileWezlow, startowy;
	int i, j;
	char slowo[20];
	wejscie >> ileWezlow >> startowy;
	int **macierz = new int*[ileWezlow + 1];
	for (i = 1; i <= ileWezlow; i++) {
		macierz[i] = new int[ileWezlow + 1];
		for (j = 1; j <= ileWezlow; j++) {
			wejscie >> slowo;
			macierz[i][j] = (slowo[0] >= '0' && slowo[0] <= '9') ? atoi(slowo) : -1;
		}
	}
	int *dist = new int[ileWezlow + 1];
	int *pred = new int[ileWezlow + 1];
	int *kolejka = new int[ileWezlow];

	for (i = 1; i <= ileWezlow; i++) {
		dist[i] = -1;
		kolejka[i - 1] = i;
	}
	dist[startowy] = 0;
	pred[startowy] = -1;

	for (i = 0; i < ileWezlow; i++) {
		int minIndeks = i;
		for (j = i + 1; j < ileWezlow; j++)
			if (dist[kolejka[j]] != -1 && (dist[kolejka[minIndeks]] == -1 || dist[kolejka[minIndeks]] > dist[kolejka[j]]))
				minIndeks = j;
		int minWezel = kolejka[minIndeks];
		kolejka[minIndeks] = kolejka[i];
		for (j = 1; j <= ileWezlow; j++)
			if (macierz[minWezel][j] != -1 && (dist[j] == -1 || dist[j] > dist[minWezel] + macierz[minWezel][j])) {
                dist[j] = dist[minWezel] + macierz[minWezel][j];
                pred[j] = minWezel;
			}
	}

	wyjscie << "dist[" << dist[1];
	for (int i = 2; i <= ileWezlow; i++)
		wyjscie << " "<< dist[i];
	wyjscie << "]\n";

	wyjscie << "pred[" << pred[1];
	for (int i = 2; i <= ileWezlow; i++)
		wyjscie << " "<< pred[i];
	wyjscie << "]\n";

	for (i = 1; i <= ileWezlow; i++)
		delete []macierz[i];
	delete []macierz;
	delete []dist;
	delete []pred;
	delete []kolejka;

	return 0;
}
