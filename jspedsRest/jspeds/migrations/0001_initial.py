# Generated by Django 4.1.7 on 2023-03-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_no', models.CharField(max_length=30)),
                ('filing_date', models.DateField()),
                ('art_unit', models.CharField(max_length=30)),
                ('examiner', models.CharField(max_length=300)),
                ('first_inventor', models.CharField(max_length=300)),
                ('entity_category', models.CharField(max_length=80)),
                ('conf_no', models.CharField(max_length=30)),
                ('app_status', models.CharField(max_length=300)),
                ('app_status_date', models.DateField()),
                ('file_loc', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('fitf', models.BooleanField()),
                ('app_type', models.CharField(max_length=300)),
                ('applicant_ref', models.CharField(max_length=300)),
                ('applicant', models.CharField(max_length=300)),
                ('assignee', models.CharField(max_length=300)),
                ('law_firm_name', models.CharField(max_length=300)),
                ('publication_number', models.CharField(max_length=30)),
                ('publication_date', models.DateField()),
                ('patent_number', models.CharField(max_length=30)),
                ('grant_date', models.DateField()),
                ('pta_amount', models.CharField(max_length=30)),
                ('terminal_disclaimer', models.BooleanField()),
                ('continuing_app', models.BooleanField()),
                ('related_for', models.BooleanField()),
                ('ipOfficeCode', models.CharField(max_length=300)),
                ('nationalSubclass', models.CharField(max_length=30)),
                ('nationalClass', models.CharField(max_length=30)),
                ('law_firms', models.JSONField()),
                ('practitioners', models.JSONField()),
                ('inventors', models.JSONField()),
                ('metadata', models.JSONField()),
                ('pros_hist', models.JSONField()),
                ('pta_bag', models.JSONField()),
                ('assignment', models.JSONField()),
                ('content', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='AppSerializer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]