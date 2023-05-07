---
title: Metaanalyser
emoji: 🎓
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: 3.28.3
app_file: app.py
pinned: false
tags:
  - LangChain
  - GPT
---

# Metaanalyser

This is an application that generates systematic reviews  powered by GPT. It searches Google Scholar with a given query and generates a systematic review using the search results. https://huggingface.co/spaces/p-baleine/metaanalyser

Following is a quote from Wikipedia:

> A systematic review is a scholarly synthesis of the evidence on a clearly presented topic using critical methods to identify, define and assess research on the topic. A systematic review extracts and interprets data from published studies on the topic, then analyzes, describes, and summarizes interpretations into a refined conclusion.

This application aims to generate a systematic review of a given topic by examining multiple literature.

This application is an experiment. The application may exceed the maximum token length and produce errors, or produce output of such poor quality that it is not appropriate to call it a systematic review.

## Examples

You can find a sample output of this application in the [examples](./examples) directory (the file name is a Google Scholar search query).

- [A Systematic Review of Large Language Model Agent and Tool Integration](./examples/llm%20agent%20OR%20llm%20tool%20integration.md)
- [A Systematic Review of Pitman-Yor Language Model](./examples/Pitman-Yor%20Language%20Model.md)
- [A Systematic Review of Programming Testing Arxiv](./examples/programming%20testing%20arxiv.md): I wanted to limit my search to arXiv, so I included "arxiv" in the query, resulting in an unintended title.
