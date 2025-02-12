# Practice Drug Safety Application

## Overview

This application is a tool designed to visualize and explore safety data for drug targets. Built using the Django web framework, it provides a simple interface for users to review key attributes of genes—such as risk scores, literature occurrences, development levels, and expression patterns.

## Background

The application processes several JSON Lines (JSONL) files containing data about fictional drug targets. It loads the main gene records and supplements them with additional data from other files. Data validation is handled via Pydantic models, ensuring that only valid and meaningful data is stored in the database. The design focuses on clarity, modularity, and testability.

## Data Description

The following data files are used:

- **genes.jsonl:** Contains the unique ID and display name for each gene.
- **risk_score_data.jsonl:** Contains a numeric safety score for each gene (higher scores indicate higher risk).  
  *(Keys: "gene_id" and "value")*
- **lit_occurrence_data.jsonl:** Contains the number of paragraph mentions for each gene in scientific literature.  
  *(Keys: "gene_id" and "value")*
- **development_level.jsonl:** Contains the development level of each gene (e.g., Tdark, Tbio, Tclin).  
  *(Keys: "gene_id" and "value")*
- **expression_data.jsonl:** Contains information on gene expression in tissues (e.g., low tissue specificity, tissue enhanced, high tissue specificity).  
  *(Keys: "gene_id" and "value")*

The data loader reads the main `genes.jsonl` file and, for each gene record, supplements it with the additional data from the other JSONL files. If any file or field is missing, it handles the situation gracefully.

## Features

- **Data Loading:**  
  A custom Django management command (`load_genes`) loads gene records from the main JSONL file and supplements them with data from additional files. The data is validated using Pydantic models before being saved to the database.

- **Data Visualization:**  
  A Django view renders a simple HTML page that displays the gene data in a table format. Users can view all genes along with their risk scores, literature occurrences, development levels, and expression information.

## Getting Started

### Prerequisites

Ensure you have Python installed. It’s recommended that you use a virtual environment so that project dependencies do not interfere with your system Python installation.

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
