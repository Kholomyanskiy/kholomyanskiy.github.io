---
slug: hallucination
title: "Halucynacje AI: dlaczego model myli się z pewnością"
description: "Halucynacje AI to wiarygodne, ale fałszywe odpowiedzi modelu językowego. Skąd się biorą, jak wyglądają w pracy i jak ograniczyć ryzyko przed uruchomieniem."
published: 2026-11-07
updated: 2026-11-07
---

# Halucynacje AI

Halucynacja AI to odpowiedź modelu językowego, która brzmi pewnie i wiarygodnie, ale nie zgadza się z rzeczywistością: zmyślony fakt, nieistniejące źródło, błędna liczba. Termin jest umowny, bo model nie ma percepcji, która mogłaby go zwieść. Część badaczy woli słowo „konfabulacja”, ale w użyciu przyjęła się „halucynacja”.

Przyczyna tkwi w samej budowie modelu. Buduje on odpowiedź jako najbardziej prawdopodobny ciąg dalszy tekstu i domyślnie nie sprawdza jej ze źródłem. Gdy brakuje potrzebnej wiedzy, prawdopodobny ciąg dalszy i tak się znajduje, a brzmi równie gładko jak poprawny. Model potrafi powiedzieć „nie wiem”, ale robi to rzadziej, niż powinien, jeśli się go o to nie poprosi.

## Jak wygląda

Najczęściej model wymyśla coś, co przypomina prawdziwe: odwołanie do przepisu z wiarygodnym numerem, cytat, tytuł publikacji, funkcję w bibliotece programistycznej, punkt umowy. Bywa też subtelniej. Model dostaje prawdziwy dokument, ale w streszczeniu myli datę, przypisuje warunek niewłaściwej stronie albo dopisuje punkt, którego tam nie ma.

Groźny jest nie sam błąd, bo ludzie też się mylą. Groźne jest to, że błędna odpowiedź brzmi dokładnie tak samo jak poprawna i wychwycić ją można tylko, porównując ze źródłem.

## Znane przypadki

W 2023 roku w Nowym Jorku adwokaci złożyli w sądzie pismo z odwołaniami do orzeczeń wygenerowanych przez ChatGPT. Kilka z tych spraw nie istniało. Sąd nałożył na adwokatów grzywnę, a historia stała się podręcznikowym przykładem.

W 2024 roku czatbot na stronie Air Canada podał pasażerowi warunki zwrotu, których nie było w regulaminie linii. Trybunał w Kanadzie nakazał firmie wypłacić różnicę: firma odpowiada za to, co mówi jej bot na jej stronie. Dla biznesu to najważniejszy wniosek: odpowiedzialność za odpowiedź AI ponosi ten, kto pokazał ją klientowi.

## Dlaczego nie da się jej całkiem wyłączyć

Z każdą generacją modeli halucynacji jest mniej, ale całkiem nie znikają: to druga strona tego, że model swobodnie formułuje tekst. Dlatego pytanie stawia się inaczej: gdzie błąd jest dopuszczalny, gdzie wychwyci go kontrola i gdzie koszt błędu jest tak wysoki, że odpowiedzi nie wolno wypuścić bez sprawdzenia przez człowieka.

## Jak ograniczyć ryzyko

Najskuteczniejszy sposób: dać modelowi źródło i poprosić, by odpowiadał tylko na jego podstawie. W przypadku dokumentów firmy to wyszukiwanie w nich ([RAG](slownik/rag.html)) z odnośnikiem do dokumentu w każdej odpowiedzi. Odnośnik można otworzyć i sprawdzić.

Pomaga też wyraźne pozwolenie na odpowiedź „w dokumentach tego nie ma” i opisanie w [prompcie](slownik/prompt.html) albo specyfikacji, co robić, gdy brakuje danych. Tam, gdzie odpowiedź trafia do systemu ewidencji, sprawdza ją kod: format, dopuszczalne wartości, zgodność z danymi źródłowymi. Tam, gdzie w grę wchodzą pieniądze albo zobowiązania wobec klienta, decyzja zostaje przy [człowieku w pętli](slownik/human-in-the-loop.html).

## Z praktyki

W projekcie automatyzacji katalogu sklepu internetowego AI pisało opisy i słowa kluczowe dla produktów w kilku kolorach. Przy sprawdzaniu kolejnych wersji wciąż wracały te same błędy: w słowach kluczowych pojawiały się kolory, w których produkt nie występuje, trafiały się zakazane zwroty reklamowe, mieszały się języki. Każdy taki tekst wyglądał porządnie i w pojedynczym egzemplarzu błąd łatwo było przeoczyć.

Ręczne poprawki w gotowych tekstach się nie utrzymywały: przy następnym przebiegu błąd wracał. Zadziałało dopiero przeniesienie poprawek do kodu generującego i dodanie automatycznych kontroli, które odrzucają tekst przed eksportem. Więcej o projekcie w [portfolio](portfolio.html).

## Co ustalić z wyprzedzeniem

W którym miejscu procesu odpowiedź AI idzie dalej bez człowieka i ile kosztowałby błąd na tym etapie. Z jakich źródeł model bierze fakty i co odpowiada, gdy nic w nich nie ma. Które kontrole wykonuje kod, a które człowiek. I jaki zestaw pytań kontrolnych ze znanymi odpowiedziami trafi do [kryteriów odbioru](slownik/acceptance-criteria.html), żeby częstość błędów zmierzyć przed uruchomieniem.

---

**Powiązane terminy:** [RAG](slownik/rag.html) · [Człowiek w pętli](slownik/human-in-the-loop.html) · [Kryteria odbioru](slownik/acceptance-criteria.html) · [Prompt](slownik/prompt.html)

Chcesz wiedzieć, gdzie błąd AI w twoim procesie kosztowałby najwięcej? [Audyt AI w dziale →](audit.html)
