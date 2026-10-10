---
slug: ai-specification
title: "Specyfikacja AI: czym jest i czym różni się od promptu"
description: "Specyfikacja AI opisuje zadanie tak, aby model wykonywał je przewidywalnie, a wynik można było sprawdzić. Co zawiera i dlaczego jest potrzebna."
---

# Specyfikacja AI

Specyfikacja AI to dokument opisujący zadanie tak, aby model lub agent wykonywał je przewidywalnie, a wynik dało się sprawdzić: co jest na wejściu i wyjściu, jakich zasad nie wolno łamać i po czym poznać, że praca jest gotowa. Istnieje poza czatem i pozostaje dostępna w kolejnych sesjach.

## Czym specyfikacja różni się od promptu

[Prompt](slownik/prompt.html) to instrukcja lub prośba w rozmowie. Zwykle dotyczy konkretnego zadania i pozostaje częścią tej sesji. Model czyta specyfikację na początku każdej sesji; aktualizuje się ją, gdy zmieniają się zasady, a później używa do sprawdzenia pracy. Dobry prompt pomaga uzyskać jedną dobrą odpowiedź. Specyfikacja sprawia, że przewidywalna staje się cała praca.

U programistów tę dyscyplinę zapewnia środowisko inżynierskie: zadania w systemie śledzenia, przeglądy kodu i testy. Menedżer lub mała firma bez działu inżynieryjnego nie ma takiego środowiska, więc jego rolę przejmuje strona ze specyfikacją.

## Co zawiera

- Cel i wynik: co ma powstać i w jakiej formie.
- Dane wejściowe: jakie dane, skąd pochodzą i w jakim są stanie.
- Ograniczenia: czego nie wolno zmieniać ani zepsuć. W specyfikacjach nazywa się je [niezmiennikami](slownik/invariant.html).
- [Kryteria odbioru](slownik/acceptance-criteria.html): jak sprawdzić, czy praca jest wykonana.
- Podjęte już decyzje, aby model nie rozpatrywał ich ponownie w każdej sesji.

W przypadku jednego zadania często wystarczy na to jedna strona.

## Kiedy zwykły opis zadania nie wystarcza

Zadanie dla modelu formułuje się zwykle tak, jakby był kolegą, który wszystko wie. Model wie mniej niż kolega i nie dopytuje, tylko dopowiada brakujące szczegóły. Wynik wygląda wiarygodnie, ale rozwiązuje inne zadanie. Potem poprawki krążą w kółko: naprawiasz jedną rzecz, psuje się następna. W internecie jest tyle żartobliwych filmów na ten temat, że powstał z nich osobny gatunek. Śmieszne, bo prawdziwe.

Drugi powód wynika z budowy samych modeli. Mają ograniczone [okno kontekstowe](slownik/context-window.html): im więcej dokumentów, wiadomości i nowych instrukcji w sesji, tym trudniej modelowi zachować wcześniejsze ustalenia. Opis zadania w rozmowie zwykle pozostaje w konkretnym czacie. Specyfikacja jest osobnym dokumentem i można ponownie przekazać ją modelowi.

## Z praktyki

Zanim zacząłem pisać specyfikacje, zlecałem zadania modelom tak jak wszyscy: w rozmowie, na bieżąco. Mniej więcej między piątą a dziesiątą odpowiedzią zaczynał się chaos. Model zapominał o podjętych decyzjach, zmieniał rzeczy, których nie wolno było ruszać, i gubił się w długich dokumentach. Tak było niemal w każdym projekcie i z każdym agentem.

Z tego doświadczenia powstał [ANSS](anss.html), otwarty standard specyfikacji do pracy z AI. W moich projektach po jego wdrożeniu jakość wyników wyraźnie wzrosła. Nie jest idealny, tak jak same modele nie są idealne, ale to podejście się sprawdza i korzystam z niego w pracy.

Ten słownik również powstaje w ten sposób. Gdy w czacie zbierze się zbyt wiele wersji, zapisujemy wszystkie decyzje w jednym pliku i od niego zaczynamy nową sesję.

## Co ustalić przed rozpoczęciem prac

Kto pisze specyfikację: klient, wykonawca czy obie strony, i kto ją zatwierdza. Gdzie będzie przechowywana i kto będzie ją aktualizować, gdy zmienią się zasady. Jak szczegółowa ma być: przy jednym zadaniu wystarczy jedna strona, a przy łańcuchu agentów przekazujących sobie pracę potrzebny jest standard taki jak ANSS.

---

**Powiązane terminy:** [Kryteria odbioru](slownik/acceptance-criteria.html) · [Niezmiennik](slownik/invariant.html) · [Prompt](slownik/prompt.html) · [Okno kontekstowe](slownik/context-window.html)

Trzeba opisać na jednej stronie zadanie dla AI lub wykonawcy? [Specyfikacja →](spec.html)
