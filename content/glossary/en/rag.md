---
slug: rag
title: "RAG: how AI answers from your company documents"
description: "RAG lets AI answer questions from your company documents and cite the source. How it works, where it goes wrong, and what to decide before launch."
published: 2026-10-26
updated: 2026-10-26
---

# RAG (search over your own documents)

Retrieval-augmented generation (RAG) is an approach in which a language model first searches a defined set of documents for relevant passages and then writes its answer based on them. The approach was described by researchers at Facebook AI in 2020. Today the term covers almost any "chat with our documents" system. In a small business, RAG usually serves one purpose: an employee or a customer asks a question in plain words and gets an answer drawn from the company's policies, contracts, price lists or manuals, with a link to the document.

## How it works

Documents are split into passages in advance and indexed so that search can find them by the meaning of a question, even when the words do not match. For each question, the system picks a few of the best-matching passages and passes them to the model. The model answers from them and, if configured to, cites the source.

The model does not memorise the documents. It sees only what the search found for that particular question. So the quality of an answer depends on two things at once: whether the right passage made it into the results, and whether the model read it correctly.

## Where RAG goes wrong

Most often it is the search that fails. It finds an outdated version of a policy, or a similar document about something else. It brings back half the answer while the other half sits in the next file. It misses tables and scans that were not recognised properly. And sometimes the documents simply do not contain the answer, and the model answers anyway, confidently and plausibly.

A source link reduces the risk: a person can open the document and check. Where an answer affects money or commitments to a customer, the check usually stays with a [human in the loop](slownik/human-in-the-loop.html).

## RAG, database or registry

The name RAG describes a pattern, "find first, then answer", and there are many ways to do the finding. Vector search over chopped-up passages is only one of them, just the best known.

If there are only a few documents and they fit into the model's [context window](slownik/context-window.html), they are passed in whole and no search is needed at all. Structured data (amounts, dates, customers, statuses) belongs in an ordinary database that the model queries. Vector search will not count the contracts expiring in December: it looks for similar text, and counting is beyond it.

When there are hundreds of documents and a question usually points to a specific one, a registry with a short description of each is often enough. The model picks a document from the registry and reads it in full. Classic RAG with vector search fits where there is a lot of continuous text, questions are about meaning, and nobody knows in advance where the answer lives.

In practice these approaches are combined. Documents get metadata (customer, type, date), which narrows the scope first, and search by meaning then runs inside that scope. It makes sense to start with the simplest option that handles the typical questions: a registry is easier to maintain, and it shows where an answer came from.

## How to test before launch

Before launch, it helps to set out in the [specification](slownik/ai-specification.html) which questions the system answers and what it says when the documents have no answer. A set of control questions with known answers becomes the basis for [acceptance criteria](slownik/acceptance-criteria.html). Testing works best in a [pilot](slownik/pilot.html), with the people who will be asking questions every day.

## How it usually goes

A company uploads a folder of contracts and policies covering several years. It holds current versions, old revisions and drafts named "final_2". At first the answers look convincing, complete with links to documents. Then someone notices the bot quoting terms from a contract that was re-signed long ago, and the link leads to the old version.

The model did exactly what was expected of it: it answered from the passage the search found. The mistake happened earlier, when someone decided what to upload and who keeps track of versions.

## What to decide in advance

Which documents go in, and who makes sure the system holds the current versions. Who will ask questions, and what kind. What the system says when the documents have no answer. Who checks the answers, and how often. And how people will be told what is inside and how to use it: without that explanation, even a system that works looks broken.

---

**Related terms:** [Knowledge base](slownik/knowledge-base.html) · [Hallucination](slownik/hallucination.html) · [Document recognition](slownik/document-recognition.html) · [AI specification](slownik/ai-specification.html)

Want AI to answer from your company's documents? [AI Solution Design →](solution-design.html)
