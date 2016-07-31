from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('date', models.DateField(verbose_name='Date')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.CharField(choices=[('open', 'Open'), ('running', 'Running'), ('closed', 'Closed')], default='open', max_length=7, verbose_name='Status')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Responsible')),
            ],
        ),
    ]
