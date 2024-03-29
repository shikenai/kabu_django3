# Generated by Django 3.2.16 on 2023-01-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(blank=True, max_length=20, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('division', models.CharField(blank=True, max_length=20, null=True)),
                ('industry_code_1', models.IntegerField(blank=True, null=True)),
                ('industry_division_1', models.CharField(blank=True, max_length=10, null=True)),
                ('industry_code_2', models.IntegerField(blank=True, null=True)),
                ('industry_division_2', models.CharField(blank=True, max_length=10, null=True)),
                ('scale_code', models.IntegerField(blank=True, null=True)),
                ('scale_division', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
