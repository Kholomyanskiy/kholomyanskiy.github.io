---
slug: process-audit
title: "Audyt procesów przed wdrożeniem AI: czym jest i po co go robić"
description: "Audyt procesów pokazuje, jak naprawdę przebiega praca przed zakupem narzędzia AI. Co obejmuje, jaki daje wynik i dlaczego jest potrzebny."
---

# Audyt procesów

Audyt procesów przed wdrożeniem AI to analiza tego, jak naprawdę przebiega praca w firmie: jakie zadania wykonują ludzie, ile czasu im to zajmuje, z jakich danych i narzędzi korzystają oraz gdzie pojawiają się opóźnienia i błędy. Wynik pokazuje, które kroki warto zautomatyzować, gdzie AI tylko doda pracy i gdzie nie można obejść się bez człowieka.

## Co obejmuje audyt

Pierwsze pytanie audytu brzmi: jak praca przebiega teraz i jaki problem warto rozwiązać? Pytanie o to, jakie narzędzie kupić, pojawia się na końcu. Przyglądamy się prawdziwemu tygodniowi pracy, bo opis stanowiska przedstawia go mniej więcej tak, jak menu opisuje kuchnię. Z audytem wewnętrznym i kontrolą ISO łączy go tylko słowo „audyt”: tutaj nikogo się nie ocenia.

Analizuje się:

- jakie zadania są wykonywane i kto je wykonuje;
- ile czasu zajmuje każde z nich;
- jakie dane, dokumenty i narzędzia są używane, także te już opłacone;
- gdzie występują praca ręczna, opóźnienia i błędy;
- które kroki można powierzyć AI i gdzie stworzy to dodatkową pracę;
- gdzie potrzebny jest człowiek i co się bez niego zatrzyma.

## Co powstaje w wyniku audytu

[Mapa procesów](slownik/process-map.html) z zaznaczonymi problemami. Możliwości automatyzacji wraz z szacowanym efektem każdej z nich. Ograniczenia i ryzyka: gdzie AI może się pomylić, kto to zauważy i [czyja praca zatrzyma się bez człowieka](slownik/failure-point.html). Lista pomysłów bez oszacowania efektów nie jest wynikiem audytu.

Audyt pokazuje obecną sytuację, a decyzję o wdrożeniu podejmuje się później. Wybrane zadanie opisuje się w [specyfikacji AI](slownik/ai-specification.html) i sprawdza w [pilotażu](slownik/pilot.html), zanim rozwiązanie trafi do całego działu.

## Dlaczego przed wdrożeniem

Audyt warto przeprowadzić przed zakupem narzędzia i przed podjęciem decyzji dotyczących ludzi. Po wdrożeniu staje się sekcją zwłok: wyjaśnia, co poszło nie tak, gdy pieniądze są już wydane. Przed wdrożeniem odpowiada na pytania wpływające na budżet. Gdzie AI zdejmie z ludzi rutynowe zadania? Co potrafią już narzędzia, za które płacisz? Komu pomoże?

## Z praktyki

Mój kolega ze studiów pisze kod od ponad dziesięciu lat, a teraz prowadzi zespół. Pewnego dnia firma wykupiła wszystkim dostęp do asystenta AI i ogłosiła, że nikt nie będzie już programował ręcznie. Nie przekazano instrukcji ani nie mierzono przyspieszenia pracy. U niego się udało, bo miał duże doświadczenie, a zadania były niewielkie. Nie wiadomo, jak poradzili sobie mniej doświadczeni pracownicy. Nikt nie pomyślał, żeby zapytać.

Sam popełniłem podobny błąd jako wykonawca. Znajomy dostawał 100–200 wiadomości dziennie i poświęcał około dwóch godzin na ich sortowanie. Zbudowaliśmy automatyczne sortowanie w Zapierze. W trakcie pracy Google dodał do Gmaila przycisk Gemini, który porządkuje pocztę według etykiet w ramach planu, za który znajomy i tak już płacił. Moja automatyzacja dodawała niewiele poza przypomnieniami o ważnych wiadomościach. Nikt nie policzył zaoszczędzonych godzin.

W obu historiach pominięto jeden krok. Nikt nie sprawdził, jak zorganizowana jest praca, zanim ją zmieniono.

## Co ustalić przed audytem

Co analizujemy: cały dział czy jeden łańcuch zadań. Kto otrzyma wynik i będzie podejmował decyzje. I jak wyjaśnić ludziom, dlaczego ich pytamy. To ostatnie jest ważniejsze, niż się wydaje: jeśli pracownicy uznają, że to kontrola przed zwolnieniami, powtórzą opis stanowiska.

---

**Powiązane terminy:** [Mapa procesów](slownik/process-map.html) · [Pilotaż](slownik/pilot.html) · [Punkt awarii](slownik/failure-point.html) · [Całkowity koszt posiadania](slownik/total-cost-of-ownership.html)

Planujesz wdrożyć AI w dziale? [Audyt AI w dziale →](audit.html)
