# PageRank Algorithm Implementation

This repository contains code developed for the "PageRank" project as part of "cs50's Introduction to AI" online course offered by Harvard University on edX.

## Overview

The PageRank algorithm, developed by Google's co-founders, is used to determine the importance of web pages based on the links pointing to them. This implementation focuses on calculating PageRank values for web pages using two different methods: sampling and iteration.

## Folder Structure

1. **pagerank**: Contains the main code file `pagerank.py` and subfolders for storing HTML pages.
    - `pagerank.py`: Python script for calculating PageRank values using sampling and iteration methods.
    - `corpus0`, `corpus1`, `corpus2`: Subfolders containing HTML files representing different sets of web pages.

## Usage

To run the PageRank algorithm, use the following command:

```bash
python pagerank.py corpus
