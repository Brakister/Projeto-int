# Generated by Django 5.0.4 on 2024-05-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordem_servico', '0003_alter_emissaoordemservico_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissaoordemservico',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
