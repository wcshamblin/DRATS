# Generated by Django 3.0.6 on 2020-06-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WTB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=60)),
                ('ccnumber', models.CharField(max_length=60)),
            ],
        ),
    ]
