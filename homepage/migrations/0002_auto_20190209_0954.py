# Generated by Django 2.1.5 on 2019-02-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='status',
            field=models.CharField(choices=[('Done', 'done'), ('Pending', 'pending')], default='done', max_length=20),
        ),
    ]
