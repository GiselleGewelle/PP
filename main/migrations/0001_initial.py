# Generated by Django 4.2.1 on 2023-06-01 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Categories', to='main.category')),
            ],
        ),
    ]
