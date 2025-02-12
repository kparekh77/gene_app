from django.core.management.base import BaseCommand
from safety_app.services.gene_service import GeneService


class Command(BaseCommand):
    help = "Load gene data from a JSONL file using the services layer."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the genes.jsonl file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        self.stdout.write(f"Loading genes from {file_path}...")
        count = GeneService.load_and_save_genes(file_path)
        self.stdout.write(f"Gene data loading complete. {count} records processed.")
