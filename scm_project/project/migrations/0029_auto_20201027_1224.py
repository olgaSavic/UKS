# Generated by Django 3.1.2 on 2020-10-27 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0028_problem_milestone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='milestone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.milestone'),
        ),
    ]
