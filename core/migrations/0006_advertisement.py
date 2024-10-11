# Generated by Django 4.2.5 on 2024-05-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='advertisement/')),
                ('text', models.CharField(max_length=150)),
            ],
        ),
    ]