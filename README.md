# qgis-smartsdi
Wtyczka **SmartSDI** - plugin dla programu QGIS

### Pobieranie danych
Wtyczka umożliwia pobranie danych dla aktualnego widoku lub w ramach przecięcia z inną warstwą wektorową.

Dane do pobrania:
- działki ewidencyjne (EGiB[^1])
- budynki ewidencyjne (EGiB)
- adresy (PRG[^2])
[^1]:Dane EGiB (Ewidencja Gruntów i Budynków) pochodzą z usług sieciowych publikowanych przez powiaty. Aktualizacja danych odbywa się min. 2 razy w tygodniu.
[^2]:Dane PRG (Państwowy Rejestr Granic) z GUGiK. Aktualizacja odbywa się codziennie.

### Wyszukiwanie działek
Możliwe jest znalezienie konkretnej działki poprzez wybranie województwa, powiatu i gminy (+ ew. obrębu) oraz wpisanie numeru działki.
Istnieje również możliwość znalezienia listy działek spełniających następujące kryteria:
- powierzchnia działki (minimalna, maksymalna)
- kształt działki (regularny/nieregularny)
- występowanie zabudowy na działce
- powierzchnia zabudowy na działce (minimalna, maksymalna)
- minimalna odległość działki od budynków
- typ własności[^3] (grupa rejestrowa np. Skarb Państwa, osoba fizyczna)
- klasoużytek[^3] (np. las, teren mieszkaniowy, grunt rolny)
[^3]:Dostępne dla wybranych powiatów

## Dodatkowe informacje:
- strona domowa: [smartsdi.pl/qgis](https://smartsdi.pl/qgis/)
- repozytorium wtyczek QGIS: [qgis-smartsdi](https://plugins.qgis.org/plugins/qgis-smartsdi/)
