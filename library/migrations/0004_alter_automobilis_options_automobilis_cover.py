# Generated by Django 4.1.1 on 2023-01-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_uzsakymoeilute_status_uzsakymas_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobilis',
            options={'ordering': ['klientas', 'valstybinis_nr'], 'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AddField(
            model_name='automobilis',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers', verbose_name='Viršelis'),
        ),
    ]
