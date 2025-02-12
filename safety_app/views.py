from django.shortcuts import render
from safety_app.services.gene_service import GeneService

def home(request):
    genes = GeneService.get_all_genes()
    context = {
        "message": "Show me some interesting safety data please.",
        "genes": genes,
    }
    return render(request, "index.html", context)
