# A Drug Safety App

## Scenario:
You are tasked with building a small tool to visualize and explore safety data for drug targets. 
This is a core part of what Sable Bio does, so we're looking to see how you handle working 
with data and presenting it effectively.

## Background
You're working for Sable Bio, a biotech company that is developing a new drug safety app.
The team uses the Django web framework to build the app, and have asked you to build
a key new feature for scientists who want to explore drug safety data.

## Task 1: Data Loading
You are provided with data containing information about fictional drug targets
in jsonl format.

* genes.jsonl: The ID and names for each gene
* risk_score_data.jsonl: A numeric safety score for each gene. Higher values indicate higher risk.
* lit_occurrence_data.jsonl: The number of paragraph mentions for the gene in scientific literature
* development_level.jsonl: The development level of the gene (Tdark - not well studied, Tbio - biology undestood, Tclin - developed into clinical settings (eg a drug has been made against the target))
* expression_data: How often the gene is expressed in different tissues (low tissue specificity, tissue enriched, high tissue specificity)

Write a script to:
* Load the data from the various jsonl files
* Ensure any missing or invalid values are handled gracefully

## Task 2: Visualize the Data
Using the provided Django application, build a simple page that allows users to:

* View the genes (eg in a table)
* Split the data by a categorical feature (eg by development level)

We leave the rest open to your imagination and interest, but here are some suggestions:

# Engineering thoughts to consider
You could load the contents the data into the view at the time of request, but bear in mind that there
are some 20,000 genes in the human genome, and many dozens of potential features.

You may want to consider loading once into a [database](https://docs.djangoproject.com/en/5.1/intro/tutorial02/) 
and then serving the data from there, where filtering and sorting can be done on the database.

## Data thoughts to consider
There are patterns and correlations in the risk score data! Can you find any?

Moreover - can your tool help a user find the patterns?

## Tips
If you work with us, you won’t be working in a vacuum, 
Here are some suggestions that describe a bit of what we’re looking for:

* We use poetry for dependency management. If you haven't used it before, check it out. 
* We use Pydantic models rather than plain dictionaries. It helps to document the schema of the data and do some validation for us.
* We like to use type hints for parameters and return types.
* We use pytest for testing and we care a lot about high test coverage.
* We prefer simplicity and rapidity to fiddly engineering setup - hence we quite like Django, even though it's not as shiny as a React app.
* AI coding tools: You are welcome to use any AI coding tools you like, but you should understand the code you've made and be prepared to answer questions about it.

(Even if you don't end up working with us, hopefully the above will be useful as these are best practices that
are widely adopted in the industry.)

## Getting Started

We suggest you make a virtual environment for development, so that anything you install does not 
pollute your system Python installation:

```bash
python -m venv .venv
source .venv/bin/activate
```

Then, to install dependencies, please run:

```bash
poetry install
```

To run the app, enter:

```bash
python manage.py runserver 8080
```

To run the tests, run:

```
pytest tests/
```

## What We’re looking for:

Code quality: Is your code clean, modular, and documented with type hints? Does it avoid mixing of concerns (eg loading logic and view logic)

Testing: We'd rather have less functionality than more bugs. Have you written tests for your code?

Learning ability: We don't expect you to know everything in the list above, we are more interested how you approached the task.



**Finally**: _Thank you_ for taking time out of your day to work on this challenge. We appreciate it can be time-consuming, especially if you have multiple interviews to prepare for.
Whatever happens, we have designed this test to be reasonably interesting, and hope it offers the opportunity to learn something new.


## Copyright and Confidentiality
© 2025 Sable Bio Ltd. All rights reserved.

This coding challenge is for assessment purposes only and is the property of Sable Bio. Please do not share, distribute, or post any part of the challenge publicly. We appreciate your understanding and cooperation!

