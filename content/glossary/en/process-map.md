---
slug: process-map
title: "Process map: what it is and why you need one before AI implementation"
description: "A process map shows how work actually moves through a department. How it differs from a flowchart, how to build one, and what to decide before AI."
---

# Process map

A process map shows how work actually moves through a department or company: who does what, in which order, what they pass on, where work waits, and where people bypass rules to get things done. It is built from what people actually do and helps decide what to automate and what to leave alone.

## How a process map differs from a flowchart

A flowchart in a procedure shows how a process is supposed to work. A process map shows how it does work. It includes things missing from the procedure: personal Excel spreadsheets, a call to a colleague to “check,” a manual review one person does out of habit, an email that waits a week for a reply. AI breaks down in exactly these places because no one mentioned them.

A process map records:

- the steps and who performs them;
- what is passed between people and departments, and in what form;
- where work waits and for how long;
- which data and tools are used;
- exceptions and workarounds;
- points where an error is costly.

## How to build one

The map takes shape in the first days of a [process audit](slownik/process-audit.html). It has one source: what people actually do. To capture that, take a [work-week snapshot](metodichka.html): each person records what they worked on, how long it took, who assigned it, and where the result went. These records are combined into an overall picture and shown to the people doing the work. They need to confirm the map. A manager alone is not enough; they know how the work is supposed to happen.

You cannot map everyone at once in a large company, and you do not need to. Choose a single workflow that is going to change and follow it from start to finish.

## From experience

For more than ten years, I worked in IT at a large electricity distribution operator: several thousand employees, branches, directorates, districts, and departments at every level. Business processes were described at the top in the quality management system, neatly and in detail. At the bottom, life went its own way. Job descriptions were often tailored to fit a person and gaps in the processes, and even more often an employee wrote their own after a few months on the job. Then it went unchanged for years. The work changed every day: a manager's requests, emails, urgent tasks that were in no document.

AI was not implemented there at the time, but it is easy to imagine what it would have looked like. The requirements would come from procedures and job descriptions, the result would be a generic [document search](slownik/rag.html), and no one could explain what problem it solved. Automation built from a map of procedures automates the procedures. The actual work carries on elsewhere.

## What to decide in advance

How much detail is needed: down to the task or to each individual step. Which workflow to map first. Where the map will live after the audit and who will update it when the process changes. A map that is not updated becomes just another procedure within a year.

## What comes next

The map shows where a process will break if a step is handed over to AI: these are the [failure points](slownik/failure-point.html). It also shows where a [human in the loop](slownik/human-in-the-loop.html) must remain. The selected part is then described in an [AI specification](slownik/ai-specification.html) and tested in a [pilot](slownik/pilot.html).

---

**Related terms:** [Process audit](slownik/process-audit.html) · [Failure point](slownik/failure-point.html) · [Human in the loop](slownik/human-in-the-loop.html) · [AI specification](slownik/ai-specification.html)

Want to see how work actually moves through your department? [AI audit for a department →](audit.html)
