---
slug: invariant
title: "Niezmiennik w specyfikacji: zasada, której nie wolno łamać"
description: "Niezmiennik w specyfikacji to zasada, której system przestrzega zawsze. Jak go zapisać, jak sprawdzić i dlaczego dla agenta AI jest najważniejszy."
published: 2026-11-08
updated: 2026-11-08
---

# Niezmiennik w specyfikacji

Niezmiennik (inwariant) w specyfikacji to zasada, która musi obowiązywać zawsze: przy każdym zadaniu, każdej zmianie i niezależnie od tego, kto wykonuje pracę. Operacji w ewidencji się nie usuwa. Saldo nie zmienia się poza transakcją. Pola w odpowiedzi API, z którego korzystają już klienci, nie zmienia się nazwy. Wymagania opisują, co zbudować, a niezmienniki to, czego przy budowie nie wolno zepsuć.

## Skąd ten termin

Słowo pochodzi z matematyki i programowania. Niezmiennikiem nazywa się tam właściwość, która pozostaje taka sama bez względu na to, co dzieje się z systemem: suma kątów trójkąta, warunek prawdziwy na każdym kroku pętli. W specyfikacji znaczenie jest to samo, tylko odnosi się do zachowania systemu i do pracy tych, którzy go zmieniają.

## Czym niezmiennik różni się od wymagania i zasady

Wymaganie można spełnić częściowo, odłożyć albo zrewidować. Zasada architektoniczna pomaga wybrać rozwiązanie, gdy wymagań brakuje, i czasem ustępuje innej zasadzie. Niezmiennik nie ustępuje niczemu. Jeśli zadanie wymaga jego złamania, praca się zatrzymuje, a decyzję podejmuje człowiek.

Dlatego niezmienników w projekcie jest mało, zwykle od trzech do dziesięciu. Gdy niezmiennikiem ogłasza się wszystko, przestają się różnić od życzeń, a wykonawca zaczyna wybierać, których przestrzegać.

## Jak się go zapisuje

W standardzie [ANSS](anss.html) niezmiennik ma cztery pola: nazwę, czego nie wolno, dlaczego i jak to sprawdzić. Na przykład dla aplikacji, która ma działać bez instalowania pakietów: nie wolno dodawać zewnętrznych modułów npm, bo aplikacja musi działać bez npm install, a sprawdzenie polega na tym, że w kodzie nie ma importów z node_modules.

Najważniejsze jest ostatnie pole. Sprawdzenie musi być konkretne: zapytanie do bazy, ograniczenie w schemacie danych, test, wiersz w diffie. Niezmiennik bez sprawdzenia pozostaje dobrą intencją, której przestrzegania nikt nie potrafi potwierdzić.

## Dlaczego przy AI to ważniejsze

Człowiek w zespole latami słyszy, czego w tym systemie nie wolno ruszać. [Agent AI](slownik/agent.html) tego nie wie. Czego brakuje w zadaniu, uzupełnia decyzjami z danych treningowych, a pod presją zadania potrafi „naprawić” błąd, usuwając kontrolę, która mu przeszkadzała.

Zapisany niezmiennik daje agentowi granicę widoczną przed rozpoczęciem pracy i regułę na wypadek konfliktu: zatrzymać się i zapytać. Pole sprawdzenia pozwala agentowi porównać z nim własny wynik, a człowiekowi przy odbiorze upewnić się, że granica jest nienaruszona. Dlatego w [specyfikacji AI](slownik/ai-specification.html) niezmienniki stoją w sekcji, którą agent czyta jako pierwszą.

## Z praktyki

W specyfikacji dla sieci lombardów najważniejsze niezmienniki wyszły z rozmowy z właścicielem firmy. Przyjęcia przedmiotu nie da się zarejestrować bez zdjęcia. O tym, dokąd trafia przedmiot po przyjęciu, decyduje wyłącznie właściciel. Skup po cenie za gram spoza ustalonego przedziału wymaga jego zatwierdzenia. Każda z tych zasad zamyka konkretny sposób nadużycia ze strony pracownika i każda ma sprawdzenie w kodzie: serwer odrzuca żądanie bez zdjęcia, a trasy przedmiotu nie da się zmienić bez potwierdzenia właściciela. Specyfikacja jest opublikowana jako przykład w repozytorium ANSS.

W każdym zleceniu technicznym dla tej strony jest sekcja niezmienników: teksty publikuje się dosłownie, plików spoza listy się nie zmienia, nowych stylów nie ma. Ich sprawdzenie jest wspólne i proste: lista zmienionych plików przed commitem. Jeśli pojawi się na niej plik spoza listy, praca staje do czasu odpowiedzi.

## Co ustalić z wyprzedzeniem

Których zasad w procesie nie wolno łamać nigdy, nawet dla pilnego zadania. Jak każdą z nich się sprawdza i kto to robi: kod, test czy człowiek przy odbiorze. Co robi wykonawca, gdy zadanie trafia na niezmiennik. I kto może niezmiennik zmienić: to decyzja człowieka, nie podejmuje jej ani agent, ani wykonawca w trakcie pracy. Sprawdzenia niezmienników wchodzą do [kryteriów odbioru](slownik/acceptance-criteria.html).

---

**Powiązane terminy:** [Specyfikacja AI](slownik/ai-specification.html) · [Kryteria odbioru](slownik/acceptance-criteria.html) · [Agent AI](slownik/agent.html) · [Punkt awarii](slownik/failure-point.html)

Trzeba zapisać zasady, których AI i wykonawca nie mogą łamać? [Specyfikacja AI →](spec.html)
