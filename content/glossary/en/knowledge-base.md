---
slug: knowledge-base
title: "Knowledge base for AI: how to build one AI answers from"
description: "A knowledge base for AI is a verified set of company rules and answers that a model relies on. How it differs from a folder of files and who maintains it."
published: 2026-11-08
updated: 2026-11-08
---

# Knowledge base for AI

A knowledge base is a collected and verified set of what a company knows about its own work: procedures, instructions, answers to frequent questions, product descriptions, customer terms. For AI, a knowledge base is the source the model answers from instead of the general knowledge it gained in training. Whatever is in the base, the model can find and quote. Whatever is missing does not exist for the model, and it will fill the gap with a plausible guess.

## How a knowledge base differs from a folder of files

A folder of documents on a shared drive is not a knowledge base by itself. Current versions sit next to old ones, drafts next to signed documents, and only a long-serving employee knows which file to trust. The model does not know that.

A knowledge base differs in three ways. It holds only current versions, with old ones removed or clearly marked. Every document has a date and a scope: which department, country or product it applies to. And the base has an owner who is responsible for keeping its content in line with how the company works today.

## How AI uses a knowledge base

A small base of a few dozen pages fits into the [context window](slownik/context-window.html) in full: it is loaded into a project or the assistant's standing instructions, and the model sees all of it at once. A large base cannot be passed in whole, so search is connected to it, finding the relevant passages for each question ([RAG](slownik/rag.html)).

In both cases the quality of answers is limited by the quality of the base. Search will find an outdated procedure as confidently as a current one, and the model will retell it smoothly, with a reference.

## What makes a base usable for AI

One document answers one question or covers one topic, and its title says what it is about. Conditions are written out explicitly, with dates and exceptions, without references like "as usual". The same thing is called the same everywhere, otherwise search will not connect "return" in one document with "complaint" in another. Documents are stored as text: scans and photos go through [document recognition](slownik/document-recognition.html) first, and its output is worth checking.

The hardest part is that much of a company's knowledge is not written down anywhere. It lives in experienced employees' heads, in correspondence and in a department's habits. Such places are found during a [process audit](slownik/process-audit.html), and writing that knowledge down usually takes longer than the technical setup.

## Who maintains it

A knowledge base needs an owner with a clear duty: when a rule changes, the document in the base changes too. It also needs a review routine, for example once a quarter, using a list of documents with the date each was last checked. An outdated base does more harm than an empty one: an empty base honestly gives no answer, an outdated one gives a wrong answer with a reference to the source.

## How it usually goes

A company decides to build an assistant that answers employees' questions about internal rules. Everything on the drive is collected and uploaded. The first tests show the assistant handles simple questions well and the questions it was built for badly: how to process an exception, whom to call when something breaks, what to do with an unusual customer.

The answers to those questions are simply not in the documents. Two or three people know them, and newcomers ask them every time. The project turns into work on writing that knowledge down, and the assistant starts to be useful once that is done. Along the way the company gains something it did not have before: rules that will not leave with an employee.

## What to decide in advance

Which questions the base must answer and who asks them: employees, customers or both. Which documents count as current and what to do with old versions. Who owns the base and how often they review it. Whose knowledge currently exists only in their head and who will write it down. And how answers are checked before launch: a set of questions with known answers that the assistant is run through after every major update of the base.

---

**Related terms:** [RAG](slownik/rag.html) · [Context window](slownik/context-window.html) · [Document recognition](slownik/document-recognition.html) · [Process audit](slownik/process-audit.html)

Want to find out which knowledge in your department exists only in people's heads? [AI audit for a department →](audit.html)
