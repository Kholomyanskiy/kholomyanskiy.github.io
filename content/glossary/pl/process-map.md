---
slug: process-map
title: "Mapa procesów: czym jest i po co ją tworzyć przed wdrożeniem AI"
description: "Mapa procesów pokazuje, jak naprawdę przebiega praca w dziale. Czym różni się od schematu blokowego, jak ją przygotować i co ustalić przed wdrożeniem AI."
---

# Mapa procesów

Mapa procesów pokazuje, jak praca naprawdę przebiega w dziale lub firmie: kto co robi, w jakiej kolejności, co przekazuje dalej, gdzie czeka i gdzie omija zasady, żeby zdążyć. Tworzy się ją na podstawie tego, co ludzie faktycznie robią. Pomaga zdecydować, co zautomatyzować, a czego nie ruszać.

## Czym mapa różni się od schematu blokowego

Schemat blokowy w procedurze pokazuje, jak proces ma przebiegać. Mapa pokazuje, jak przebiega naprawdę. Zawiera to, czego nie ma w procedurze: prywatne arkusze w Excelu, telefon do kolegi, żeby „dopytać”, ręczne sprawdzenie, które jedna osoba wykonuje z przyzwyczajenia, wiadomość czekającą tydzień na odpowiedź. AI zawodzi właśnie w tych miejscach, bo nikt o nich nie powiedział.

Na mapie zaznacza się:

- poszczególne kroki i osoby, które je wykonują;
- co i w jakiej formie przekazuje się między ludźmi i działami;
- gdzie praca czeka i jak długo;
- używane dane i narzędzia;
- wyjątki i obejścia;
- miejsca, w których błąd dużo kosztuje.

## Jak ją przygotować

Mapa powstaje w pierwszych dniach [audytu procesów](slownik/process-audit.html). Ma jedno źródło: to, co ludzie rzeczywiście robią. Żeby to uchwycić, robi się [fotografię tygodnia pracy](metodichka.html): każdy zapisuje, czym się zajmował, ile czasu to zajęło, od kogo otrzymał zadanie i dokąd trafił wynik. Z tych zapisów powstaje całościowy obraz, który pokazuje się osobom wykonującym tę pracę. To one muszą potwierdzić mapę. Sam kierownik nie wystarczy, bo wie, jak praca powinna przebiegać.

W dużej firmie nie da się przeanalizować wszystkich naraz i nie ma takiej potrzeby. Wybiera się jeden łańcuch zadań, który ma się zmienić, i przechodzi się go od początku do końca.

## Z praktyki

Przez ponad dziesięć lat pracowałem w IT dużego operatora sieci dystrybucyjnej energii elektrycznej: kilka tysięcy pracowników, oddziały, dyrekcje, rejony, a w każdej jednostce własne działy. Procesy biznesowe opisywano na górze, w systemie zarządzania jakością, starannie i szczegółowo. Na dole życie toczyło się własnym torem. Opisy stanowisk często dopasowywano do pracownika i luk w procesach, a jeszcze częściej pracownik sam pisał swój opis po kilku miesiącach pracy. Potem nie zmieniał się przez lata. Praca zmieniała się codziennie: polecenia kierownika, wiadomości, pilne zadania, których nie było w żadnym dokumencie.

Nie wdrażano tam wtedy AI, ale łatwo sobie wyobrazić, jak by to wyglądało. Wymagania oparte na procedurach i opisach stanowisk, a na wyjściu ogólne [wyszukiwanie w dokumentach](slownik/rag.html), i nikt nie potrafiłby wyjaśnić, jaki problem rozwiązuje. Automatyzacja oparta na mapie procedur automatyzuje procedury. Prawdziwa praca toczy się obok.

## Co ustalić z góry

Jak szczegółowa ma być mapa: do poziomu zadania czy pojedynczego kroku. Który łańcuch zadań przeanalizować jako pierwszy. Gdzie mapa będzie dostępna po audycie i kto ją zaktualizuje, gdy zmieni się proces. Mapa, której nikt nie aktualizuje, po roku staje się kolejną procedurą.

## Co dalej

Mapa pokazuje, gdzie proces się załamie, jeśli krok zostanie przekazany AI: są to [punkty awarii](slownik/failure-point.html). Pokazuje też, gdzie musi pozostać [człowiek w pętli](slownik/human-in-the-loop.html). Wybrany fragment opisuje się później w [specyfikacji AI](slownik/ai-specification.html) i sprawdza w [pilotażu](slownik/pilot.html).

---

**Powiązane terminy:** [Audyt procesów](slownik/process-audit.html) · [Punkt awarii](slownik/failure-point.html) · [Człowiek w pętli](slownik/human-in-the-loop.html) · [Specyfikacja AI](slownik/ai-specification.html)

Chcesz zobaczyć, jak naprawdę przebiega praca w twoim dziale? [Audyt AI w dziale →](audit.html)
