# Generated by Django 3.2.4 on 2021-06-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tac', '0004_alter_popupcontent_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popupcontent',
            name='language',
            field=models.CharField(default='de', max_length=10, verbose_name='Language'),
        ),
    ]