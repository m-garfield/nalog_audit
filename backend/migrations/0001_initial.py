# Generated by Django 3.2.20 on 2023-08-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('position_work', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
