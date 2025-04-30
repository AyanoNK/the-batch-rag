# The Batch Scrapper

This is a simple script to scrape the batch website and save the results in markdown format in an S3 bucket.

## Requirements

- A bucket called `the-batch-markdown`
- AWS CLI configured with SSO
- Python 3.8 or higher
- Installed dependencies from `requirements.txt`
- Playwright

## Installation

```bash
pip install -r requirements.txt
```

```bash
playwright install
```

## Usage

Run after running aws sso login with a profile or session with

- S3 enabled
- A bucket called `the-batch-markdown`

Run

```bash
python main.py
```

## Configuration

- `main.py` contains the configuration for the script.
