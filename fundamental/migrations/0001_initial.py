# Generated by Django 3.2.13 on 2022-07-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='pics')),
                ('kab', models.DateField(auto_now=True)),
                ('dekha', models.IntegerField()),
            ],
        ),
    ]
