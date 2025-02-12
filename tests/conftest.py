import json
from tests.helpers import write_jsonl
import pytest
from pathlib import Path


@pytest.fixture
def valid_data_files(tmp_path):
    """
    Create a temporary directory with the following files:
      - genes.jsonl: contains gene records (with keys "id" and "display_name")
      - risk_score_data.jsonl: records with keys "gene_id" and "value" for risk scores
      - lit_occurrence_data.jsonl: records with keys "gene_id" and "value" for literature occurrences
      - development_level.jsonl: records with keys "gene_id" and "value" for development level
      - expression_data.jsonl: records with keys "gene_id" and "value" for expression data
    """
    # Main genes file (using key "id" for the gene ID)
    genes = [
        {"id": 1, "display_name": "GeneOne"},
        {"id": 2, "display_name": "GeneTwo"},
    ]

    # Supplementary mapping files use "gene_id" as key and "value" for the mapped field.
    risk_scores = [
        {"gene_id": 1, "value": 0.45},
        {"gene_id": 2, "value": 0.80},
    ]
    lit_occurrences = [
        {"gene_id": 1, "value": 10},
        {"gene_id": 2, "value": 15},
    ]
    dev_levels = [
        {"gene_id": 1, "value": "Tbio"},
        {"gene_id": 2, "value": "Tclin"},
    ]
    expressions = [
        {"gene_id": 1, "value": "Low tissue specificity"},
        {"gene_id": 2, "value": "High tissue specificity"},
    ]

    # Create files in the temporary directory
    base = tmp_path
    write_jsonl(base / "genes.jsonl", genes)
    write_jsonl(base / "risk_score_data.jsonl", risk_scores)
    write_jsonl(base / "lit_occurrence_data.jsonl", lit_occurrences)
    write_jsonl(base / "development_level.jsonl", dev_levels)
    write_jsonl(base / "expression_data.jsonl", expressions)

    # Return the path to the main file (and directory if needed)
    return {"genes_file": str(base / "genes.jsonl"), "dir": str(base)}


@pytest.fixture
def sample_data_dir(tmp_path: Path) -> Path:
    """Creates a temporary directory with all JSONL files for a full run."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    genes = [
        {"id": 1, "display_name": "GeneA"},
        {"id": 2, "display_name": "GeneB"}
    ]
    with open(data_dir / "genes.jsonl", "w") as f:
        for record in genes:
            f.write(json.dumps(record) + "\n")

    risk = [
        {"gene_id": 1, "value": 0.4},
        {"gene_id": 2, "value": 0.7}
    ]
    with open(data_dir / "risk_score_data.jsonl", "w") as f:
        for record in risk:
            f.write(json.dumps(record) + "\n")

    lit = [
        {"gene_id": 1, "value": 10},
        {"gene_id": 2, "value": 20}
    ]
    with open(data_dir / "lit_occurrence_data.jsonl", "w") as f:
        for record in lit:
            f.write(json.dumps(record) + "\n")

    dev = [
        {"gene_id": 1, "value": "Tdark"},
        {"gene_id": 2, "value": "Tclin"}
    ]
    with open(data_dir / "development_level.jsonl", "w") as f:
        for record in dev:
            f.write(json.dumps(record) + "\n")

    expr = [
        {"gene_id": 1, "value": "Low tissue specificity"},
        {"gene_id": 2, "value": "Tissue enriched"}
    ]
    with open(data_dir / "expression_data.jsonl", "w") as f:
        for record in expr:
            f.write(json.dumps(record) + "\n")

    return data_dir
