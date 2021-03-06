# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendDays', models.IntegerField()),
                ('absentDays', models.IntegerField()),
                ('illDays', models.IntegerField(default=0)),
                ('annualLeaveDays', models.IntegerField(default=0)),
                ('pAffairLeaveDays', models.IntegerField(default=0)),
                ('marryLeaveDays', models.IntegerField(default=0)),
                ('homeLeaveDays', models.IntegerField(default=0)),
                ('overtimeDays', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('ctype', models.IntegerField()),
                ('superior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapId', models.CharField(max_length=8, unique=True)),
                ('IDNumber', models.CharField(blank=True, max_length=18, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('hometown', models.CharField(max_length=255)),
                ('graduateDate', models.DateField()),
                ('school', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('workDate', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Company', verbose_name='\u4eba\u4e8b\u5b50\u8303\u56f4')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('ifOversea', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Company', verbose_name='\u96b6\u5c5e\u516c\u53f8')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basicSalary', models.FloatField()),
                ('subsidy1', models.FloatField()),
                ('subsidy2', models.FloatField()),
                ('subsidy3', models.FloatField()),
                ('subsidy4', models.FloatField()),
                ('subsidy5', models.FloatField()),
                ('subsidyAdjust', models.FloatField()),
                ('bound1', models.FloatField()),
                ('bound2', models.FloatField()),
                ('bound3', models.FloatField()),
                ('bound4', models.FloatField()),
                ('bound5', models.FloatField()),
                ('boundAdjust', models.FloatField()),
                ('wageAdjust', models.FloatField()),
                ('insuranceBase', models.FloatField()),
                ('houseFundBase', models.FloatField()),
                ('annuityBase', models.FloatField()),
                ('tax', models.FloatField()),
                ('afterTaxAdjust', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pPensionRatio', models.FloatField()),
                ('ePensionRatio', models.FloatField()),
                ('pHealthRatio', models.FloatField()),
                ('eHealthRatio', models.FloatField()),
                ('pBirthRatio', models.FloatField()),
                ('eBirthRatio', models.FloatField()),
                ('pJobRatio', models.FloatField()),
                ('eJobRatio', models.FloatField()),
                ('pInjuryRatio', models.FloatField()),
                ('eInjuryRatio', models.FloatField()),
                ('pHouseFundRatio', models.FloatField()),
                ('eHouseFundRatio', models.FloatField()),
                ('pAnnuityRatio', models.FloatField()),
                ('eAnnuityRatio', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='SystemArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
                ('comment', models.CharField(blank=True, max_length=127, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectSize', to='erp.SystemArg', verbose_name='\u9879\u76ee\u89c4\u6a21'),
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='erp.SystemArg', verbose_name='\u56fd\u7c4d'),
        ),
        migrations.AddField(
            model_name='employee',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educationalBackground', to='erp.SystemArg', verbose_name='\u5b66\u5386'),
        ),
        migrations.AddField(
            model_name='employee',
            name='etype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eType', to='erp.SystemArg', verbose_name='\u4eba\u5458\u7ec4'),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender', to='erp.SystemArg', verbose_name='\u6027\u522b'),
        ),
        migrations.AddField(
            model_name='employee',
            name='positionStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positionStatus', to='erp.SystemArg', verbose_name='\u5c97\u4f4d\u72b6\u6001'),
        ),
        migrations.AddField(
            model_name='employee',
            name='positionType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positionType', to='erp.SystemArg', verbose_name='\u804c\u4f4d\u5e8f\u5217'),
        ),
        migrations.AddField(
            model_name='employee',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professionIn', to='erp.SystemArg', verbose_name='\u6240\u4ece\u4e8b\u4e13\u4e1a'),
        ),
        migrations.AddField(
            model_name='employee',
            name='projectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='projectPosition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positionPosition', to='erp.SystemArg', verbose_name='\u9879\u76ee\u804c\u4f4d'),
        ),
        migrations.AddField(
            model_name='employee',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rank', to='erp.SystemArg', verbose_name='\u804c\u7ea7'),
        ),
        migrations.AddField(
            model_name='employee',
            name='rationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rationality', to='erp.SystemArg', verbose_name='\u6c11\u65cf'),
        ),
        migrations.AddField(
            model_name='employee',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='title', to='erp.SystemArg', verbose_name='\u804c\u79f0'),
        ),
        migrations.AddField(
            model_name='employee',
            name='workerTitle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workerTitle', to='erp.SystemArg', verbose_name='\u804c\u4e1a\u6280\u80fd\u7b49\u7ea7'),
        ),
    ]
