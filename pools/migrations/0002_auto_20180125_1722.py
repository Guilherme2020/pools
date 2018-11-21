# Generated by Django 2.0.1 on 2018-01-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=255),
        ),
    ]
