# Generated by Django 3.1 on 2021-08-03 23:22

from django.db import migrations, models
import django.db.models.deletion
import onlinestoreapp.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Category Name', max_length=250, verbose_name='Category Name')),
                ('description', models.CharField(help_text='Category Description', max_length=500, verbose_name='Category Description')),
                ('parent', models.ManyToManyField(blank=True, related_name='sub_categories', to='onlinestoreapp.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Product Name', max_length=250, verbose_name='Product Name')),
                ('description', models.CharField(help_text='Product Description', max_length=500, verbose_name='Product Description')),
                ('amount', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='categories', to='onlinestoreapp.Category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Shop Name', max_length=250, verbose_name='Shop Name')),
                ('description', models.CharField(help_text='Shop Description', max_length=500, verbose_name='Shop Description')),
                ('image_url', models.URLField(help_text='Shop Picture', max_length=300, verbose_name='Shop Picture')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinestoreapp.product')),
            ],
            options={
                'verbose_name_plural': 'Shops',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=onlinestoreapp.utils.get_image_filename)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinestoreapp.product')),
            ],
        ),
    ]
