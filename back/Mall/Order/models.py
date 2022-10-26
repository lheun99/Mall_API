from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Order(models.Model):
    ORDER_STATE = (
        (0, '결제 완료'),
        (1, '배송준비중'),
        (2, '배송중'),
        (3, '배송완료'),
    )

    orderer_id = models.ForeignKey(
        'Customer.Customer', verbose_name='주문 고객 정보', on_delete=models.CASCADE)

    recipient_name = models.CharField(verbose_name="수령 고객 이름", max_length=50)
    recipient_phone_number = PhoneNumberField(
        verbose_name="수령 고객 전화번호", unique=True)

    ordered_at = models.DateTimeField(verbose_name="주문 날짜", auto_now_add=True)

    address = models.CharField(verbose_name="주소", max_length=50)

    product_id = models.ForeignKey(
        'Product.Product', verbose_name='제품 정보', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="제품 수량")

    status = models.PositiveIntegerField(
        verbose_name='주문 상태', default=0, choices=ORDER_STATE)

    def __str__(self):
        return str(self.orderer) + ' ' + str(self.product)

    class Meta:
        db_table = "Order"
        verbose_name = "주문"
        verbose_name_plural = "주문 정보"
