# Generated by Django 2.2 on 2019-05-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0014_auto_20190509_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='create_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='expiry_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
