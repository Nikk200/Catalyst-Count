# Generated by Django 5.0.7 on 2024-07-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0005_alter_company_year_founded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='current_employee_estimate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='size_range',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='total_employee_estimate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
