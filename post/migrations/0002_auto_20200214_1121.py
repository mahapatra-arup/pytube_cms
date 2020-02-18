# Generated by Django 3.0.1 on 2020-02-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_on'], 'verbose_name': 'Post', 'verbose_name_plural': 'Post'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tag'},
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Drafted', 'Drafted'), ('Published', 'Published'), ('Rejected', 'Rejected')], default='Published', max_length=10),
        ),
        migrations.AlterModelTable(
            name='post',
            table='Post',
        ),
    ]
