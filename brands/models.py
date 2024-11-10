from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Marcas")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="criado em:")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="atualizado em:")

    class Meta:
        ordering = ['name']
        verbose_name = ('marca')

    def __str__(self):
        return self.name
