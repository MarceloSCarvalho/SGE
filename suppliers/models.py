from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Fornecedores")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em:")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em:")

    class Meta:
        ordering = ['name']
        verbose_name = ('fornecedor')

    def __str__(self):
        return self.name
