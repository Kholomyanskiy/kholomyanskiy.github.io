---
slug: total-cost-of-ownership
title: "Total cost of ownership of an AI solution: what it covers"
description: "The total cost of ownership of an AI solution covers the build, subscriptions, human review and ongoing support. What goes into it and how to estimate it."
published: 2026-10-26
updated: 2026-10-26
---

# Total cost of ownership

The total cost of ownership (TCO) of an AI solution is all the money and time it consumes over its working life: the build and setup, subscriptions and per-request model fees, staff hours spent checking results, and the support and fixes needed when the data or the model itself changes. A quote usually shows only the first item. The rest turn up after launch and, over time, can cost more than the build.

## What it is made of

- **Build and setup.** Developing the solution, connecting it to your systems, testing, a [pilot](slownik/pilot.html).
- **Subscriptions and requests.** A service plan or a fee for every request to the model. Spending grows with the number of documents and the length of requests.
- **Human review.** The time of the employee who [checks the output](slownik/human-in-the-loop.html), corrects it and approves it. If every answer has to be checked, this can become the largest line.
- **Support.** A supplier sends a price list in a new format, a document template changes, a new model version comes out and the solution starts answering differently. Each of these costs developer hours.
- **Errors.** What a missed AI error costs and who fixes it.
- **Training and exit.** The time it takes for people to start using the tool, and the cost of walking away: moving data out, going back to manual work.

## Why support gets forgotten

The build is easy to price: there is a task, a deadline and a figure. Support is spread over time and is invisible at the moment of decision. With AI solutions it tends to be more noticeable than with ordinary software. The model is updated by its vendor, and after an update the same requests can produce different answers. In a small business, input data is rarely uniform: ten suppliers send price lists in ten different ways.

So the yearly cost of the solution is compared with what the current manual process costs over the same year. The build price on its own has nothing to be compared with.

## How to estimate it in advance

Take a one-year horizon. Add up the build, the monthly fees, and the hours for review and support. Review hours are best taken from the pilot, since estimates by eye tend to be optimistic. Then compare with current costs: how many hours a month the same work takes today and what an hour costs. The [calculator](kalkulator.html) has fields for human review minutes, processing cost, subscriptions, implementation and monthly support. It does not cover staff training or non-standard cases, so those need to be added on top. If it is unclear which steps are worth automating in the first place, start with a [process audit](slownik/process-audit.html).

## From experience

I was building product card automation for an online store: descriptions and import files were to be generated from supplier price lists. The price lists came in roughly ten different shapes, and the client doubted they could be parsed reliably. I suggested creating a single price list template and asking suppliers to fill it in, but the conversation with suppliers never happened. In my estimate, full automation of this work was not possible. About 60% was, and some small operations could reach 80–90%. The client wanted all or nothing, the build price seemed high to him, and after the first working version the project was stopped.

A total cost of ownership calculation would have answered the question left open at the time: does that 60% pay off? That takes knowing what the current manual work costs and how many hours will remain for corrections. Without those figures, a partial result is easy to mistake for an unfinished one. There is another side too. Some business owners are not ready to hand AI even the work it can handle, although the need is there and so are the attempts. That is normal, and it is also better found out before work begins.

## What to decide in advance

Over what period to compare costs and benefits. In the first months a solution usually looks unprofitable because of the build cost, while support and fixes accumulate gradually, so they only become visible over a year or longer. Who will support the solution after launch and how many hours a month you set aside for it. How many answers a person checks: all of them or a sample. Whether partial automation is acceptable to you and at what share it starts to pay off. What happens if the solution has to be switched off after six months.

---

**Related terms:** [Human in the loop](slownik/human-in-the-loop.html) · [Pilot](slownik/pilot.html) · [Process audit](slownik/process-audit.html) · [Failure point](slownik/failure-point.html)

Want to check whether automation will pay off? [Automation payback calculator →](kalkulator.html)
