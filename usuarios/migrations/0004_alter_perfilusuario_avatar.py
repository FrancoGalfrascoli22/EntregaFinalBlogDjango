# Generated by Django 4.0.4 on 2022-05-25 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_perfilusuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', null=True, upload_to='avatar'),
        ),
    ]
