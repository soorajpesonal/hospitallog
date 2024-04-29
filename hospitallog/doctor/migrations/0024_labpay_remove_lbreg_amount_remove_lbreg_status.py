# Generated by Django 4.0.1 on 2024-03-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0023_lbreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='labpay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pid', models.CharField(max_length=10)),
                ('phno', models.IntegerField()),
                ('category', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=100)),
                ('lbdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='lbreg',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='lbreg',
            name='status',
        ),
    ]
