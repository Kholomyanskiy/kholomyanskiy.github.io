---
slug: human-in-the-loop
title: "Human in the loop: the person's role in an AI process"
description: "A human in the loop checks, corrects or approves AI output before it moves on. What levels of involvement exist and what each of them costs."
published: 2026-10-26
updated: 2026-10-26
---

# Human in the loop

A human in the loop is a participant in a process who checks, corrects or approves AI output before it moves on. The AI prepares a draft, a shortlist or a proposal, and the decision stays with the person. Their place is set in advance: at which step they come in, what they check, and what they do if the output is not good enough.

## Levels of involvement

A person can be in the loop in different ways, and both reliability and economics depend on which one.

- **Approves every output.** Nothing moves on without their confirmation. The most reliable option and the most expensive in time.
- **Checks a sample.** Looks at part of the output, say every tenth item, and watches whether the error rate is rising.
- **Handles exceptions.** The AI itself passes on cases where a rule was triggered: a large amount, an unfamiliar format, a complaint.
- **Watches from the side.** The process runs on its own, the person sees a summary and can stop it. This setup is sometimes called human on the loop.

## How to choose the level

By the cost of an error and whether it can be undone. A misfiled email takes a second to fix; rejecting a suitable candidate or sending a wrong payment is much harder to reverse. The more expensive and irreversible the decision, the closer the person stands to every output. Recruitment also comes with legal requirements: the EU AI Act classifies such systems as high-risk and requires human oversight for them.

A separate danger is that the person gets used to agreeing. If the AI is almost always right, checking turns into clicking a button. The AI Act has its own term for this: automation bias. Clear review criteria help, and so does enough time to actually read the output.

## How the AI calls in a person

The person does not have to catch every error alone. A solution can be built so that the AI stops and calls them in disputed or important cases. These rules are set during development:

- **irreversible actions:** sending to a client, paying, deleting, rejecting a candidate happen only after confirmation;
- **thresholds:** an amount above a set limit, a new supplier, an unfamiliar document format go to a person;
- **checking against the source:** if the output contradicts data in the system, or two fields contradict each other, work stops until someone checks;
- **missing data:** instead of guessing, the AI asks a clarifying question;
- **stop conditions:** a list of situations in which the AI halts and reports what happened.

A model's own "I'm confident" cannot be fully trusted, so external rules and checks are a safer basis. They are described in the [specification](spec.html), together with who receives the question and how long it can wait for an answer.

## What it costs

Human review takes hours, and they count against the benefit just like subscriptions do. If checking one output takes almost as long as doing the work by hand, the automation will not pay off. The [calculator](kalkulator.html) has a separate field for this: review minutes per task. Real minutes are best taken from the pilot, since estimates by eye usually come out too low.

## Why it is more than a cost

A human in the loop keeps expertise inside the company. They see where the AI goes wrong and know how to work without it. This is the backup whose absence creates a [failure point](slownik/failure-point.html). It also suggests a different approach to implementation: AI takes routine work off people, and the people stay in the loop and get more done. The [manager's guide](metodichka.html) covers this approach in more detail.

## From experience

I am currently training a recruitment specialist. One of the tasks is checking CVs against role criteria. The criteria are kept in a file, the AI checks CVs against them and shows who fits. The decision to invite a candidate is made by the person. When the AI gets it wrong, the criterion is refined with one line in the file. More in the [case description](case-recruitment.html).

Time savings have not been measured yet: the client plans to do that once the remaining tasks are ready. The division of roles is already clear. The AI prepares the shortlist, and the choice stays with the person.

## What to decide in advance

At which step the person comes in and at what level of involvement. What criteria they check against. How many review minutes go into the calculation. Who covers for them during holidays. And what happens to an output they reject.

---

**Related terms:** [Failure point](slownik/failure-point.html) · [Total cost of ownership](slownik/total-cost-of-ownership.html) · [Pilot](slownik/pilot.html) · [Acceptance criteria](slownik/acceptance-criteria.html)

Want to see how much human review will cost? [Automation payback calculator →](kalkulator.html)
