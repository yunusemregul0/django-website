# Generated by Django 4.0.3 on 2022-11-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_course_category_course_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isHome',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
