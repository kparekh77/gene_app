from typing import Iterable
from safety_app.utils.models import Gene
from safety_app.utils.data_loader import DataLoader


class GeneService:
    @staticmethod
    def load_and_save_genes(genes_file_path: str) -> int:
        """
        Loads gene data from the JSONL files (using DataLoader) and saves them
        into the database using the Gene model.
        Returns the number of genes processed.
        """
        count = 0
        for gene_data in DataLoader.load_genes(genes_file_path):
            Gene.objects.update_or_create(
                gene_id=gene_data.id,
                defaults={
                    "display_name": gene_data.display_name,
                    "risk_score": gene_data.risk_score,
                    "lit_occurrences": gene_data.lit_occurrences,
                    "development_level": gene_data.development_level,
                    "expression": gene_data.expression,
                },
            )
            count += 1
        return count

    @staticmethod
    def get_all_genes() -> Iterable[Gene]:
        """Return all genes from the database."""
        return Gene.objects.all()
