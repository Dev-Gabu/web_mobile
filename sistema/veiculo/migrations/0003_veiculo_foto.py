# Generated by Django 5.0.4 on 2024-05-08 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0002_veiculo_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='veiculo/fotos'),
        ),
    ]
