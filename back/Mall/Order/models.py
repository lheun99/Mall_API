from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Order(models.Model):
    ordered_at = models.DateTimeField(verbose_name="주문 날짜", auto_now_add=True)
    address = models.CharField(verbose_name="주소", max_length=50)

    orderer = models.ForeignKey(
        'Customer.Customer', verbose_name='고객 정보', on_delete=models.CASCADE)

    product = models.ForeignKey(
        'Product.Product', verbose_name='제품 정보', on_delete=models.CASCADE)

    recipient_name = models.CharField(verbose_name="수령자 이름", max_length=50)
    recipient_phone_number = PhoneNumberField(
        verbose_name="수령자 전화번호", unique=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = "Order"
        verbose_name = "주문"
        verbose_name_plural = "주문 정보"
