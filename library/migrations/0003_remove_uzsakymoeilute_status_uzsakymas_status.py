# Generated by Django 4.1.1 on 2023-01-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_automobilis_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzsakymoeilute',
            name='status',
        ),
        migrations.AddField(
            model_name='uzsakymas',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Atsiimta'), ('g', 'Galima atsiimti'), ('s', 'Taisoma'), ('e', 'Eileje')], default='a', help_text='Status', max_length=1),
        ),
    ]
