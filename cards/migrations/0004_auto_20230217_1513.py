# Generated by Django 3.1.14 on 2023-02-17 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_summa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='Muddati',
            new_name='Card_data',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Karta_raqami',
            new_name='Card_num',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Ism_familya',
            new_name='Name',
        ),
    ]
