# Generated by Django 4.1.6 on 2023-07-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nza', '0004_grammar_delete_grammarlesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grammar',
            old_name='save',
            new_name='json',
        ),
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]