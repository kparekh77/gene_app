import json
import os
from typing import Dict, Iterable, Any
from safety_app.utils.models import GeneData
from safety_app.utils.mapping_loader import MappingLoader


class DataLoader:
    @staticmethod
    def load_genes(genes_file_path: str) -> Iterable[GeneData]:
        """
        Loads gene records from the main genes JSONL file, then supplements each record with data
        from the supplementary JSONL files found in the same folder.

        The main file is expected to have keys "id" and "display_name". The supplementary files are:
          - risk_score_data.jsonl (keys: "gene_id" and "risk_score")
          - lit_occurrence_data.jsonl (keys: "gene_id" and "lit_occurrences")
          - development_level.jsonl (keys: "gene_id" and "development_level")
          - expression_data.jsonl (keys: "gene_id" and "value")
        """

        base_dir = os.path.dirname(genes_file_path)

        risk_file = os.path.join(base_dir, "risk_score_data.jsonl")
        lit_file = os.path.join(base_dir, "lit_occurrence_data.jsonl")
        dev_file = os.path.join(base_dir, "development_level.jsonl")
        expr_file = os.path.join(base_dir, "expression_data.jsonl")

        risk_mapping = MappingLoader.load_mapping(risk_file, key_field="gene_id", value_field="value")
        lit_mapping = MappingLoader.load_mapping(lit_file, key_field="gene_id", value_field="value")
        dev_mapping = MappingLoader.load_mapping(dev_file, key_field="gene_id", value_field="value")
        expr_mapping = MappingLoader.load_mapping(expr_file, key_field="gene_id", value_field="value")

        with open(genes_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                record = json.loads(line)
                try:
                    gene_data = GeneData(**record)
                except Exception as e:
                    print(f"Skipping invalid gene record: {record}. Error: {e}")
                    continue

                gene_id = gene_data.id
                gene_data.risk_score = risk_mapping.get(gene_id)
                gene_data.lit_occurrences = lit_mapping.get(gene_id)
                gene_data.development_level = dev_mapping.get(gene_id)
                gene_data.expression = expr_mapping.get(gene_id)

                yield gene_data
