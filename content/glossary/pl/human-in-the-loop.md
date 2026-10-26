---
slug: human-in-the-loop
title: "Człowiek w pętli (human-in-the-loop): rola w procesie z AI"
description: "Człowiek w pętli sprawdza, poprawia lub zatwierdza wynik AI, zanim trafi on dalej. Jakie są poziomy udziału człowieka i ile one kosztują."
published: 2026-10-26
updated: 2026-10-26
---

# Człowiek w pętli (human-in-the-loop)

Człowiek w pętli (human-in-the-loop) to uczestnik procesu, który sprawdza, poprawia lub zatwierdza wynik AI, zanim trafi on dalej. AI przygotowuje szkic, zestawienie albo propozycję, a decyzja należy do człowieka. Jego miejsce ustala się z góry: na którym kroku się włącza, co sprawdza i co robi, jeśli wynik się nie nadaje.

## Poziomy udziału

Człowiek może być w pętli na różne sposoby i od tego zależą zarówno niezawodność, jak i ekonomia.

- **Zatwierdza każdy wynik.** Nic nie idzie dalej bez jego potwierdzenia. Najbardziej niezawodny wariant i najdroższy pod względem czasu.
- **Sprawdza wyrywkowo.** Przegląda część wyników, na przykład co dziesiąty, i pilnuje, czy nie rośnie odsetek błędów.
- **Rozpatruje wyjątki.** AI samo przekazuje mu przypadki, w których zadziałała reguła: wysoka kwota, nieznany format, reklamacja.
- **Obserwuje z boku.** Proces działa samodzielnie, człowiek widzi podsumowanie i może go zatrzymać. Taki układ nazywa się czasem human-on-the-loop.

## Jak wybrać poziom

Według kosztu błędu i tego, czy da się go naprawić. Źle przypisaną wiadomość poprawia się w sekundę, odrzucenie odpowiedniego kandydata albo błędną płatność znacznie trudniej. Im droższa i mniej odwracalna decyzja, tym bliżej każdego wyniku stoi człowiek. W rekrutacji dochodzą wymogi prawne: unijny AI Act zalicza takie systemy do wysokiego ryzyka i wymaga dla nich nadzoru człowieka.

Osobne ryzyko polega na tym, że człowiek przyzwyczaja się do przytakiwania. Jeśli AI prawie zawsze ma rację, sprawdzanie zamienia się w klikanie przycisku. AI Act ma na to osobne określenie: skłonność do nadmiernego polegania na automatyzacji. Pomagają jasne kryteria sprawdzania i tyle czasu, żeby dało się wczytać w wynik.

## Jak AI samo wzywa człowieka

Człowiek nie musi wyłapywać każdego błędu sam. Rozwiązanie można zbudować tak, by AI zatrzymywało się i wzywało go w spornych i ważnych przypadkach. Takie reguły zakłada się już na etapie budowy:

- **działania nieodwracalne:** wysyłka do klienta, płatność, usunięcie danych, odrzucenie kandydata następują dopiero po potwierdzeniu;
- **progi:** kwota powyżej ustalonej, nowy dostawca, nieznany format dokumentu trafiają do człowieka;
- **porównanie ze źródłem:** jeśli wynik nie zgadza się z danymi w systemie albo dwa pola sobie przeczą, praca czeka na sprawdzenie;
- **brak danych:** zamiast zgadywać, AI zadaje pytanie doprecyzowujące;
- **warunki zatrzymania:** lista sytuacji, w których AI przerywa pracę i informuje, co się stało.

Deklaracji modelu „jestem pewien” nie można w pełni ufać, dlatego pewniej jest opierać się na zewnętrznych regułach i kontrolach. Opisuje się je w [specyfikacji](spec.html) razem z tym, do kogo trafia pytanie i jak długo może czekać na odpowiedź.

## Ile to kosztuje

Sprawdzanie przez człowieka to godziny, które liczy się w bilansie korzyści na równi z abonamentami. Jeśli sprawdzenie jednego wyniku zajmuje prawie tyle samo co ręczna praca, automatyzacja się nie zwróci. W [kalkulatorze](kalkulator.html) jest na to osobne pole: minuty weryfikacji na zadanie. Rzeczywiste minuty lepiej wziąć z pilotażu, bo na oko zwykle się je zaniża.

## Dlaczego to nie tylko koszt

Człowiek w pętli zatrzymuje wiedzę ekspercką w firmie. Widzi, gdzie AI się myli, i wie, jak pracować bez niego. To właśnie ta rezerwa, której brak tworzy [punkt awarii](slownik/failure-point.html). Stąd inne podejście do wdrożenia: AI zdejmuje z ludzi rutynę, a ludzie zostają w pętli i robią więcej. Więcej o nim w [poradniku dla menedżera](metodichka.html).

## Z praktyki

Prowadzę obecnie szkolenie dla specjalisty ds. rekrutacji. Jedno z zadań: porównywanie CV z kryteriami roli. Kryteria są zapisane w pliku, AI sprawdza według nich CV i pokazuje, kto pasuje. Decyzję, czy zaprosić kandydata, podejmuje człowiek. Jeśli AI się pomyli, kryterium doprecyzowuje się jedną linijką w pliku. Więcej w [opisie przypadku](case-recruitment.html).

Oszczędności czasu jeszcze nie policzono: klient planuje to zrobić, gdy pozostałe zadania będą gotowe. Podział ról widać już teraz. AI przygotowuje zestawienie, wybór zostaje przy człowieku.

## Co ustalić z wyprzedzeniem

Na którym kroku człowiek się włącza i jaki ma poziom udziału. Według jakich kryteriów sprawdza. Ile minut weryfikacji zakłada się w rachunku. Kto go zastępuje podczas urlopu. I co dzieje się z wynikiem, który odrzucił.

---

**Powiązane terminy:** [Punkt awarii](slownik/failure-point.html) · [Całkowity koszt posiadania](slownik/total-cost-of-ownership.html) · [Pilotaż](slownik/pilot.html) · [Kryteria odbioru](slownik/acceptance-criteria.html)

Chcesz policzyć, ile pochłonie weryfikacja przez człowieka? [Kalkulator opłacalności →](kalkulator.html)
