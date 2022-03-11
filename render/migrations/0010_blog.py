# Generated by Django 4.0.1 on 2022-02-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/blog')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
