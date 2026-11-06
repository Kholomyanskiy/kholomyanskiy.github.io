---
slug: context-window
title: "Okno kontekstowe: ile AI ma w głowie naraz"
description: "Okno kontekstowe określa, ile tekstu model widzi naraz. Co je wypełnia, co się dzieje przy przepełnieniu i jak pracować z długimi zadaniami."
published: 2026-11-07
updated: 2026-11-07
---

# Okno kontekstowe

Okno kontekstowe to ilość tekstu, którą model językowy widzi jednocześnie, gdy przygotowuje odpowiedź. Trafia do niego wszystko naraz: instrukcje systemowe, wgrane pliki, historia rozmowy i sama odpowiedź, którą model właśnie pisze. Czego nie ma w oknie, tego dla modelu nie ma. Model nie ma pamięci między rozmowami: każdy nowy czat zaczyna się od pustego okna, chyba że usługa sama wstawi do niego zapisane notatki.

Rozmiar okna mierzy się w tokenach. Token to fragment słowa: w tekście angielskim to średnio około trzech czwartych słowa, a słowa polskie i rosyjskie dzielą się na więcej części, więc ta sama treść zajmuje więcej tokenów. Współczesne modele mają okna rzędu setek tysięcy tokenów, niektóre około miliona. Dla porównania: sto tysięcy tokenów mieści sporą książkę.

## Co wypełnia okno

Miejsce w oknie kończy się szybciej, niż się wydaje. Każde pytanie i każda odpowiedź zostają w historii i zajmują miejsce do końca rozmowy. Załączony PDF z tabelami i skanami zamienia się w dużą ilość tekstu. Przy pracy z kodem agent czyta pliki projektu, uruchamia polecenia i dostaje ich wyniki, a to wszystko również gromadzi się w oknie.

Dlatego rozmowa, która zaczęła się od krótkiego pytania, po paru godzinach pracy może zbliżyć się do limitu, nawet jeśli nikt nie wgrywał niczego dużego.

## Co się dzieje, gdy okno się zapełni

Usługi zachowują się różnie. Jedne odmawiają dalszej pracy i proponują nowy czat. Inne po cichu odrzucają najstarsze wiadomości. Jeszcze inne streszczają historię i pracują dalej na streszczeniu. W każdym z tych przypadków część wcześniejszych ustaleń ginie albo się upraszcza, a model może zapomnieć umowę z początku rozmowy i nic o tym nie powiedzieć.

## Dlaczego duże okno nie rozwiązuje wszystkiego

Nawet gdy tekst mieści się w całości, model nie korzysta z niego równomiernie. Badania z 2023 roku pokazały, że informacje z początku i końca długiego tekstu modele odnajdują pewniej niż te ze środka. Od tamtej pory modele wyraźnie się poprawiły, ale zasada pozostaje praktyczna: im dłuższy kontekst, tym większa szansa, że potrzebny szczegół zginie wśród reszty.

Długi kontekst jest też droższy i wolniejszy: przy pracy przez API płaci się za tokeny, a każde kolejne pytanie w długiej rozmowie przesyła modelowi całą historię od nowa. Stąd prosta zasada: przekazywać modelowi tyle, ile potrzeba do zadania, i nic ponad to.

## Jak sobie z tym radzić

Zasady i decyzje potrzebne w każdej rozmowie trzyma się w pliku: w stałych instrukcjach projektu albo w pliku z zasadami, takim jak CLAUDE.md w Claude Code. Model czyta go na początku każdej sesji i nic nie zależy od tego, co zostało w historii. Na tym samym podejściu opiera się [specyfikacja AI](slownik/ai-specification.html).

Duże zadanie dzieli się na części, a każdą część realizuje w osobnej sesji. Na koniec sesji wynik zapisuje się w pliku, a następna sesja zaczyna od niego. To pewniejsze niż jedna rozmowa trwająca tydzień.

Gdy dokumentów jest więcej, niż mieści okno, model dostaje tylko potrzebne fragmenty. Służy do tego wyszukiwanie w dokumentach ([RAG](slownik/rag.html)) albo rejestr, z którego model wybiera, co przeczytać.

## Z praktyki

Strona, na której opublikowano ten słownik, powstaje w osobnych sesjach z AI: jedno zadanie, jedna sesja, jedna zmiana. Każda sesja zaczyna się od przeczytania dwóch plików. W pierwszym są zasady projektu, w drugim plan prac i historia decyzji. Po każdym zamkniętym zadaniu plan jest aktualizowany, a kolejna sesja kontynuuje tam, gdzie skończyła poprzednia, choć samych wcześniejszych rozmów model nie widzi.

Z czasem sam plik planu urósł i zajmuje już zauważalną część okna. To też praca z kontekstem: od czasu do czasu zamknięte sprawy trzeba zwijać w krótkie podsumowania, żeby zostało miejsce na bieżące zadanie.

## Co ustalić z wyprzedzeniem

Jakich zasad i decyzji model potrzebuje w każdej rozmowie i w jakim pliku są zapisane. Jak duże zadanie dzieli się na sesje i gdzie zapisuje się wynik każdej z nich. Które dokumenty przekazuje się w całości, a które przez wyszukiwanie. I kto pilnuje, żeby pliki z zasadami nie traciły aktualności: model sumiennie wykona także nieaktualną zasadę.

---

**Powiązane terminy:** [Prompt](slownik/prompt.html) · [RAG](slownik/rag.html) · [Specyfikacja AI](slownik/ai-specification.html) · [Baza wiedzy](slownik/knowledge-base.html)

Chcesz nauczyć się organizować długą pracę z AI na własnych zadaniach? [Szkolenie AI →](training.html)
