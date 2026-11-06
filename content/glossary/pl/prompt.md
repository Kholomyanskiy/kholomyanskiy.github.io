---
slug: prompt
title: "Prompt: czym jest i jak zlecać zadania AI"
description: "Prompt to tekst, którym zleca się zadanie modelowi językowemu. Z czego się składa, gdzie nie wystarcza i kiedy potrzebny jest szablon albo specyfikacja."
published: 2026-11-07
updated: 2026-11-07
---

# Prompt

Prompt (z angielskiego: podpowiedź) to tekst, który człowiek przekazuje modelowi językowemu: pytanie, zadanie, instrukcja, przykład albo dane do przetworzenia. Poza ogólną wiedzą z treningu model wie o zadaniu tylko tyle, ile zapisano w prompcie i we wcześniejszych wiadomościach rozmowy. Dlatego od promptu zależy, czy odpowiedź będzie przydatna od razu, czy trzeba będzie ją kilka razy doprecyzowywać.

Rozróżnia się prompt użytkownika, czyli wiadomość na czacie, i prompt systemowy: stałe instrukcje, które model dostaje przed rozpoczęciem rozmowy. Prompt systemowy ustawiają twórcy usługi albo sam użytkownik w ustawieniach projektu, asystenta lub agenta. W narzędziach dla programistów tę samą rolę pełnią pliki z zasadami, na przykład CLAUDE.md w Claude Code.

## Z czego składa się dobry prompt

Dobry prompt opisuje zadanie tak, jak opisałoby się je nowemu pracownikowi, bystremu, ale niewiedzącemu nic o firmie. Zawiera samo zadanie i cel: co trzeba zrobić i po co. Zawiera kontekst: dla kogo jest wynik, jakie dokumenty i dane uwzględnić, co już zrobiono. Określa format: tabela, e-mail albo kod, długość, język. Określa ograniczenia: czego robić nie wolno i co uznać za błąd. Jeśli potrzebny jest konkretny styl, pomaga przykład gotowego wyniku.

Sama długość promptu niewiele znaczy. Krótkie polecenie sprawdza się, gdy zadanie jest proste i typowe. Im bardziej wynik zależy od zasad firmy, tym więcej tych zasad powinno trafić do promptu.

## Prompt, szablon i specyfikacja

Jednorazowe zadanie załatwia jednorazowy prompt. Jeśli to samo zadanie wraca co tydzień, prompt zapisuje się jako szablon albo stałą instrukcję projektu. Wtedy nikt nie wpisuje go od nowa, a wynik nie zależy od tego, kto danego dnia pisze polecenie.

Gdy zadanie jest duże, rozciąga się na kilka sesji albo wynik trzeba sprawdzać według zasad, jeden prompt przestaje wystarczać. Zasady, granice i warunki sprawdzenia przenosi się do [specyfikacji](slownik/ai-specification.html). Model czyta ją na początku każdej sesji, ludzie odbierają na jej podstawie pracę, a prompt wyznacza bieżący krok.

## Gdzie prompt nie pomaga

Prompt nie da modelowi wiedzy, której nie ma ani w nim, ani w treningu modelu. Jeśli odpowiedź ma opierać się na dokumentach firmy, przekazuje się je modelowi w całości albo podłącza wyszukiwanie w nich ([RAG](slownik/rag.html)). Bez tego model wypełni lukę wiarygodnie brzmiącym tekstem i powstanie [halucynacja](slownik/hallucination.html).

Ilość tekstu, którą model obejmuje naraz, ogranicza [okno kontekstowe](slownik/context-window.html). W długiej rozmowie instrukcje z początku tracą wagę i model stopniowo od nich odchodzi. Powtarzanie ich w każdej wiadomości jest mniej pewne niż trzymanie ich w prompcie systemowym albo w pliku z zasadami.

Przeformułowania też mają granicę. Jeśli trzecia wersja polecenia daje ten sam błędny wynik, przyczyną są zwykle brakujące dane albo niejasno postawione zadanie.

## Z praktyki

Ze specjalistą od rekrutacji budowaliśmy sprawdzanie CV pod kątem kryteriów roli. Gdy AI się myliło, pierwszym odruchem było przepisanie polecenia. Pewniejsze okazało się doprecyzowanie kryterium jedną linijką w pliku, według którego idzie sprawdzanie. Polecenie zostawało bez zmian, plik z każdą poprawką stawał się dokładniejszy, a poprawka działała dla wszystkich kolejnych CV. Więcej w [opisie case'u](case-recruitment.html).

Z właścicielką kawiarni zbudowaliśmy formularz zgłoszeń w HTML, który potem osadza się na stronie w WordPressie. Wystarczyły jeden czy dwa prompty: zadanie było małe i samodzielne, a wymagania wobec formularza znane z góry. Dopracowania wymagał tylko wygląd, bo formularz trochę rozjechał się z układem strony. Im dokładniej wynik ma pasować do czegoś, co już istnieje, tym więcej tego istniejącego warto pokazać modelowi.

## Co ustalić z wyprzedzeniem

Które zadania się powtarzają i zasługują na zapisany szablon. Gdzie przechowywane są szablony i instrukcje i kto je aktualizuje, gdy zmieniają się zasady. Jakie dane wolno przekazywać modelowi, a jakich nie. I po jakich cechach sprawdza się wynik, żeby ocena nie zależała od tego, kto sprawdza: z tych cech powstają [kryteria odbioru](slownik/acceptance-criteria.html).

---

**Powiązane terminy:** [Specyfikacja AI](slownik/ai-specification.html) · [Okno kontekstowe](slownik/context-window.html) · [Halucynacja](slownik/hallucination.html) · [Agent AI](slownik/agent.html)

Chcesz nauczyć się zlecać zadania AI we własnej pracy? [Szkolenie AI →](training.html)
