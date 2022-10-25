from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(verbose_name="제품 이름", max_length=50)
    price = models.IntegerField(verbose_name='제품 가격')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = "Product"
        verbose_name = "제품"
        verbose_name_plural = "제품 정보"
