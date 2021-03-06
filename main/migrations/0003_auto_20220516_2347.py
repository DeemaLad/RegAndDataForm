# Generated by Django 3.2.5 on 2022-05-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220516_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passportDetails', models.CharField(max_length=100, verbose_name='Паспортные данные/Свидетельство о рождении')),
                ('copyPassport', models.ImageField(upload_to='passports/', verbose_name='Изображение')),
                ('kidFullName', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birthDate', models.DateField(verbose_name='Дата Рождения')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес по месту прописки')),
                ('user_agreement', models.BooleanField(default=True, verbose_name='Пользовательское соглашение')),
            ],
            options={
                'verbose_name': 'Ребенок',
                'verbose_name_plural': 'Список детей',
            },
        ),
        migrations.AlterModelOptions(
            name='parent1',
            options={'verbose_name': 'Родитель №1', 'verbose_name_plural': 'Список родителей(опекунов) №1'},
        ),
        migrations.AlterModelOptions(
            name='parent2',
            options={'verbose_name': 'Родитель №2', 'verbose_name_plural': 'Список родителей(опекунов) №2'},
        ),
        migrations.AlterField(
            model_name='parent1',
            name='user_agreement',
            field=models.BooleanField(default=True, verbose_name='Пользовательское соглашение'),
        ),
        migrations.AlterField(
            model_name='parent2',
            name='user_agreement',
            field=models.BooleanField(default=True, verbose_name='Пользовательское соглашение'),
        ),
    ]
