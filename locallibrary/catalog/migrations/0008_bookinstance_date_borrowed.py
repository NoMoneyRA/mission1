# Generated by Django 5.1.1 on 2024-11-18 18:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='date_borrowed',
            field=models.DateField(default=django.utils.timezone.now, help_text='Дата взятия книги'),
        ),
    ]