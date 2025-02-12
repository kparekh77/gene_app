from django.db import models
from pydantic import BaseModel, Field
from typing import Optional


class GeneData(BaseModel):
    id: int = Field(..., description="The gene ID")
    display_name: str = Field(..., description="The gene’s display name")
    risk_score: Optional[float] = Field(0.0, description="The safety risk score (0–1)")
    lit_occurrences: Optional[int] = Field(0, description="Literature occurrences")
    development_level: Optional[str] = Field("Tdark", description="Development level (e.g. Tdark, Tbio, Tclin)")
    expression: Optional[str] = Field("", description="Expression information")



class Gene(models.Model):
    gene_id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    risk_score = models.FloatField(blank=True, null=True)
    lit_occurrences = models.IntegerField(blank=True, null=True)
    development_level = models.CharField(max_length=20, blank=True, null=True)
    expression = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.display_name or f"Gene {self.gene_id}"
