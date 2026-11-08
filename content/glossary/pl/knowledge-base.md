---
slug: knowledge-base
title: "Baza wiedzy dla AI: jak ją zbudować, żeby AI nie zmyślało"
description: "Baza wiedzy dla AI to sprawdzony zbiór zasad, instrukcji i odpowiedzi firmy, na którym opiera się model. Czym różni się od folderu z plikami i kto ją prowadzi."
published: 2026-11-08
updated: 2026-11-08
---

# Baza wiedzy dla AI

Baza wiedzy to zebrany i sprawdzony zbiór tego, co firma wie o swojej pracy: procedury, instrukcje, odpowiedzi na częste pytania, opisy produktów, warunki dla klientów. Dla AI baza wiedzy jest źródłem, z którego model odpowiada zamiast z ogólnej wiedzy z treningu. To, co jest w bazie, model może znaleźć i zacytować. Czego w niej nie ma, tego dla modelu nie ma, a lukę wypełni wiarygodnie brzmiącym domysłem.

## Czym baza wiedzy różni się od folderu z plikami

Folder z dokumentami na wspólnym dysku sam w sobie nie jest bazą wiedzy. Aktualne wersje leżą w nim obok starych, szkice obok podpisanych dokumentów, i tylko pracownik z dużym stażem wie, któremu plikowi wierzyć. Model tego nie wie.

Baza wiedzy różni się trzema rzeczami. Są w niej tylko aktualne wersje, a stare usunięto albo wyraźnie oznaczono. Każdy dokument ma datę i zakres: dla jakiego działu, kraju, produktu obowiązuje. I baza ma właściciela, który odpowiada za to, żeby jej treść zgadzała się z tym, jak firma pracuje dziś.

## Jak AI korzysta z bazy wiedzy

Mała baza, na kilkadziesiąt stron, mieści się w całości w [oknie kontekstowym](slownik/context-window.html): wgrywa się ją do projektu albo do stałych instrukcji asystenta i model widzi wszystko naraz. Dużej bazy nie da się przekazać w całości, więc podłącza się do niej wyszukiwanie, które przy każdym pytaniu znajduje pasujące fragmenty ([RAG](slownik/rag.html)).

W obu przypadkach jakość odpowiedzi jest ograniczona jakością bazy. Wyszukiwanie znajdzie nieaktualną procedurę równie pewnie jak obowiązującą, a model opowie ją gładko i z odnośnikiem.

## Co sprawia, że baza nadaje się dla AI

Jeden dokument odpowiada na jedno pytanie albo opisuje jeden temat, a tytuł mówi, o czym jest. Warunki są zapisane wprost, z datami i wyjątkami, bez odesłań w rodzaju „jak zwykle”. Ta sama rzecz wszędzie nazywa się tak samo, inaczej wyszukiwanie nie połączy „zwrotu” w jednym dokumencie z „reklamacją” w innym. Dokumenty są przechowywane jako tekst: skany i zdjęcia przechodzą najpierw [rozpoznawanie dokumentów](slownik/document-recognition.html), a jego wynik warto sprawdzić.

Najtrudniejsze jest to, że duża część wiedzy firmy nie jest nigdzie zapisana. Żyje w głowach doświadczonych pracowników, w korespondencji i w nawykach działu. Takie miejsca znajduje się podczas [audytu procesów](slownik/process-audit.html), a spisanie tej wiedzy zwykle zajmuje więcej czasu niż konfiguracja techniczna.

## Kto ją prowadzi

Baza wiedzy potrzebuje właściciela z jasnym obowiązkiem: gdy zmienia się zasada, zmienia się też dokument w bazie. Potrzebny jest też tryb przeglądu, na przykład raz na kwartał według listy dokumentów z datą ostatniego sprawdzenia. Nieaktualna baza szkodzi bardziej niż pusta: pusta uczciwie nie odpowiada, nieaktualna odpowiada błędnie i z odnośnikiem do źródła.

## Jak to zwykle wygląda

Firma postanawia zbudować asystenta, który odpowiada pracownikom na pytania o wewnętrzne zasady. Zbiera się wszystko, co leży na dysku, i wgrywa. Pierwsze testy pokazują, że na proste pytania asystent odpowiada dobrze, a na te, dla których go robiono, słabo: jak obsłużyć wyjątek, do kogo dzwonić przy awarii, co zrobić z nietypowym klientem.

Odpowiedzi na te pytania w dokumentach po prostu nie ma. Znają je dwie, trzy osoby, a nowi pracownicy za każdym razem pytają właśnie je. Projekt zamienia się w pracę nad spisaniem tej wiedzy, a asystent zaczyna być przydatny, kiedy ta praca jest zrobiona. Przy okazji firma zyskuje coś, czego wcześniej nie miała: zasady, które nie odejdą razem z pracownikiem.

## Co ustalić z wyprzedzeniem

Na jakie pytania baza ma odpowiadać i kto je zadaje: pracownicy, klienci czy jedni i drudzy. Które dokumenty uznaje się za aktualne i co zrobić ze starymi wersjami. Kto jest właścicielem bazy i jak często ją przegląda. Czyja wiedza istnieje dziś tylko w głowie i kto ją spisze. I jak sprawdzić odpowiedzi przed uruchomieniem: zestaw pytań ze znanymi odpowiedziami, przez który przepuszcza się asystenta po każdej większej aktualizacji bazy.

---

**Powiązane terminy:** [RAG](slownik/rag.html) · [Okno kontekstowe](slownik/context-window.html) · [Rozpoznawanie dokumentów](slownik/document-recognition.html) · [Audyt procesów](slownik/process-audit.html)

Chcesz sprawdzić, jaka wiedza w twoim dziale istnieje tylko w głowach? [Audyt AI w dziale →](audit.html)
