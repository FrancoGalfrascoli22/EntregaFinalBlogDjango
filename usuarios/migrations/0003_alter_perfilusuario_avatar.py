# Generated by Django 4.0.4 on 2022-05-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_perfilusuario_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='avatar',
            field=models.ImageField(default='default.jpg', null=True, upload_to='avatar'),
        ),
    ]
