# Generated by Django 4.1.7 on 2023-03-01 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jspeds', '0002_remove_application_id_alter_application_app_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='app_status',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_status_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_type',
        ),
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='application',
            name='applicant_ref',
        ),
        migrations.RemoveField(
            model_name='application',
            name='art_unit',
        ),
        migrations.RemoveField(
            model_name='application',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='application',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='application',
            name='conf_no',
        ),
        migrations.RemoveField(
            model_name='application',
            name='content',
        ),
        migrations.RemoveField(
            model_name='application',
            name='continuing_app',
        ),
        migrations.RemoveField(
            model_name='application',
            name='entity_category',
        ),
        migrations.RemoveField(
            model_name='application',
            name='examiner',
        ),
        migrations.RemoveField(
            model_name='application',
            name='file_loc',
        ),
        migrations.RemoveField(
            model_name='application',
            name='filing_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='first_inventor',
        ),
        migrations.RemoveField(
            model_name='application',
            name='fitf',
        ),
        migrations.RemoveField(
            model_name='application',
            name='grant_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='inventors',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ipOfficeCode',
        ),
        migrations.RemoveField(
            model_name='application',
            name='law_firm_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='law_firms',
        ),
        migrations.RemoveField(
            model_name='application',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='application',
            name='nationalClass',
        ),
        migrations.RemoveField(
            model_name='application',
            name='nationalSubclass',
        ),
        migrations.RemoveField(
            model_name='application',
            name='patent_number',
        ),
        migrations.RemoveField(
            model_name='application',
            name='practitioners',
        ),
        migrations.RemoveField(
            model_name='application',
            name='pros_hist',
        ),
        migrations.RemoveField(
            model_name='application',
            name='pta_amount',
        ),
        migrations.RemoveField(
            model_name='application',
            name='pta_bag',
        ),
        migrations.RemoveField(
            model_name='application',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='publication_number',
        ),
        migrations.RemoveField(
            model_name='application',
            name='related_for',
        ),
        migrations.RemoveField(
            model_name='application',
            name='terminal_disclaimer',
        ),
        migrations.RemoveField(
            model_name='application',
            name='title',
        ),
    ]
