from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Necessity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('satisfied', models.BooleanField(default=False, verbose_name='Satisfied')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Organization name', max_length=64, verbose_name='Name')),
                ('description', models.TextField(help_text='Organization description', verbose_name='Description')),
                ('photo', models.ImageField(upload_to='organization_photos', verbose_name='Photo')),
                ('necessity_description', models.TextField(help_text='Text to explain the organization material needs', verbose_name='Necessity description')),
                ('email', models.EmailField(blank=True, help_text='Contact email for the organization', max_length=254, verbose_name='Organization email')),
                ('homepage_url', models.URLField(blank=True, help_text='Organization homepage link', verbose_name='Homepage URL')),
                ('facebook_url', models.URLField(blank=True, help_text='Organization facebook link', verbose_name='Facebook URL')),
                ('twitter_url', models.URLField(blank=True, help_text='Organization twitter link', verbose_name='Twitter URL')),
                ('coordinator', models.ForeignKey(help_text='Person responsible for the organization', on_delete=django.db.models.deletion.CASCADE, to='contributors.Contributor', verbose_name='Coordinator')),
                ('necessities', models.ManyToManyField(to='organizations.Necessity')),
                ('projects', models.ManyToManyField(to='projects.Project')),
            ],
        ),
    ]
