# Generated by Django 4.1.5 on 2023-01-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('categeory', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('details', models.TextField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='myimage')),
            ],
        ),
    ]