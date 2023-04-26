# Generated by Django 4.2 on 2023-04-25 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('Restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.restaurant')),
            ],
        ),
    ]
