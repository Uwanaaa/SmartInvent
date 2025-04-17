from django.db import models
from django.contrib.postgres.search import TrigramSimilarity,SearchVector

class ProductManager(models.Manager):
    def query_search(self,query):
        results = self.annotate(
            search=SearchVector('name'),
            similarity=TrigramSimilarity('name',query)
        ).filter(
            search = query
        ).filter(
            similarity__gt=0.2
        ).order_by('-similarity')

        return results