# Generated by Django 3.2.5 on 2022-05-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220517_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='trainTicketBack',
            field=models.BooleanField(default=False, verbose_name='Билет обратно'),
        ),
        migrations.AddField(
            model_name='kid',
            name='trainTicketThere',
            field=models.BooleanField(default=False, verbose_name='Билет туда'),
        ),
    ]
