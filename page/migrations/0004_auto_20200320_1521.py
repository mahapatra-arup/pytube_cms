# Generated by Django 3.0.1 on 2020-03-20 09:51

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20200319_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page.Menu'),
        ),
    ]
