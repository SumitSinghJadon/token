# Generated by Django 5.0.4 on 2024-04-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_name', models.CharField(max_length=50)),
                ('Emp_salary', models.IntegerField()),
                ('Emp_contact', models.IntegerField()),
                ('Emp_Address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_fees', models.IntegerField()),
                ('stu_contact', models.IntegerField()),
                ('stu_Address', models.CharField(max_length=50)),
            ],
        ),
    ]
