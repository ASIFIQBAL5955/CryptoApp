# Generated by Django 4.1.3 on 2022-12-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('phone', models.IntegerField(blank=True, max_length=20)),
                ('Email', models.EmailField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Change_password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('New_password', models.IntegerField(blank=True, max_length=10)),
                ('Confirm_new_password', models.IntegerField(blank=True, max_length=10)),
            ],
        ),
    ]
