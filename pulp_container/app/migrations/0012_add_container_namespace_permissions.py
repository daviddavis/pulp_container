# Generated by Django 2.2.17 on 2020-12-22 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0011_add_container_repository_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='containernamespace',
            options={'permissions': [('manage_namespace_distributions', 'Can manage distributions in a namespace')]},
        ),
    ]
