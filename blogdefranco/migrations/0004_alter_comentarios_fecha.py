# Generated by Django 4.0.4 on 2022-05-24 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdefranco', '0003_alter_comentarios_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]