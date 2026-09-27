# Book Web Scraping & Data Extraction

A Python data-extraction project that scrapes book information from **Books to Scrape** and structures the collected data with Pandas.

## Overview

The script requests catalogue pages, parses HTML using BeautifulSoup, extracts product information, and stores the collected records in a Pandas DataFrame.

## Tech Stack

- Python 3
- Requests
- BeautifulSoup
- Pandas

## Extracted Fields

The current script collects:

- Book title
- Price
- Star-rating class

It iterates across multiple catalogue pages to build a structured dataset.

## Installation

```bash
pip install requests beautifulsoup4 pandas
```

## Run

```bash
python main.py
```

## How It Works

1. Sends HTTP requests to catalogue pages.
2. Parses the HTML with BeautifulSoup.
3. Finds each book card in the page.
4. Extracts title, price, and rating information.
5. Appends the records to a Python list.
6. Converts the collection into a Pandas DataFrame.

## Current Scope

This repository demonstrates the extraction and DataFrame-building stage of a data pipeline. The current implementation does not yet persist the DataFrame to a database or file.

## Suggested Next Improvements

- Add request timeout and error handling
- Export results to CSV/JSON
- Persist records to MySQL/PostgreSQL
- Add duplicate handling and validation
- Add command-line arguments for category/page range
- Add automated tests
