# Generated by Django 2.1.7 on 2019-03-28 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20190328_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddID',
            fields=[
                ('this_rid', models.IntegerField(primary_key=True, serialize=False)),
                ('this_date', models.DateField()),
                ('this_summary', models.TextField(null=True)),
                ('this_pros', models.TextField(null=True)),
                ('this_cons', models.TextField(null=True)),
                ('this_advices_to_management', models.TextField(null=True)),
                ('this_overall_ratings', models.CharField(max_length=10)),
                ('this_work_balance_stars', models.CharField(max_length=10)),
                ('this_culture_values_stars', models.CharField(max_length=10)),
                ('this_career_opportunities_stars', models.CharField(max_length=10)),
                ('this_company_benefit_stars', models.CharField(max_length=10)),
                ('this_senior_management_stars', models.CharField(max_length=10)),
                ('this_helpful_count', models.IntegerField()),
                ('this_cid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basic_app.Company')),
                ('this_pid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basic_app.Position')),
                ('this_uid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basic_app.UserProfileInfo')),
            ],
        ),
    ]