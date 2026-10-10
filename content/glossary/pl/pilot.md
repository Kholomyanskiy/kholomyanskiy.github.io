---
slug: pilot
title: "Pilotaż wdrożenia AI: czym jest i jak nie zmarnować budżetu"
description: "Pilotaż sprawdza rozwiązanie AI na twoich danych i z udziałem twoich ludzi przed pełnym wdrożeniem. Po co go robić, jak uniknąć błędów i co ustalić."
---

# Pilotaż

Pilotaż to ograniczone czasowo i zakresem uruchomienie rozwiązania na prawdziwych danych i z udziałem prawdziwych użytkowników, z kryteriami sukcesu zapisanymi z góry. Na podstawie jego wyników podejmuje się decyzję o dalszym wdrożeniu, poprawkach albo zakończeniu.

## Po co robić pilotaż

Demo pokazuje, że technologia w ogóle działa. Pilotaż sprawdza, czy działa u ciebie: na twoich dokumentach, skanach i odręcznych notatkach na marginesach; z twoimi ludźmi, ich nawykami i obejściami; w twoim procesie, gdzie ktoś musi zaakceptować, sprawdzić i przekazać dalej wynik modelu.

Dobrze zaplanowany pilotaż odpowiada na trzy pytania. Czy jest wystarczająco dużo danych? Co zmieni się w pracy ludzi? Ile to będzie kosztować po zakończeniu pilotażu, gdy rozwiązanie trzeba będzie utrzymywać?

## Jak wygląda pilotaż bez kryteriów

Bot działa przez miesiąc, a po miesiącu słyszymy: „chyba działa, ludziom się podoba”; decyzję o zakupie podejmuje się na wyczucie. Pilotaż przeprowadza się na dwudziestu czystych dokumentach, a w codziennej pracy są skany, odręczne notatki i arkusze w trzech formatach. Pilotaż nie ma daty końcowej, więc rozwiązanie jest bez końca dopracowywane i po cichu staje się stałym systemem, którego nikt nie zdecydował się wdrożyć. Albo mierzy się niewłaściwą rzecz: model prawie zawsze odpowiada poprawnie, ale czas pracownika na zadanie się nie zmienił.

W każdym przypadku pieniądze zostały wydane, a decyzji nie ma. Nieudany pilotaż przynajmniej daje jasną odpowiedź. Najwięcej kosztuje pilotaż, po którym nie wiadomo, co robić.

## Z praktyki

Duża firma infrastrukturalna postanowiła kupić system, który jeden z jej dyrektorów zobaczył na targach branżowych: operator widział na ekranie cały obszar, usterki miały być automatycznie oznaczane na podstawie zgłoszeń klientów, a system przewidywał z danych z poprzednich lat, które urządzenia wkrótce się zepsują. U klienta, na którym pokazywano rozwiązanie, wszystko działało.

Przeprowadzono pilotaż w jednym dziale i nawet on okazał się kosztowny. Wtedy wyszło na jaw, że system zależał od dwóch rzeczy, których brakowało: szczegółowych map odległych terenów i danych o urządzeniach, których nikt nie prowadził od lat. Prognozy nie zaczęły działać tak, jak powinny. Pilotaż wykrył braki, ale nie podjęto na jego podstawie decyzji, bo wcześniej nikt nie zapisał, co oznacza sukces. System poprawiano, a później wdrożono szerzej, już bez tej części, dla której go kupiono. Nie było tam AI. Mechanizm był taki sam.

## Co ustalić przed uruchomieniem

Jaki zakres wybrać: jeden łańcuch zadań z [mapy procesów](slownik/process-map.html), w którym można zmierzyć efekt i zauważyć błąd modelu, zanim stanie się kosztowny. Pilotaż obejmujący cały dział może kosztować tyle, co małe wdrożenie. Jak praca przebiega teraz: ile trwa, ile jest błędów i jaka jest jej skala, żeby było z czym porównać wynik. Jakie [kryteria](slownik/acceptance-criteria.html) oznaczają sukces pilotażu, jakie mają progi i na jakich danych będą sprawdzane. Jak długo potrwa pilotaż. Kto podejmie końcową decyzję i jakie są trzy możliwości: rozszerzamy, poprawiamy albo kończymy.

Osobno ustal, gdzie podczas pilotażu pozostaje [człowiek w pętli](slownik/human-in-the-loop.html) i co się stanie, jeśli model popełni błąd. Widać to w [punktach awarii](slownik/failure-point.html).

## Co dalej

Jeśli pilotaż się powiedzie, oblicza się [całkowity koszt posiadania](slownik/total-cost-of-ownership.html): utrzymanie, aktualizacje i czas ludzi poświęcony na sprawdzanie wyników. Pilotaż często wygląda tanio, bo obsługują go entuzjaści. Nie wystarczy ich na cały dział.

---

**Powiązane terminy:** [Audyt procesów](slownik/process-audit.html) · [Kryteria odbioru](slownik/acceptance-criteria.html) · [Całkowity koszt posiadania](slownik/total-cost-of-ownership.html) · [Punkt awarii](slownik/failure-point.html)

Planujesz pilotaż? Najpierw określ, na jakie pytanie ma odpowiedzieć. [Usługi →](services.html)
