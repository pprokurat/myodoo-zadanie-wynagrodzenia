# Wynagrodzenia

Aplikacja służy do obliczania wynagrodzeń netto na podstawie podanych kwot brutto z użyciem zewnętrznego serwisu wynagrodzenia.pl.
Kwoty netto obliczane są według domyślnych ustawień kalkulatora dla umowy o pracę.
Aplikacja mogłaby potencjalnie zostać rozszerzona o funkcję podawania niestandardowych parametrów obliczeń, na przykład wyboru innego typu umowy.

## Użycie aplikacji

W celu wykonania obliczeń należy uruchomić aplikację, podając wejściowe kwoty brutto jako jej argumenty, na przykład:

```cmd
python wynagrodzenia.py 2250 2500 2800 3000 3500 4000
```

## Wymogi aplikacji

Aplikacja wymaga zainstalowania za pomocą narzędzia `pip` następujących pakietów:

* `numpy`
* `matplotlib`
* `mechanize`
* `beautifulsoup4`

Aplikację wykonano z użyciem Python w wersji 3.8.0.