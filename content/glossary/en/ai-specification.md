---
slug: ai-specification
title: "AI specification: what it is and how it differs from a prompt"
description: "An AI specification describes a task so a model can perform it predictably and its output can be checked. What it contains and why it matters."
---

# AI specification

An AI specification is a document that describes a task so a model or agent can perform it predictably and its output can be checked: what goes in, what comes out, which rules must not be broken, and how to tell when the work is done. It lives outside the chat and remains available across sessions.

## How a specification differs from a prompt

A [prompt](slownik/prompt.html) is an instruction or request in a conversation. It usually handles a specific task and remains part of that session. The model reads the specification at the start of each session; it is updated when the rules change and is also used later to check the work. A good prompt produces one good answer. A specification makes the whole body of work predictable.

For developers, this discipline is kept by the engineering environment: tasks in a tracker, code reviews, and tests. A manager or small company without an engineering department has no such environment, so a specification page fills that role.

## What it contains

- Goal and output: what should be produced and in what form.
- Input: what data is used, where it comes from, and what state it is in.
- Constraints: what must not be changed or broken. Specifications call these [invariants](slownik/invariant.html).
- [Acceptance criteria](slownik/acceptance-criteria.html): how to check that the work is done.
- Decisions already made, so the model does not revisit them in every session.

For one task, all of this often fits on a page.

## When a regular task brief is not enough

People usually brief a model as if it were a colleague who knows everything. The model knows less than a colleague and does not ask follow-up questions; it fills in the gaps. The result looks plausible but does the wrong thing. Revisions then go round in circles: fix one thing, break the next. There are so many joke videos about this online that they have become a genre. Funny because it is true.

The second reason lies in how models work. They have a limited [context window](slownik/context-window.html): the more documents, messages, and new instructions a session contains, the harder it is for the model to retain earlier agreements. A conversational task brief usually stays in one specific chat. A specification lives separately and can be given to the model again.

## From experience

Before I started writing specifications, I briefed models the way everyone does: conversationally, as we went. By about the fifth to tenth answer, things became muddled. The model forgot decisions, rewrote things that were off limits, and got confused by long documents. This happened in almost every project, with every agent.

That experience led to [ANSS](anss.html), an open specification standard for working with AI. In my projects, the quality of results improved noticeably after I adopted it. It is not perfect, just as models are not perfect, but the approach works and I use it in my work.

Even this glossary is written this way. When a chat accumulates too many versions, we consolidate all decisions into one file and start a new session from it.

## What to decide before work begins

Who writes the specification: the client, the contractor, or both, and who approves it. Where it lives and who updates it when the rules change. How detailed it needs to be: one page is enough for a single task, while a chain of agents handing work to one another needs a standard such as ANSS.

---

**Related terms:** [Acceptance criteria](slownik/acceptance-criteria.html) · [Invariant](slownik/invariant.html) · [Prompt](slownik/prompt.html) · [Context window](slownik/context-window.html)

Need to describe a task for AI or a contractor on one page? [Specification →](spec.html)
