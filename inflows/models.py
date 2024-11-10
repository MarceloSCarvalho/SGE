from django.db import models
from suppliers.models import Supplier
from products.models import Product


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name="inflows", verbose_name="fornecedor")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="inflows", verbose_name="Produto")
    quantity = models.IntegerField(verbose_name="Quantidade")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em:")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em:")

    class Meta:
        ordering = ['-created_at']
        verbose_name = ("Fluxo de Entrada")

    def __str__(self):
        return f"{self.quantity} units of {str(self.product)} received from {str(self.supplier)}"
