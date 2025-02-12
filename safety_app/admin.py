from django.contrib import admin
from safety_app.utils.models import Gene


@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    list_display = ("gene_id", "display_name", "risk_score", "lit_occurrences", "development_level", "expression")
