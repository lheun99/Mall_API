# Generated by Django 3.1.14 on 2022-10-25 14:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True, verbose_name='주문 날짜')),
                ('address', models.CharField(max_length=50, verbose_name='주소')),
                ('recipient_name', models.CharField(max_length=50, verbose_name='수령자 이름')),
                ('recipient_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='수령자 전화번호')),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer', verbose_name='고객 정보')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='제품 정보')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문 정보',
                'db_table': 'Order',
            },
        ),
    ]