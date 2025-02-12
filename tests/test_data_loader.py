from safety_app.utils.data_loader import DataLoader
from safety_app.utils.models import GeneData
from tests.helpers import write_jsonl

def test_load_genes_valid(valid_data_files):
    """
    Test that DataLoader.load_genes correctly merges data from the supplementary files.
    """
    genes_file = valid_data_files["genes_file"]
    genes = list(DataLoader.load_genes(genes_file))
    assert len(genes) == 2

    gene1: GeneData = genes[0]
    assert gene1.id == 1
    assert gene1.display_name == "GeneOne"
    assert gene1.risk_score == 0.45
    assert gene1.lit_occurrences == 10
    assert gene1.development_level == "Tbio"
    assert gene1.expression == "Low tissue specificity"

    gene2: GeneData = genes[1]
    assert gene2.id == 2
    assert gene2.display_name == "GeneTwo"
    assert gene2.risk_score == 0.80
    assert gene2.lit_occurrences == 15
    assert gene2.development_level == "Tclin"
    assert gene2.expression == "High tissue specificity"


def test_load_genes_missing_supplementary(tmp_path):
    """
    Test that if the supplementary files are missing, the gene records are loaded
    and their supplementary fields remain None.
    """

    genes = [
        {"id": 1, "display_name": "GeneOnly"},
    ]
    base = tmp_path
    genes_file = base / "genes.jsonl"
    write_jsonl(genes_file, genes)

    genes_loaded = list(DataLoader.load_genes(str(genes_file)))
    assert len(genes_loaded) == 1
    gene = genes_loaded[0]

    assert gene.risk_score is None
    assert gene.lit_occurrences is None
    assert gene.development_level is None
    assert gene.expression is None


def test_load_genes_with_invalid_record(tmp_path, capsys):
    """
    Test that an invalid gene record (missing required field) is skipped.
    """
    valid = {"id": 1, "display_name": "GeneValid"}
    invalid = {"display_name": "MissingID"}
    genes = [valid, invalid]
    base = tmp_path
    genes_file = base / "genes.jsonl"
    write_jsonl(genes_file, genes)

    risk_scores = [{"gene_id": 1, "value": 0.55}]
    lit_occ = [{"gene_id": 1, "value": 5}]
    dev_levels = [{"gene_id": 1, "value": "Tbio"}]
    expr = [{"gene_id": 1, "value": "Tissue specific"}]

    for fname, data in [
        ("risk_score_data.jsonl", risk_scores),
        ("lit_occurrence_data.jsonl", lit_occ),
        ("development_level.jsonl", dev_levels),
        ("expression_data.jsonl", expr),
    ]:
        write_jsonl(base / fname, data)

    genes_loaded = list(DataLoader.load_genes(str(genes_file)))
    assert len(genes_loaded) == 1
    gene = genes_loaded[0]
    assert gene.id == 1

    captured = capsys.readouterr().out
    assert "Skipping invalid gene record" in captured
