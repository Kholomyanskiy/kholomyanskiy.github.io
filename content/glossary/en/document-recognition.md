---
slug: document-recognition
title: "Document recognition (OCR): types and how to choose"
description: "Document recognition turns scans and photos into text and data. The main types, from classic OCR to vision models, and how to check the result."
published: 2026-11-08
updated: 2026-11-08
---

# Document recognition (OCR)

Document recognition turns a scan, a photo or an image-only PDF into text and data that software can work with: search, add up, enter into a system. In everyday use all of this is called OCR (optical character recognition), although the name covers different technologies with different strengths. The choice between them decides how much manual work remains after automation.

## The main types

Classic OCR finds letters and digits in an image and outputs text. It is fast, cheap and handles clean print well: contracts, letters, book pages. But the output is just text, with no understanding of where the document number is and where the amount is. A crumpled receipt, a stamp over the text or a photo taken at an angle noticeably lowers quality.

Template-based extraction adds markup to OCR: in a known document type the fields are marked in advance, and the system pulls values from them. It works well on a stream of identical forms from the same senders and poorly when formats keep changing.

Language models with vision read the whole image and return the required fields directly: shop, date, line items, total. They need no template for each format and cope with angled photos and unfamiliar layouts. The downside is that a model may confidently write in a plausible figure where nothing can be read in the image. That is the same [hallucination](slownik/hallucination.html), only in numbers.

Handwriting is a case of its own. All three approaches can read it, but with a noticeably higher error rate, and such data is usually not allowed into accounting without a human check.

## Text or data

For archive search and a [knowledge base](slownik/knowledge-base.html), text is enough: what matters is that the words are recognised and the document can be found. Accounting and record-keeping need data: specific fields with verified values. These are two different tasks with different quality requirements. A typo in a word barely affects search; a typo in an amount ends up in a report.

## How the result is checked

The most useful checks rely on the document's internal logic. Line items must add up to the total. Tax must match the rate. A date cannot be in the future. A Polish NIP tax number has a check digit, and a misread number usually fails it. Code checks such rules without involving the model.

Anything that fails a check or is recognised with low confidence goes to a [human in the loop](slownik/human-in-the-loop.html). A good recognition system does not promise zero errors; it shows which documents need a person's eyes.

## When recognition is not needed

The most reliable document is one that never had to be recognised. A PDF exported from software already contains text. In Poland, since 2026, invoices between businesses increasingly pass through KSeF as structured data and can be obtained without a single scan. Before automating recognition, it is worth checking whether the same data can be obtained electronically from the source.

## From experience

For a Telegram bot that tracks personal expenses, we built recognition of Polish till receipts from photos. Classic OCR would have produced text from which the shop, date, items and total would have to be extracted with separate rules for each receipt format, and retail chains use different formats. So the receipt is read by a vision model that returns the fields directly. There were no serious errors in receipt recognition.

The main lesson was about choosing the approach. For receipts, with many formats and small documents, a vision model turned out simpler and cheaper to set up. For a stream of identical contracts, classic OCR with rules can be more reliable and several times cheaper.

## What to decide in advance

Which documents need recognising, in what volume, and how much their formats vary. Whether the goal is text for search or data for accounting. Which checks code performs and what happens to a document that fails them. Who reviews disputed documents and how many per day is acceptable. And whether some documents can be obtained electronically, so they need no recognition at all.

---

**Related terms:** [Knowledge base for AI](slownik/knowledge-base.html) · [AI hallucination](slownik/hallucination.html) · [Human in the loop](slownik/human-in-the-loop.html) · [RAG](slownik/rag.html)

Want to automate document processing in your company? [AI Solution Design →](solution-design.html)
