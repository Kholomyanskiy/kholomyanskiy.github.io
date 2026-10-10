---
slug: pilot
title: "AI implementation pilot: what it is and how to avoid wasting the budget"
description: "A pilot tests an AI solution with your data and people before full implementation. Why it matters, what can go wrong, and what to decide first."
---

# Pilot

A pilot is a time-limited, small-scale launch of a solution using real data and real people, with success criteria written down in advance. Its results help decide whether to continue implementation, make changes, or stop.

## Why run a pilot

A demo can show that the technology works in principle. A pilot checks whether it works for you: with your documents, scans, and handwritten notes in the margins; with your people, their habits, and their workarounds; in your process, where someone has to accept, check, and pass on the model's output.

A good pilot answers three questions. Is there enough data? What changes in people's work? How much will it cost after the pilot, when the solution has to be maintained?

## What a pilot without criteria looks like

A bot runs for a month. A month later, people say “it seems to work, people like it,” and the purchase decision is based on impressions. The pilot uses twenty clean documents, while the real work involves scans, handwritten notes, and spreadsheets in three formats. The pilot has no end date, so it is endlessly tweaked and quietly becomes a permanent system no one decided to adopt. Or the wrong thing is measured: the model is almost always right, but the employee's time per task has not changed.

In every case, money has been spent and no decision has been made. A failed pilot at least gives you an answer. The most expensive pilot is one that leaves you unsure what to do.

## From experience

A large infrastructure company decided to buy a system one of its executives had seen at an industry expo: an operator could see the whole territory on screen, faults would be marked automatically from customer reports, and the system would predict which equipment was likely to fail based on previous years' records. It worked for the customer whose case was being demonstrated.

They ran a pilot in one department, and even that was expensive. It showed that the system depended on two things they did not have: detailed maps of remote areas and equipment data that no one had maintained for years. The forecasts never worked as intended. The pilot found the gaps, but no decision followed because no one had recorded in advance what counted as success. The system was modified and later rolled out further, without the feature it had been bought for. There was no AI involved. The mechanics were the same.

## What to decide before launch

Which part to include: one workflow from the [process map](slownik/process-map.html) where the effect can be measured and a model error can be caught before it becomes costly. A pilot covering an entire department can itself cost as much as a small implementation. How the work is done now: time, error count, and volume, so there is something to compare against. Which [criteria](slownik/acceptance-criteria.html) define a successful pilot, what their thresholds are, and which data will be used to check them. How long it runs. Who makes the final decision and which of three options they can choose: expand, revise, or close.

Also decide where a [human in the loop](slownik/human-in-the-loop.html) remains during the pilot and what happens if the model makes a mistake. The [failure points](slownik/failure-point.html) make this clear.

## What comes next

If the pilot succeeds, calculate the [total cost of ownership](slownik/total-cost-of-ownership.html): maintenance, updates, and people's time spent checking. A pilot often looks cheap because enthusiasts keep it running. There are not enough enthusiasts for an entire department.

---

**Related terms:** [Process audit](slownik/process-audit.html) · [Acceptance criteria](slownik/acceptance-criteria.html) · [Total cost of ownership](slownik/total-cost-of-ownership.html) · [Failure point](slownik/failure-point.html)

Planning a pilot? First define the question it should answer. [Services →](services.html)
