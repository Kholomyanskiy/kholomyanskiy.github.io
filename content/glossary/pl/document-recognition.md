---
slug: document-recognition
title: "Rozpoznawanie dokumentów (OCR): rodzaje i jak wybrać"
description: "Rozpoznawanie dokumentów zamienia skany i zdjęcia w tekst i dane. Jakie są rodzaje, od klasycznego OCR po modele z widzeniem, i jak sprawdzać wynik."
published: 2026-11-08
updated: 2026-11-08
---

# Rozpoznawanie dokumentów (OCR)

Rozpoznawanie dokumentów to zamiana skanu, zdjęcia albo PDF-a w postaci obrazu na tekst i dane, z którymi program może pracować: wyszukać, zsumować, wprowadzić do ewidencji. Potocznie całość nazywa się OCR (optical character recognition, optyczne rozpoznawanie znaków), choć pod jedną nazwą kryją się różne technologie o różnych mocnych stronach. Wybór między nimi decyduje o tym, ile ręcznej pracy zostanie po automatyzacji.

## Jakie są rodzaje

Klasyczny OCR znajduje na obrazie litery i cyfry i zwraca tekst. Jest szybki, tani i dobrze radzi sobie z czystym drukiem: umowami, pismami, stronami książek. Na wyjściu jest jednak tylko tekst, bez zrozumienia, gdzie jest numer dokumentu, a gdzie kwota. Pognieciony paragon, pieczątka na tekście albo zdjęcie pod kątem wyraźnie obniżają jakość.

Wyciąganie danych według szablonu dodaje do OCR oznaczenia: w dokumencie znanego rodzaju pola są zaznaczone z góry, a system pobiera z nich wartości. Sprawdza się przy strumieniu jednakowych formularzy od tych samych nadawców i słabo, gdy formaty ciągle się zmieniają.

Modele językowe z widzeniem czytają cały obraz i od razu zwracają potrzebne pola: sklep, datę, pozycje, sumę. Nie potrzebują szablonu dla każdego formatu, radzą sobie ze zdjęciami pod kątem i nietypowym układem. Druga strona jest taka, że model potrafi pewnie wpisać wiarygodną liczbę tam, gdzie na zdjęciu nic nie da się odczytać. To ta sama [halucynacja](slownik/hallucination.html), tylko w liczbach.

Pismo odręczne to osobny przypadek. Rozpoznają je wszystkie trzy podejścia, ale z wyraźnie większym odsetkiem błędów, i bez sprawdzenia przez człowieka takie dane zwykle nie trafiają do ewidencji.

## Tekst czy dane

Do wyszukiwania w archiwum i do [bazy wiedzy](slownik/knowledge-base.html) wystarczy tekst: ważne, żeby słowa były rozpoznane, a dokument dawał się znaleźć. Księgowość i ewidencja potrzebują danych: konkretnych pól ze sprawdzonymi wartościami. To dwa różne zadania z różnymi wymaganiami co do jakości. Literówka w słowie prawie nie przeszkadza w wyszukiwaniu, literówka w kwocie trafia do raportu.

## Jak sprawdza się wynik

Najbardziej przydatne kontrole opierają się na wewnętrznej logice dokumentu. Suma pozycji musi zgadzać się z sumą całkowitą. Podatek musi odpowiadać stawce. Data nie może być z przyszłości. NIP ma cyfrę kontrolną i błędnie odczytany numer najczęściej jej nie przechodzi. Takie reguły sprawdza kod, bez udziału modelu.

To, co nie przeszło kontroli albo zostało rozpoznane z niską pewnością, trafia do [człowieka w pętli](slownik/human-in-the-loop.html). Dobry system rozpoznawania nie obiecuje zera błędów, tylko pokazuje, które dokumenty trzeba obejrzeć.

## Kiedy rozpoznawanie nie jest potrzebne

Najpewniejszy jest dokument, którego nie trzeba było rozpoznawać. PDF wyeksportowany z programu zawiera już tekst. W Polsce od 2026 roku faktury między firmami coraz częściej przechodzą przez KSeF jako dane ustrukturyzowane i można je dostać bez ani jednego skanu. Zanim zautomatyzuje się rozpoznawanie, warto sprawdzić, czy tych samych danych nie da się pobrać elektronicznie u źródła.

## Z praktyki

Dla bota na Telegramie do ewidencji wydatków osobistych zbudowaliśmy rozpoznawanie polskich paragonów ze zdjęć. Klasyczny OCR dałby tekst, z którego sklep, datę, pozycje i sumę trzeba by wyciągać osobnymi regułami dla każdego formatu paragonu, a sieci handlowe mają różne formaty. Dlatego paragon czyta model z widzeniem i od razu zwraca pola. Poważnych błędów w rozpoznawaniu paragonów nie było.

Najważniejszy wniosek dotyczył wyboru podejścia. Przy paragonach, gdzie formatów jest dużo, a każdy dokument jest mały, model z widzeniem okazał się prostszy i tańszy w konfiguracji. Przy strumieniu jednakowych umów klasyczny OCR z regułami może być pewniejszy i kilkakrotnie tańszy.

## Co ustalić z wyprzedzeniem

Jakie dokumenty i w jakiej liczbie trzeba rozpoznawać i na ile różnią się ich formaty. Czy potrzebny jest tekst do wyszukiwania, czy dane do ewidencji. Jakie kontrole wykonuje kod i co dzieje się z dokumentem, który ich nie przeszedł. Kto ogląda wątpliwe dokumenty i ile dziennie jest dopuszczalne. I czy część dokumentów da się dostać w formie elektronicznej, żeby w ogóle ich nie rozpoznawać.

---

**Powiązane terminy:** [Baza wiedzy dla AI](slownik/knowledge-base.html) · [Halucynacje AI](slownik/hallucination.html) · [Człowiek w pętli](slownik/human-in-the-loop.html) · [RAG](slownik/rag.html)

Chcesz zautomatyzować obsługę dokumentów w swojej firmie? [Projektowanie rozwiązania AI →](solution-design.html)
