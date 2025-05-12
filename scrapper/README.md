# The Batch Scrapper
This is a script to scrape The Batch, a website tailored to put weekly news about AI.

The script takes the most relevant information from each of the articles, transforms them into Markdown, stores them into a file and uploads said file to an S3 bucket in Amazon.

## Requirements

- A bucket called `the-batch-markdown`
- AWS CLI configured with SSO (or equivalent AWS environment variables)
- Python 3.8 or higher
- Installed dependencies from `requirements.txt`
- Playwright

## Installation

First, install the required dependencies to run the project.

```bash
pip install -r requirements.txt
```

### Using Playwright to scrape

For this project, Playwright is being used to access the web and scrape the different articles in the web, traversing through each of them. 
To start using Playwright, download the required drivers to allow Playwright access the web.

```bash
playwright install
```

## Usage

After running aws sso login with a profile or session with

- S3 enabled
- A bucket called `the-batch-markdown`

Run

```bash
python main.py
```

## Configuration

- `main.py` contains the configuration for the script.
