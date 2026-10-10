---
slug: acceptance-criteria
title: "Kryteria odbioru rozwiązania AI: czym są i jak je ustalać"
description: "Kryteria odbioru określają, po czym poznać, że praca jest ukończona. Jak wygląda dobre kryterium, dlaczego AI utrudnia ocenę i co ustalić przed pracą."
---

# Kryteria odbioru

Kryteria odbioru to sprawdzalne warunki, które pozwalają stwierdzić, czy praca została ukończona. Zapisuje się je przed rozpoczęciem prac, tak aby klient i wykonawca rozumieli je tak samo i mogli ocenić wynik bez sporu.

## Jak wygląda dobre kryterium

„Bot odpowiada klientom” nie jest kryterium: do tego opisu pasuje każdy bot, także taki, który odpowiada nie na temat. „Bot odpowiada na pytania z zatwierdzonej listy, a pozostałe przekazuje menedżerowi w ciągu minuty” jest już kryterium. Można je sprawdzić, a po sprawdzeniu nie ma o co się spierać.

Dobre kryterium ma cztery cechy. Jest sprawdzalne: można odpowiedzieć „tak” lub „nie” albo coś zmierzyć. Sprawdza się je na twoich danych, ze wszystkimi ich osobliwościami. Ma próg, poniżej którego praca nie zostaje odebrana. Z góry wiadomo też, kto i jak je sprawdzi. Warto zapisywać każde kryterium w jednym zdaniu: co sprawdzamy, na jakich danych, jaką metodą i jaki wynik wystarczy. Na przykład: „Kwota i numer faktury są poprawnie odczytane ze wszystkich dokumentów zestawu testowego; księgowy sprawdza je z oryginałami”.

## Dlaczego AI utrudnia ocenę

Zwykły program zwraca ten sam wynik dla tych samych danych. Model może odpowiadać różnie, a na trzech udanych przykładach każda demonstracja wygląda świetnie. Dlatego kryterium dla AI prawie zawsze określa odsetek: w ilu dokumentach z zestawu testowego wynik jest poprawny i ile błędów można zaakceptować.

Błędy też nie mają jednakowej wagi. Literówka w komentarzu i błędna kwota na fakturze mają różne skutki, co również trzeba zapisać. Dla jednego pola dopuszczalny odsetek błędów może wynosić zero, a dla innego można zaakceptować pomyłki, jeśli takie przypadki trafiają do [człowieka w pętli](slownik/human-in-the-loop.html).

Jeszcze jedna sprawa: kryterium powinno dotyczyć efektu pracy. Sama jakość modelu nie wystarczy. Model może rozpoznawać prawie wszystko poprawnie, a czas pracownika na zadanie się nie zmieni, bo nadal sprawdza każdy dokument.

## Typowe błędy

W opisie wymagań pojawia się „wygodny interfejs” i „wysoka jakość rozpoznawania”, wykonawca oddaje to, co udało mu się zrobić, i nie ma podstaw do sporu. Kryteria zapisuje się po zakończeniu prac i dopasowuje do wyniku. Kryteria ustala sam wykonawca, więc oczywiście zapisuje tylko to, co na pewno zrealizuje. Sprawdza się, czy funkcje istnieją, ale nie to, czy rozwiązują problem.

Brak kryteriów szkodzi obu stronom. Wykonawca również nie może zakończyć pracy: wyniku nie określono z góry, więc za każdym razem jest „nie całkiem taki”, a poprawki ciągną się bez końca. W dużych firmach z formalnym odbiorem zdarza się to rzadko, częściej u klientów indywidualnych i w małych firmach. Kryteria chronią klienta przed pracą wykonaną na wyczucie, a wykonawcę przed projektem, którego nie da się zakończyć.

## Z praktyki

W moich projektach nie zdarzały się spory o odbiór. Mam za to historię, w której nie zapisaliśmy, co uznamy za sukces. Sortowanie przychodzącej poczty, o którym pisałem w artykule o [audycie procesów](slownik/process-audit.html), zrobiliśmy bez ustalenia, ile godzin dziennie ma ono oszczędzić i jaki odsetek wiadomości może trafić do złego folderu. Dlatego do dziś nie wiemy, czy ta praca się opłaciła.

## Co ustalić przed rozpoczęciem prac

Zestaw przykładów testowych z prawdziwych danych, także tych kłopotliwych. Co uznajemy za błąd i które błędy są krytyczne. Próg dla każdego kryterium. Jak praca przebiega obecnie, żeby było z czym porównać wynik; dobrym sposobem na ustalenie tego jest [pilotaż](slownik/pilot.html). Kto odbiera pracę i co się dzieje, jeśli nie przejdzie oceny.

Wszystko to należy do [specyfikacji AI](slownik/ai-specification.html). Kryteria bez specyfikacji sprawdzają nieokreślony cel. Specyfikacja bez kryteriów nie daje sposobu na ocenę wyniku.

---

**Powiązane terminy:** [Specyfikacja AI](slownik/ai-specification.html) · [Pilotaż](slownik/pilot.html) · [Człowiek w pętli](slownik/human-in-the-loop.html) · [Halucynacja](slownik/hallucination.html)

Czy możesz sprawdzić, czy wykonawca zrobił to, za co płacisz? [Specyfikacja AI →](spec.html)
