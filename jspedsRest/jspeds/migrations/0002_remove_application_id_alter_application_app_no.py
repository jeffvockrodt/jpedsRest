# Generated by Django 4.1.7 on 2023-03-01 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jspeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.AlterField(
            model_name='application',
            name='app_no',
            field=models.CharField(db_column='app_no', max_length=30, primary_key=True, serialize=False),
        ),
    ]
