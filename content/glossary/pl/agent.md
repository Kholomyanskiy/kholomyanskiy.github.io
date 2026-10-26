---
slug: agent
title: "Agent AI: czym różni się od bota i kiedy jest potrzebny"
description: "Agent AI sam dobiera kroki i narzędzia do celu. Czym różni się od bota, skryptu i RPA, kiedy agent ma sens, a kiedy wystarczy prosta automatyzacja."
published: 2026-10-26
updated: 2026-10-26
---

# Agent AI

Agentem AI nazywa się dziś zwykle system oparty na modelu językowym, który sam kieruje przebiegiem pracy: dostaje cel, dobiera kroki i narzędzia, wykonuje działania i na podstawie ich wyniku decyduje, co dalej. Narzędziami mogą być poczta, arkusz, system księgowy, wyszukiwanie w dokumentach. Bot wykonuje z góry zapisany scenariusz. Agent buduje scenariusz w trakcie pracy, w granicach tego, na co mu pozwolono.

Słowo ma też szersze znaczenie. W klasycznej teorii AI agentem jest każdy system, który odbiera sygnały z otoczenia i w nim działa. Z kolei w reklamie agentem nierzadko nazywa się zwykłego chatbota albo łańcuch z jednym wywołaniem modelu. Dlatego gdy ktoś proponuje „agenta”, warto dopytać, o czym w tym rozwiązaniu AI będzie decydować samo.

## Drabina automatyzacji

Agent wyrósł z kilku pokoleń automatyzacji i każde z nich nadal działa. Warto widzieć całą drabinę, bo zadanie klienta niemal zawsze da się rozwiązać na którymś z jej szczebli.

- **Formuły i arkusze.** Excel i podobne programy liczą według formuł: sumy, stany, zestawienia. Reguły ustala człowiek, arkusz tylko liczy.
- **Skrypty i makra.** Kod w VBA, Pythonie czy PHP wykonuje sekwencję działań: zmienia nazwy plików, rozdziela pocztę według tematu, eksportuje raport. Działa ściśle według tego, co zapisano.
- **Boty i RPA.** Robot powtarza czynności człowieka w interfejsie: otwiera system, kopiuje pola, klika przyciski. Chatbot odpowiada według scenariusza albo słów kluczowych. Krok w bok od scenariusza i bot staje albo się myli.
- **Platformy automatyzacji.** Usługi takie jak Zapier, Make czy n8n pozwalają składać takie łańcuchy bez programisty: przyszedł e-mail, dane trafiły do arkusza, kierownik dostał powiadomienie.
- **AI w pojedynczym kroku.** Do sztywnego łańcucha wstawia się model językowy do jednej czynności: zrozumieć, czego dotyczy wiadomość, wyciągnąć pola z faktury, napisać szkic odpowiedzi. Scenariusz nadal jest ustalony z góry. Takie łańcuchy programiści nazywają workflow, w odróżnieniu od agentów.
- **Agent.** Model sam decyduje, co robić dalej: jakie narzędzie wywołać, co sprawdzić, kiedy się zatrzymać i zapytać człowieka.

Im wyższy szczebel, tym więcej zadań obejmuje i tym trudniej przewidzieć jego zachowanie.

## Czym agent różni się od bota

Bot wie, co robić, bo jest to zapisane w scenariuszu. Agent wie, co trzeba osiągnąć, i sam dobiera działania. Stąd praktyczne różnice.

- **Nietypowe dane wejściowe.** Bot wykłada się na wiadomości, która nie pasuje do reguły. Agent może ją przeczytać i obsłużyć.
- **Wiele kroków.** Agent potrafi zebrać dane z trzech systemów, porównać je i przygotować podsumowanie, nie mając gotowej instrukcji na taki przypadek.
- **Przewidywalność.** Bot przy tych samych danych daje ten sam wynik. Agent może dwa razy rozwiązać to samo zadanie inaczej, a czasem pewnie się pomylić: modelom zdarzają się [halucynacje](slownik/hallucination.html).

## Stopnie samodzielności

Agenci różnią się tym, na ile im pozwolono.

- **Podpowiada.** Przygotowuje szkic albo wariant decyzji, resztę robi człowiek.
- **Działa za potwierdzeniem.** Wykonuje kroki sam, ale przed ważnymi działaniami prosi o zgodę.
- **Działa sam.** Pracuje bez udziału człowieka w ramach ustalonych reguł, człowiek widzi raport.

Im droższy błąd, tym niższy poziom samodzielności i tym bliżej jest [człowiek w pętli](slownik/human-in-the-loop.html).

## Kiedy agent nie jest potrzebny

Agenta często proponuje się tam, gdzie wystarczą niższe szczeble. Jeśli zadanie da się opisać regułą, reguła jest pewniejsza. Wiadomości o określonym temacie rozdzieli filtr poczty. Raport według stałego wzoru złoży skrypt. Pieniądze, podatki, stany magazynowe i dokumenty z liczbami policzy zwykła formuła: niczego nie dopowiada i nie myli się każdego dnia inaczej.

Proste rozwiązanie jest tańsze, łatwiej je sprawdzić i utrzymać, ma mniej powodów, żeby się zepsuć. Agent dokłada opłaty za zapytania do modelu, czas na sprawdzanie jego pracy i nieprzewidywalność, którą trzeba ograniczać regułami. Wszystko to wchodzi w [całkowity koszt posiadania](slownik/total-cost-of-ownership.html).

Dobry układ jest często mieszany. Agent przegląda napływające sprawy, rozpoznaje, co przyszło, i wybiera działanie. Obliczenia robi kalkulator albo skrypt, który agent wywołuje jako narzędzie. Model decyduje, co zrobić, kod liczy.

## Kiedy agent ma sens

Tam, gdzie dane wejściowe są różnorodne i nie mieszczą się w regułach: swobodny tekst wiadomości, dokumenty w różnych formach, pytania klientów. Tam, gdzie zadanie wymaga kilku kroków w różnych systemach, a ich kolejność zależy od tego, co znaleziono po drodze. I tam, gdzie koszt pojedynczego błędu jest niewielki albo przechwytuje go kontrola.

## Z praktyki

W projekcie z agencją rekrutacyjną CV nie można wysyłać do modelu w chmurze w takiej postaci, w jakiej przyszły. Dane osobowe usuwa skrypt według sztywnych reguł: które pola usunąć i czym je zastąpić. Agent nie ma tu nic do decydowania, a błąd byłby kosztowny, więc działa najprostszy szczebel drabiny. Model językowy włącza się później, gdy zanonimizowane CV porównuje się z kryteriami roli.

Przy automatyzacji kart produktów dla sklepu internetowego podział był podobny. Część danych w cennikach dostawców pokrywała się z polami sklepu i prościej, a zarazem pewniej przenosić je skryptem. Model jest potrzebny tam, gdzie ze skąpych danych trzeba napisać opis. Gdy te dwie części się miesza i oddaje AI wszystko naraz, rośnie i koszt, i liczba błędów tam, gdzie mogło ich wcale nie być.

## Co ustalić z wyprzedzeniem

Czy zadanie da się opisać regułą. Jeśli tak, zaczyna się od reguły. Co agent może robić sam, a gdzie musi zapytać. Jakich narzędzi potrzebuje i jakie obliczenia przekazuje kodowi. Kto sprawdza jego pracę i jak często. I jak poznać, że agent działa gorzej niż proste rozwiązanie, które można postawić zamiast niego.

---

**Powiązane terminy:** [Człowiek w pętli](slownik/human-in-the-loop.html) · [Halucynacja](slownik/hallucination.html) · [Całkowity koszt posiadania](slownik/total-cost-of-ownership.html) · [RAG](slownik/rag.html) · [Prompt](slownik/prompt.html)

Chcesz ustalić, czy wystarczy bot, czy potrzebny jest agent? [Projektowanie rozwiązania AI →](solution-design.html)
