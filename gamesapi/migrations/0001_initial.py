# Generated by Django 4.2 on 2023-05-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=10)),
                ('Ratings', models.CharField(max_length=10)),
                ('Year_Of_Release', models.CharField(max_length=10)),
            ],
        ),
    ]
