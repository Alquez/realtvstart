# Generated by Django 4.2 on 2023-05-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backgammon',
            options={'verbose_name': 'Матч нарды', 'verbose_name_plural': 'Матчи нарды'},
        ),
        migrations.AlterModelOptions(
            name='sporttype',
            options={'verbose_name': 'Нарды иконка', 'verbose_name_plural': 'Нарды иконка'},
        ),
        migrations.AlterModelOptions(
            name='tournament',
            options={'verbose_name': 'Турнир нарды', 'verbose_name_plural': 'Турниры нарды'},
        ),
        migrations.RemoveField(
            model_name='sporttype',
            name='logo',
        ),
        migrations.AddField(
            model_name='sporttype',
            name='image',
            field=models.ImageField(null=True, upload_to='nard_images/'),
        ),
    ]
