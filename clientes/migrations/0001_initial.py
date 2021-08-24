# Generated by Django 3.2.5 on 2021-07-16 12:55


from django.db import migrations, models

# Prepara a migração: python manage.py makemigrations
# Depois realiza a migraçã: python manage.py migrate

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=3, max_digits=5)),
                ('bio', models.TextField()),
            ],
        ),
    ]
