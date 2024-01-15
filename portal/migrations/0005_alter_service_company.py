# Generated by Django 4.2.7 on 2024-01-10 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0004_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='事業者'),
        ),
    ]