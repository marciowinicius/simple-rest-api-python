# Generated by Django 2.0.5 on 2018-05-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]