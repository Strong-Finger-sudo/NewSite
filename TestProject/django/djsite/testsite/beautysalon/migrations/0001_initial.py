# Generated by Django 4.2.1 on 2023-05-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название сервиса')),
                ('social_image_header', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='Ссылка на сервис')),
            ],
            options={
                'verbose_name': 'Соц сеть',
                'verbose_name_plural': 'Соц сети',
            },
        ),
    ]
