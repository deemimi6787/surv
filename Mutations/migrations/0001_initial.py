# Generated by Django 3.0.5 on 2020-10-02 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('idNo', models.IntegerField()),
                ('phoneNo', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mutation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('idNumber', models.CharField(max_length=100)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mutations.Register')),
            ],
        ),
    ]
