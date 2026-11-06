---
slug: context-window
title: "Context window: how much an AI can keep in mind"
description: "The context window sets how much text a model sees at once. What fills it, what happens when it overflows, and how to handle long tasks."
published: 2026-11-07
updated: 2026-11-07
---

# Context window

The context window is the amount of text a language model sees at once while it prepares an answer. Everything goes into it together: system instructions, uploaded files, the conversation history and the answer the model is writing right now. Whatever does not fit in the window does not exist for the model. It has no memory between conversations: every new chat starts with an empty window unless the service itself inserts saved notes.

Window size is measured in tokens. A token is a piece of a word: in English text it averages about three quarters of a word, while Russian and Polish words are split into more pieces, so the same meaning takes more tokens. Current models have windows of hundreds of thousands of tokens, some around a million. For scale, a hundred thousand tokens hold a substantial book.

## What fills the window

Space in the window runs out faster than it seems. Every question and every answer stays in the history and takes up space until the conversation ends. An attached PDF with tables and scans turns into a large amount of text. When working with code, an agent reads project files, runs commands and receives their output, and all of that accumulates in the window too.

So a conversation that began with a short question can approach the limit after a couple of hours of work, even if nobody uploaded anything large.

## What happens when the window fills up

Services behave differently. Some refuse to continue and suggest starting a new chat. Some quietly drop the oldest messages. Others compress the history into a short summary and carry on with it. In all three cases part of what was said earlier is lost or simplified, and the model may forget an agreement from the start of the conversation without saying so.

## Why a large window does not solve everything

Even when the text fits entirely, the model does not use it evenly. Research from 2023 showed that models find information at the beginning and end of a long text more reliably than in the middle. Models have improved considerably since then, but the rule remains practical: the longer the context, the higher the chance that the detail you need gets lost among everything else.

Long context is also more expensive and slower: with API access you pay per token, and each new question in a long conversation sends the whole history to the model again. Hence a simple rule: give the model what the task needs and no more.

## How to work with it

Rules and decisions needed in every conversation are kept in a file: in standing project instructions or a rule file such as CLAUDE.md in Claude Code. The model reads it at the start of each session, and nothing depends on what is left in the history. The same approach underlies an [AI specification](slownik/ai-specification.html).

A large task is split into parts, and each part is handled in its own session. At the end of a session the outcome is written to a file, and the next session starts from it. This is more reliable than a single conversation that lasts a week.

When there are more documents than the window holds, the model receives only the relevant passages. That is what document search ([RAG](slownik/rag.html)) is for, or a register the model uses to choose what to read.

## From experience

The site that hosts this glossary is built in separate sessions with AI: one task, one session, one change. Each session starts by reading two files. The first holds the project rules, the second the work plan and the history of decisions. After every completed task the plan is updated, and the next session picks up where the previous one stopped, even though the model never sees those earlier conversations.

Over time the plan file itself has grown and now takes up a noticeable part of the window. That is context work too: from time to time, finished items have to be folded into short summaries so that room stays free for the current task.

## What to decide in advance

Which rules and decisions the model needs in every conversation, and which file they live in. How a large task is split into sessions and where the outcome of each is recorded. Which documents are passed in full and which through search. And who makes sure the rule files do not go stale: the model will faithfully follow an outdated rule as well.

---

**Related terms:** [Prompt](slownik/prompt.html) · [RAG](slownik/rag.html) · [AI specification](slownik/ai-specification.html) · [Knowledge base](slownik/knowledge-base.html)

Want to learn how to organise long work with AI on your own tasks? [AI training →](training.html)
