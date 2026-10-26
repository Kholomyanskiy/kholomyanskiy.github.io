---
slug: agent
title: "AI agent: how it differs from a bot and when you need one"
description: "An AI agent chooses its own steps and tools to reach a goal. How it differs from a bot, a script and RPA, and when simple automation is enough."
published: 2026-10-26
updated: 2026-10-26
---

# AI agent

An AI agent today usually means a system built on a language model that directs its own work: it receives a goal, chooses steps and tools, carries out actions and decides what to do next based on their results. Tools can include email, a spreadsheet, an accounting system, search across documents. A bot follows a script written in advance. An agent builds its script as it goes, within the limits of what it is allowed to do.

The word also has a broader meaning. In classical AI theory, an agent is any system that perceives its environment and acts in it. In marketing, on the other hand, "agent" often labels an ordinary chatbot or a chain with a single model call. So when someone offers you an "agent", it is worth asking what the AI will actually decide on its own.

## The automation ladder

Agents grew out of several generations of automation, and every one of them still works. It helps to see the whole ladder, because a client's task can almost always be solved on one of its rungs.

- **Formulas and spreadsheets.** Excel and similar tools calculate by formula: totals, balances, summary reports. A person sets the rules; the spreadsheet only calculates.
- **Scripts and macros.** Code in VBA, Python or PHP carries out a sequence of actions: renaming files, sorting emails by subject, exporting a report. It does exactly what is written.
- **Bots and RPA.** A robot repeats a person's actions in an interface: opens a system, copies fields, clicks buttons. A chatbot answers from a script or by keywords. One step off the script, and the bot stops or gets it wrong.
- **Automation platforms.** Services such as Zapier, Make or n8n let you assemble such chains without a programmer: an email arrives, the data goes into a spreadsheet, a manager gets a notification.
- **AI in a single step.** A language model is inserted into a fixed chain for one action: understanding what an email is about, pulling fields from an invoice, drafting a reply. The script is still set in advance. Developers call such chains workflows, as distinct from agents.
- **Agent.** The model decides what to do next: which tool to call, what to check, when to stop and ask a person.

The higher the rung, the more tasks it covers and the less predictable it becomes.

## How an agent differs from a bot

A bot knows what to do because it is written in the script. An agent knows what needs to be achieved and chooses its actions itself. That leads to practical differences.

- **Non-standard input.** A bot breaks on an email that does not fit the rule. An agent can read it and deal with it.
- **Several steps.** An agent can gather data from three systems, compare it and prepare a summary without a ready-made instruction for that case.
- **Predictability.** Given the same input, a bot produces the same output. An agent may solve the same task differently twice, and sometimes be confidently wrong: models are prone to [hallucinations](slownik/hallucination.html).

## Degrees of autonomy

Agents differ in how much they are allowed to do.

- **Suggests.** Prepares a draft or an option; a person does the rest.
- **Acts with confirmation.** Carries out steps itself but asks for permission before important actions.
- **Acts alone.** Works without human involvement within set rules; a person sees a report.

The more expensive an error, the lower the autonomy and the closer the [human in the loop](slownik/human-in-the-loop.html).

## When you don't need an agent

Agents are often offered where lower rungs would do. If a task can be described by a rule, the rule is more reliable. Emails with a particular subject can be sorted by a mail filter. A report in a fixed format can be assembled by a script. Money, taxes, stock levels and documents full of figures are best calculated by an ordinary formula: it does not make things up, and it is not wrong in a different way every day.

A simple solution is cheaper, easier to check and maintain, and has fewer reasons to break. An agent adds fees for model requests, time spent reviewing its work, and unpredictability that has to be contained by rules. All of this belongs in the [total cost of ownership](slownik/total-cost-of-ownership.html).

A good setup is often mixed. The agent goes through the incoming flow, works out what has arrived and chooses an action. Calculations are done by a calculator or a script that the agent calls as a tool. The model decides what to do; the code does the maths.

## When an agent makes sense

Where the input varies and does not fit into rules: free-text emails, documents in different formats, customer questions. Where a task takes several steps across different systems, and the order of steps depends on what turns up along the way. And where the cost of a single error is small or a check catches it.

## From experience

In a project with a recruitment agency, CVs cannot be sent to a cloud model as they are. Personal data is removed by a script following fixed rules: which fields to delete and what to replace them with. There is nothing for an agent to decide here, and a mistake would be costly, so the simplest rung of the ladder does the job. The language model comes in later, when the anonymised CV is checked against the role criteria.

Product card automation for an online store had a similar split. Part of the data in supplier price lists matched the store's fields, and it is simpler and more reliable to move it with a script. The model is needed where a description has to be written from sparse data. When the two parts are mixed and everything is handed to AI at once, both the cost and the number of errors go up, in places where there need not have been any errors at all.

## What to decide in advance

Whether the task can be described by a rule. If it can, start with the rule. What the agent may do on its own and where it must ask. Which tools it needs and which calculations it hands over to code. Who checks its work and how often. And how you will know that the agent performs worse than a simple solution that could replace it.

---

**Related terms:** [Human in the loop](slownik/human-in-the-loop.html) · [Hallucination](slownik/hallucination.html) · [Total cost of ownership](slownik/total-cost-of-ownership.html) · [RAG](slownik/rag.html) · [Prompt](slownik/prompt.html)

Not sure whether a bot will do or you need an agent? [AI Solution Design →](solution-design.html)
