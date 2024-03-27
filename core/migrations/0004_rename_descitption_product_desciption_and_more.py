# Generated by Django 5.0.3 on 2024-03-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_civil_status_alter_user_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descitption',
            new_name='desciption',
        ),
        migrations.AlterField(
            model_name='user',
            name='civil_status',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Casad@', 'Casad@'), ('Divorciad@', 'Divorciad@'), ('Viud@', 'Viud@'), ('Union libre', 'Union libre')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=100, verbose_name='Sexo'),
        ),
    ]
