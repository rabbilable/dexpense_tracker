# Generated by Django 3.1 on 2020-08-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('transaction_date', models.DateTimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='tracker.Category')),
            ],
        ),
    ]