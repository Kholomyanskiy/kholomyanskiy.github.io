---
slug: failure-point
title: "Failure point when implementing AI: how to find it"
description: "A failure point appears when, after automation, no one is left to restore the system or do the work by hand. Where to look for it and how to measure it early."
published: 2026-10-26
updated: 2026-10-26
---

# Failure point

A failure point is an element of a system whose failure stops the whole process. In AI implementation, it is often a part of the work that has no human backup left: if the system fails, no one can restore it or do the work by hand. The usual path there looks like this. AI takes routine work off people, people are let go, and with them goes the ability to maintain, administer and work around the system.

## Where the term comes from

It comes from engineering and IT, where people more often speak of a single point of failure. That can be one server with no backup, one network link, one specialist who knows how everything works. People in this role have long been accounted for too: software teams talk about the "bus factor", the number of people whose departure would stall a project. In AI implementation, a failure point most often appears where no one is left who can stand in for the automation when it stops working.

Errors the model makes on individual steps are a neighbouring topic. They are caught by checking the output, with a [human in the loop](slownik/human-in-the-loop.html) and [acceptance criteria](slownik/acceptance-criteria.html). A failure point answers a different question: what happens when the automation does not work at all.

## Why it appears

People in an area being automated usually have a function that is missing from their job description: they know how to keep working when the system is down. Automation holds as long as the model, the service, the integration and the paid subscription all work. A failure in any of these links hands the work back to people. If those people are gone, the work waits until someone is found and trained.

In that situation, the decision to cut staff is made on the hours saved. The hours needed for recovery usually stay out of the calculation, because there has been no failure yet.

## Where to look

The easiest place is a [process map](slownik/process-map.html). Watch the areas where cuts are planned because of automation. Functions that only one person knows. Maintenance, administration and system support. Steps with no manual path. And external dependencies: the model provider, integrations, the vendor's pricing.

## How to measure it

For each area, four values are estimated:

- **acceptable downtime:** how long the area can be down without serious harm: an hour, a day, a week;
- **recovery time:** how long it takes to get work going again after a failure, with the people who remain;
- **backup:** how many people can restore the system or do the work by hand;
- **cost of downtime:** what an hour or a day of stoppage costs.

If recovery time is longer than acceptable downtime, the area is a failure point. Then a response is chosen: keep people, train those who stay, sign a support contract, preserve a manual path. Decisions about the size of a department make sense after this calculation, during a [process audit](slownik/process-audit.html). The chosen option, together with the manual path and what to do when something fails, goes into the solution's [specification](spec.html).

## From experience

For more than ten years I worked in IT in the energy sector. There is a rule there called N-1: a system must withstand the failure of any single element. It is checked in advance, on the diagram, before any outage. When AI is built into a process, I ask the same question: what happens if this element fails, and who takes over the work then.

When no one asks that question, this is what usually happens. A company decides that AI now writes the reports and lets some of its system administrators go. The reports get written. A few months later the network goes down, and no one is left to bring it back. The model made no mistake. What failed was an area with no backup left.

## What to decide in advance

Who restores the system if it fails at night or over a weekend. Whether there is a manual path, and who among the remaining staff knows how to use it. What to do if the model provider changes its terms or the service is unavailable for several days. And whom to let go: that question is settled after the failure points have been counted.

---

**Related terms:** [Process audit](slownik/process-audit.html) · [Process map](slownik/process-map.html) · [Human in the loop](slownik/human-in-the-loop.html) · [Total cost of ownership](slownik/total-cost-of-ownership.html)

Planning to reshape a department around AI? [AI audit for a department →](audit.html)
