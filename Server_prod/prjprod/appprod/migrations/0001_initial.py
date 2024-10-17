# Generated by Django 5.1.2 on 2024-10-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='0', max_length=250)),
                ('precio', models.DecimalField(decimal_places=2, default='0', max_digits=10)),
                ('existencias', models.IntegerField(default='0')),
            ],
        ),
    ]
