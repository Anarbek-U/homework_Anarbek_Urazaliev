# Generated by Django 5.2.3 on 2025-06-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='more_detailed',
            field=models.TextField(null=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(null=True, verbose_name='Дата выполнения'),
        ),
    ]
