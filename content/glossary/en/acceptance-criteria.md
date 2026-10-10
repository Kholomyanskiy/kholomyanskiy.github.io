---
slug: acceptance-criteria
title: "AI solution acceptance criteria: what they are and how to write them"
description: "Acceptance criteria define how you decide that work is complete. What makes a good criterion, why AI makes this harder, and what to decide before work begins."
---

# Acceptance criteria

Acceptance criteria are verifiable conditions used to decide whether work is complete. They are written before work begins so the client and contractor interpret them the same way and can check the result without a dispute.

## What makes a good criterion

“The bot answers customers” is not a criterion: it could describe any bot, including one that gives irrelevant answers. “The bot answers questions from an approved list and passes all other questions to a manager within one minute” is a criterion. It can be checked, and once it has been checked there is no room for dispute.

A usable criterion has four features. It is verifiable: you can answer “yes” or “no,” or measure it. It is checked against your data, with all their quirks. It has a threshold below which the work is not accepted. And it is clear in advance who checks it and how. It is useful to write each criterion in one sentence: what is being checked, against which data, by what method, and what result is sufficient. For example: “The invoice amount and number are extracted correctly from every document in the test set, as checked by the accountant against the originals.”

## Why AI makes this harder

Conventional software gives the same answer to the same data. A model may answer differently, and any demo looks great on three successful examples. That is why an AI criterion almost always describes a proportion: how many documents in the test set have a correct result, and how many errors are allowed.

Errors are not all equal either. A typo in a comment and an incorrect invoice amount have different consequences, and that needs to be written down too. Sometimes the acceptable error rate for one field is zero, while another can tolerate some errors if those cases go to a [human in the loop](slownik/human-in-the-loop.html).

One more thing: tie the criterion to the work outcome. Model quality alone is not enough. A model may recognize almost everything correctly, while the employee's time per task stays the same because they still check every document.

## Common mistakes

The brief says “user-friendly interface” and “high recognition quality,” the contractor delivers whatever they have built, and there is nothing concrete to dispute. Criteria are written after delivery and adjusted to fit the result. The contractor writes the criteria and, naturally, lists only what they can certainly deliver. People check whether features exist without checking whether those features solve the problem.

Both sides suffer when criteria are missing. The contractor cannot finish the work either: the result was never defined in advance, so it is always “not quite right,” and revisions go round in circles. This is rare in large companies with formal acceptance processes, and more common with individual clients and small businesses. Criteria protect the client from work done by guesswork and the contractor from a project that cannot be completed.

## From experience

I have not had acceptance disputes in my projects. I do have a story about not writing down what success meant. We set up incoming email sorting, which I wrote about in the article on [process audits](slownik/process-audit.html), without recording how many hours a day it should save or what share of emails could land in the wrong folder. So we still cannot answer whether the work paid off.

## What to decide before work begins

A set of test examples from your real data, including the awkward ones. What counts as an error and which errors are critical. A threshold for each criterion. How the work is done now, so you have a baseline to compare against; a [pilot](slownik/pilot.html) is a useful way to establish one. Who accepts the work and what happens if it fails.

All of this belongs in the [AI specification](slownik/ai-specification.html). Criteria without a specification check an undefined target. A specification without criteria gives you no way to check the result.

---

**Related terms:** [AI specification](slownik/ai-specification.html) · [Pilot](slownik/pilot.html) · [Human in the loop](slownik/human-in-the-loop.html) · [Hallucination](slownik/hallucination.html)

Can you check that the contractor delivered what you are paying for? [AI specification →](spec.html)
