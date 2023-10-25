# Generated by Django 4.2.5 on 2023-10-25 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('apodo', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]