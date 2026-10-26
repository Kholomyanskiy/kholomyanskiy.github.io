---
slug: failure-point
title: "Punkt awarii przy wdrażaniu AI: czym jest i jak go znaleźć"
description: "Punkt awarii powstaje, gdy po automatyzacji nie ma kto przywrócić systemu ani wykonać pracy ręcznie. Gdzie go szukać i jak zmierzyć go z wyprzedzeniem."
published: 2026-10-26
updated: 2026-10-26
---

# Punkt awarii

Punkt awarii to element systemu, którego awaria zatrzymuje cały proces. Przy wdrażaniu AI takim punktem często staje się odcinek pracy, na którym nie została żadna rezerwa w ludziach: jeśli system zawiedzie, nie będzie komu go przywrócić ani wykonać pracy ręcznie. Droga do tego zwykle wygląda tak. AI zdejmuje z ludzi rutynę, ludzi się zwalnia, a razem z nimi znika umiejętność utrzymania, administrowania i pracy z pominięciem systemu.

## Skąd ten termin

Pochodzi z inżynierii i IT, gdzie częściej mówi się o pojedynczym punkcie awarii (single point of failure). Może nim być jeden serwer bez zapasu, jedno łącze, jeden specjalista, który wie, jak wszystko działa. Ludzi w tej roli również bierze się pod uwagę od dawna: w programowaniu istnieje „bus factor”, czyli liczba osób, po których odejściu projekt staje. Przy wdrażaniu AI punkt awarii najczęściej pojawia się tam, gdzie zabrakło ludzi zdolnych zastąpić automatyzację, kiedy ona nie działa.

Błędy samego modelu na pojedynczych krokach to sąsiedni temat. Wyłapuje się je przez sprawdzanie wyniku: dzięki [człowiekowi w pętli](slownik/human-in-the-loop.html) i [kryteriom odbioru](slownik/acceptance-criteria.html). Punkt awarii odpowiada na inne pytanie: co się stanie, gdy automatyzacja w ogóle przestanie działać.

## Dlaczego się pojawia

Ludzie na automatyzowanym odcinku zwykle pełnią funkcję, której nie ma w opisie stanowiska: wiedzą, jak pracować, kiedy system stoi. Automatyzacja działa, dopóki działają model, usługa, integracja i opłacona subskrypcja. Awaria któregokolwiek z tych ogniw oddaje pracę z powrotem ludziom. Jeśli ich już nie ma, praca czeka, aż ktoś zostanie znaleziony i przeszkolony.

Decyzję o redukcji etatów podejmuje się wtedy na podstawie zaoszczędzonych godzin. Godziny potrzebne na przywrócenie działania zwykle nie trafiają do rachunku, bo awarii jeszcze nie było.

## Gdzie go szukać

Najwygodniej na [mapie procesów](slownik/process-map.html). Podejrzane są odcinki, na których z powodu automatyzacji planuje się redukcję etatów. Funkcje, które zna jedna osoba. Utrzymanie, administrowanie i wsparcie systemów. Kroki bez ścieżki ręcznej. A także zależności zewnętrzne: usługa modelu, integracje, cennik dostawcy.

## Jak go zmierzyć

Dla każdego odcinka liczy się cztery wielkości:

- **dopuszczalny przestój:** jak długo odcinek może nie działać bez poważnej szkody: godzinę, dzień, tydzień;
- **czas przywrócenia:** ile potrwa przywrócenie pracy po awarii z ludźmi, którzy zostaną;
- **rezerwa:** ile osób potrafi przywrócić system albo wykonać pracę ręcznie;
- **koszt przestoju:** ile kosztuje godzina lub dzień postoju.

Jeśli czas przywrócenia jest dłuższy niż dopuszczalny przestój, odcinek jest punktem awarii. Następnie wybiera się, co z nim zrobić: zostawić ludzi, przeszkolić tych, którzy zostają, podpisać umowę serwisową, zachować ścieżkę ręczną. O składzie działu warto decydować po takim rachunku, podczas [audytu procesów](slownik/process-audit.html). Wybrany wariant wraz ze ścieżką ręczną i procedurą na wypadek awarii zapisuje się w [specyfikacji](spec.html) rozwiązania.

## Z praktyki

Przez ponad dziesięć lat pracowałem w IT w energetyce. Obowiązuje tam zasada N-1: system musi wytrzymać awarię dowolnego pojedynczego elementu. Sprawdza się ją z wyprzedzeniem, na schemacie, przed jakąkolwiek awarią. Kiedy w proces wbudowuje się AI, zadaję to samo pytanie: co się stanie, jeśli ten element zawiedzie, i kto wtedy przejmie pracę.

Gdy nikt tego pytania nie zadaje, zwykle wygląda to tak. Firma uznaje, że raporty pisze teraz AI, i zwalnia część administratorów systemów. Raporty powstają. Po kilku miesiącach pada sieć i nie ma kto jej podnieść. Model się nie pomylił. Zawiódł odcinek, na którym nie została żadna rezerwa.

## Co ustalić z wyprzedzeniem

Kto przywraca system, jeśli padnie w nocy albo w weekend. Czy istnieje ścieżka ręczna i kto spośród pozostałych osób umie z niej korzystać. Co zrobić, jeśli dostawca modelu zmieni warunki albo usługa będzie niedostępna przez kilka dni. I kogo zwalniać: to pytanie rozstrzyga się po policzeniu punktów awarii.

---

**Powiązane terminy:** [Audyt procesów](slownik/process-audit.html) · [Mapa procesów](slownik/process-map.html) · [Człowiek w pętli](slownik/human-in-the-loop.html) · [Całkowity koszt posiadania](slownik/total-cost-of-ownership.html)

Planujesz przebudować dział pod AI? [Audyt AI w dziale →](audit.html)
