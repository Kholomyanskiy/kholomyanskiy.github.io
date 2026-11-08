---
slug: invariant
title: "Specification invariant: a rule that must never break"
description: "An invariant in a specification is a rule a system always obeys. How to write it, how to check it, and why it matters most for an AI agent."
published: 2026-11-08
updated: 2026-11-08
---

# Specification invariant

An invariant in a specification is a rule that must hold at all times: for any task, any change and any person or agent doing the work. Records in the ledger are never deleted. A balance never changes outside a transaction. A field in an API response that clients already rely on is never renamed. Requirements describe what to build; invariants describe what must not be broken while building it.

## Where the term comes from

The word comes from mathematics and programming. There an invariant is a property that stays the same whatever happens to the system: the sum of a triangle's angles, a condition that is true at every step of a loop. In a specification the meaning is the same, applied to the system's behaviour and to the work of those who change it.

## How an invariant differs from a requirement and a principle

A requirement can be met partially, postponed or revised. An architectural principle helps choose a solution when requirements run out, and sometimes gives way to another principle. An invariant gives way to nothing. If a task requires breaking it, work stops and a person decides.

That is why a project has few invariants, usually between three and ten. When everything is declared an invariant, invariants become indistinguishable from wishes, and whoever does the work starts choosing which ones to respect.

## How it is written

In the [ANSS](anss.html) standard an invariant has four fields: a name, what is forbidden, why, and how to check it. For example, for an application that must run without installing packages: no external npm modules may be added, because the app must work without npm install, and the check is that the code contains no imports from node_modules.

The last field matters most. The check must be concrete: a database query, a constraint in the data schema, a test, a line in a diff. An invariant without a check is a good intention whose observance nobody can confirm.

## Why it matters more with AI

A person on a team hears for years what must not be touched in a system. An [AI agent](slownik/agent.html) does not know it. Whatever the task leaves out, it fills in with decisions from its training data, and under pressure to finish it may "fix" an error by removing the check that got in the way.

A written invariant gives the agent a boundary it sees before work begins, and a rule for conflicts: stop and ask. The check field lets the agent test its own output against the rule, and lets a person confirm at acceptance that the boundary is intact. That is why in an [AI specification](slownik/ai-specification.html) invariants sit in the section the agent reads first.

## From experience

In a specification for a pawnshop chain, the most important invariants came from a conversation with the business owner. An intake record cannot be saved without a photo of the item. Only the owner decides where an item goes after intake. Buying metal at a per-gram price outside the set range requires the owner's approval. Each of these rules closes a specific way an employee could abuse the system, and each has a check in code: the server rejects a request without a photo, and an item's route cannot change without the owner's confirmation. The specification is published as an example in the ANSS repository.

Every task spec for this website includes an invariants section: texts are published verbatim, files outside the list are not changed, no new styles are introduced. Their check is shared and simple: the list of changed files before the commit. If a file outside the list appears there, work stops until the owner replies.

## What to decide in advance

Which rules in the process must never be broken, even for an urgent task. How each of them is checked and who performs the check: code, a test or a person at acceptance. What the person or agent doing the work should do when a task runs into an invariant. And who may change an invariant: that is a human decision, made neither by the agent nor by a contractor mid-project. Invariant checks belong in the [acceptance criteria](slownik/acceptance-criteria.html).

---

**Related terms:** [AI specification](slownik/ai-specification.html) · [Acceptance criteria](slownik/acceptance-criteria.html) · [AI agent](slownik/agent.html) · [Failure point](slownik/failure-point.html)

Need to write down the rules that AI and contractors must not break? [AI specification →](spec.html)
