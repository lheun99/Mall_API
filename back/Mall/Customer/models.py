from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):

    email = models.CharField(verbose_name="이메일", max_length=50, unique=True)
    name = models.CharField(verbose_name="고객 이름", max_length=50)
    phone_number = PhoneNumberField(verbose_name="전화번호", unique=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = "HappyMoonday_Customer"
        verbose_name = "고객"
        verbose_name_plural = "고객 정보"
