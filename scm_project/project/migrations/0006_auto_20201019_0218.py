# Generated by Django 3.1.2 on 2020-10-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(),
        ),
    ]