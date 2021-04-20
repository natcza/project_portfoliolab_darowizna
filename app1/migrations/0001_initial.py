# Generated by Django 2.2.19 on 2021-04-20 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarzadowa'), (3, 'zbiorka lokalna')], default=1)),
                ('categories', models.ManyToManyField(related_name='institutions', to='app1.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=12)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField(blank=True)),
                ('categories', models.ManyToManyField(related_name='donations', to='app1.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='app1.Institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]