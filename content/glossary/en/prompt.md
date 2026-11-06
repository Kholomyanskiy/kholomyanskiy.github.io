---
slug: prompt
title: "Prompt: what it is and how to give AI a task"
description: "A prompt is the text used to give a language model a task. What a good prompt contains, where it falls short, and when a template or specification is needed."
published: 2026-11-07
updated: 2026-11-07
---

# Prompt

A prompt is the text a person gives a language model: a question, a task, an instruction, an example or data to process. Apart from general knowledge from training, the model knows about the task only what is written in the prompt and in earlier messages of the conversation. So the prompt decides whether the answer is useful the first time or needs several rounds of clarification.

There are user prompts, which are messages in a chat, and system prompts: standing instructions the model receives before the conversation starts. A system prompt is set by the developers of a service or by the user in the settings of a project, assistant or agent. In development tools, rule files play the same role, for example CLAUDE.md in Claude Code.

## What a good prompt contains

A good prompt describes the task the way you would describe it to a new employee who is capable but knows nothing about the company. It states the task and the goal: what needs to be done and why. It gives context: who the result is for, which documents and data to take into account, what has already been done. It sets the format: a table, an email or code, length, language. It sets limits: what must not be done and what counts as an error. If a particular style is needed, an example of a finished result helps.

Length on its own means little. A short request works when the task is simple and common. The more the result depends on the company's own rules, the more of those rules belong in the prompt.

## Prompt, template and specification

A one-off task is handled by a one-off prompt. If the same task comes up every week, the prompt is saved as a template or a standing project instruction. That way nobody types it again, and the result does not depend on who writes the request that day.

When the task is large, runs over several sessions, or the result has to be checked against rules, a single prompt is not enough. Rules, boundaries and checks move into a [specification](slownik/ai-specification.html). The model reads it at the start of every session, people use it to accept the work, and the prompt sets the current step.

## Where a prompt does not help

A prompt cannot give the model knowledge that is neither in the prompt nor in its training. If an answer must rely on company documents, they are passed to the model in full or connected through search ([RAG](slownik/rag.html)). Without that, the model fills the gap with plausible text, which is a [hallucination](slownik/hallucination.html).

The amount of text a model holds at once is limited by its [context window](slownik/context-window.html). In a long conversation, instructions from the beginning lose weight and the model gradually drifts away from them. Repeating them in every message is less reliable than keeping them in the system prompt or a rule file.

Rewording has its limits too. If the third version of a request gives the same wrong result, the cause is usually missing data or a vaguely defined task.

## From experience

With a recruitment specialist, we built a check of CVs against role criteria. When the AI got it wrong, the first impulse was to rewrite the request. Adjusting the criterion with one line in the file the check runs on proved more reliable. The request stayed the same, the file became more precise with every edit, and each fix applied to every CV after it. More in the [case description](case-recruitment.html).

With a café owner, we built an HTML enquiry form that is then embedded into a WordPress site. One or two prompts were enough: the task was small and self-contained, and the requirements for the form were clear in advance. Only the styling needed finishing, as the form drifted slightly from the site's layout. The more closely a result has to match something that already exists, the more of that existing thing is worth showing the model.

## What to decide in advance

Which tasks repeat and deserve a saved template. Where templates and instructions are kept and who updates them when the rules change. Which data may be given to the model and which may not. And by which signs the result is checked, so that the assessment does not depend on who checks it: those signs become the [acceptance criteria](slownik/acceptance-criteria.html).

---

**Related terms:** [AI specification](slownik/ai-specification.html) · [Context window](slownik/context-window.html) · [Hallucination](slownik/hallucination.html) · [AI agent](slownik/agent.html)

Want to learn to give AI tasks in your own work? [AI training →](training.html)
