# Generated by Django 5.2.1 on 2025-06-03 22:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_text', models.CharField(blank=True, max_length=128, null=True)),
                ('company_text', models.CharField(blank=True, max_length=32, null=True)),
                ('source_text', models.CharField(blank=True, max_length=32, null=True)),
                ('salary_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('salary_max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('salary_expected', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discarded', models.BooleanField(blank=True, default=False)),
                ('primary_reference_text', models.TextField(blank=True, null=True)),
                ('secondary_reference_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wished',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_text', models.CharField(blank=True, max_length=128, null=True)),
                ('company_text', models.CharField(blank=True, max_length=32, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discarded', models.BooleanField(blank=True, default=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=32)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments_text', models.TextField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.job')),
            ],
        ),
    ]
