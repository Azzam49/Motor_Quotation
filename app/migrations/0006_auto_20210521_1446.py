# Generated by Django 3.1.6 on 2021-05-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210521_1445'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='customerprofile',
            constraint=models.UniqueConstraint(fields=('user', 'quotation'), name='unique user-quotation'),
        ),
    ]
