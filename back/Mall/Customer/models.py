from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):

    email = models.EmailField(
        verbose_name="이메일", max_length=254, unique=True)
    customer_name = models.CharField(
        verbose_name="고객 이름", max_length=50)
    phone_number = PhoneNumberField(
        verbose_name="전화번호", unique=True, region="SK")

    class Meta:
        db_table = "Customer"
        verbose_name = "고객"
        verbose_name_plural = "고객 정보"
