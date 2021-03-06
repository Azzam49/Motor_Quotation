# Generated by Django 3.1.6 on 2021-05-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210518_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverageSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Coverage Name')),
                ('value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Coverage Value')),
            ],
        ),
    ]
