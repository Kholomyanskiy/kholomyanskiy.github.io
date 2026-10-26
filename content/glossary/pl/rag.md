---
slug: rag
title: "RAG: jak AI odpowiada na podstawie dokumentów firmy"
description: "RAG pozwala AI odpowiadać na pytania na podstawie dokumentów firmy i wskazywać źródło. Jak to działa, gdzie się myli i co ustalić przed uruchomieniem."
published: 2026-10-26
updated: 2026-10-26
---

# RAG (wyszukiwanie we własnych dokumentach)

RAG (retrieval-augmented generation, generowanie wspomagane wyszukiwaniem) to podejście, w którym model językowy najpierw wyszukuje pasujące fragmenty w określonym zbiorze dokumentów i dopiero na ich podstawie formułuje odpowiedź. Podejście opisali badacze Facebook AI w 2020 roku. Dziś tak nazywa się niemal każdy system w rodzaju „czat z naszymi dokumentami”. W małej firmie RAG służy zwykle jednemu: żeby pracownik albo klient zadał pytanie zwykłymi słowami i dostał odpowiedź z regulaminów, umów, cenników czy instrukcji firmy, z odnośnikiem do dokumentu.

## Jak to działa

Dokumenty dzieli się wcześniej na fragmenty i indeksuje tak, żeby wyszukiwarka znajdowała je po sensie pytania, nawet gdy słowa się nie pokrywają. Do każdego pytania system dobiera kilka najlepiej pasujących fragmentów i przekazuje je modelowi. Model odpowiada na ich podstawie i, jeśli tak to skonfigurowano, podaje źródło.

Model nie zapamiętuje dokumentów. Widzi tylko to, co wyszukiwarka znalazła pod konkretne pytanie. Dlatego jakość odpowiedzi zależy od dwóch rzeczy naraz: czy do wyników trafił właściwy fragment i czy model dobrze go przeczytał.

## Gdzie RAG się myli

Najczęściej myli się wyszukiwanie. Znajduje nieaktualną wersję regulaminu albo podobny dokument w innej sprawie. Przynosi połowę odpowiedzi, gdy druga połowa leży w sąsiednim pliku. Nie widzi tabel i skanów, które źle się rozpoznały. Zdarza się też, że odpowiedzi w dokumentach w ogóle nie ma, a model i tak odpowiada, pewnie i wiarygodnie.

Odnośnik do źródła zmniejsza ryzyko: można otworzyć dokument i sprawdzić. Tam, gdzie odpowiedź wpływa na pieniądze albo zobowiązania wobec klienta, zwykle obowiązuje zasada [człowieka w pętli](slownik/human-in-the-loop.html).

## RAG, baza danych czy rejestr

Nazwa RAG opisuje schemat „najpierw znajdź, potem odpowiedz”, a szukać można na różne sposoby. Wyszukiwanie wektorowe w pociętych fragmentach to tylko jeden z nich, po prostu najbardziej znany.

Jeśli dokumentów jest niewiele i mieszczą się w [oknie kontekstowym](slownik/context-window.html) modelu, przekazuje się je w całości i wyszukiwanie w ogóle nie jest potrzebne. Dane strukturalne (kwoty, daty, klienci, statusy) najlepiej trzymać w zwykłej bazie danych, do której model wysyła zapytanie. Wyszukiwanie wektorowe nie policzy umów, które wygasają w grudniu: szuka podobnego tekstu i liczyć nie umie.

Gdy dokumentów są setki, a pytanie zwykle wskazuje konkretny dokument, często wystarcza rejestr z krótkim opisem każdego z nich. Model wybiera dokument z rejestru i czyta go w całości. Klasyczny RAG z wyszukiwaniem wektorowym sprawdza się tam, gdzie jest dużo ciągłego tekstu, pytania dotyczą sensu i nie wiadomo z góry, gdzie leży odpowiedź.

W praktyce te sposoby się łączy. Dokumentom nadaje się metadane (klient, typ, data), według nich najpierw zawęża się zakres i dopiero w nim szuka się po sensie. Rozsądnie zacząć od najprostszego wariantu, który obsłuży typowe pytania: rejestr łatwiej utrzymać i widać w nim, skąd wzięła się odpowiedź.

## Jak sprawdzić przed uruchomieniem

Przed uruchomieniem warto opisać w [specyfikacji](slownik/ai-specification.html), na jakie pytania system odpowiada i co mówi, gdy w dokumentach nie ma odpowiedzi. Zestaw pytań kontrolnych ze znanymi z góry odpowiedziami staje się podstawą [kryteriów odbioru](slownik/acceptance-criteria.html). Sprawdzać najlepiej w ramach [pilotażu](slownik/pilot.html), z ludźmi, którzy będą zadawać pytania na co dzień.

## Jak to zwykle wygląda

Firma wgrywa do systemu folder z umowami i regulaminami z kilku lat. Leżą w nim wersje obowiązujące, stare redakcje i szkice z dopiskiem „final_2”. Na początku odpowiedzi brzmią przekonująco, z odnośnikami do dokumentów. Potem ktoś zauważa, że bot cytuje warunki z umowy, którą dawno podpisano na nowo, a odnośnik prowadzi do starej wersji.

Model zrobił w tej sytuacji dokładnie to, czego od niego oczekiwano: odpowiedział na podstawie fragmentu, który znalazło wyszukiwanie. Błąd pojawił się wcześniej, kiedy decydowano, co wgrać i kto pilnuje wersji.

## Co ustalić z wyprzedzeniem

Jakie dokumenty wgrywamy i kto odpowiada za to, żeby w systemie leżały wersje obowiązujące. Kto będzie zadawał pytania i jakie. Co system odpowiada, gdy w dokumentach nie ma odpowiedzi. Kto i jak często sprawdza odpowiedzi. I jak ludziom wytłumaczyć, co jest w środku i jak z tego korzystać: bez tego nawet sprawny system wygląda na zepsuty.

---

**Powiązane terminy:** [Baza wiedzy](slownik/knowledge-base.html) · [Halucynacja](slownik/hallucination.html) · [Rozpoznawanie dokumentów](slownik/document-recognition.html) · [Specyfikacja AI](slownik/ai-specification.html)

Chcesz, żeby AI odpowiadało na podstawie dokumentów twojej firmy? [Projektowanie rozwiązania AI →](solution-design.html)
