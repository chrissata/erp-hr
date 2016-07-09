#encoding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# system arguments
class SystemArg(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    text = models.CharField(max_length=255)
    comment = models.CharField(max_length=127, null=True, blank=True)



class Company(models.Model):
    cid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255, unique=True)
    ctype = models.IntegerField()
    superior = models.ForeignKey('self')



class Project(models.Model):
    pid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255, unique=True)
    company = models.ForeignKey(Company, verbose_name=u'隶属公司')
    size = models.ForeignKey(SystemArg, verbose_name=u'项目规模', related_name='projectSize')
    ifOversea = models.BooleanField(default=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)




class Employee(models.Model):
    sapId = models.CharField(max_length=8, unique=True)
    idNumber = models.CharField(max_length=18, null=True, blank=True, unique=True)
    name = models.CharField(max_length=255)
    positionStatus = models.ForeignKey(SystemArg,verbose_name=u'岗位状态', related_name='positionStatus')
    company = models.ForeignKey(Company, verbose_name=u'人事子范围')
    etype = models.ForeignKey(SystemArg, verbose_name=u'人员组', related_name='eType')#人员组
    position = models.CharField(max_length=255)
    gender = models.ForeignKey(SystemArg, verbose_name=u'性别', related_name='gender')
    birthday = models.DateField()
    rationality = models.ForeignKey(SystemArg, verbose_name=u'民族', related_name='rationality')
    hometown = models.CharField(max_length=255)
    country = models.ForeignKey(SystemArg, verbose_name=u'国籍', related_name='country')
    education = models.ForeignKey(SystemArg, verbose_name=u'学历', related_name='educationalBackground')#学历
    graduateDate = models.DateField()
    school = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    workDate = models.DateField()
    positionType = models.ForeignKey(SystemArg, verbose_name=u'职位序列', related_name='positionType')#职位序列
    rank = models.ForeignKey(SystemArg, verbose_name=u'职级', related_name='rank') # 职级
    title = models.ForeignKey(SystemArg, verbose_name=u'职称', blank=True, null=True, related_name='title')#职称
    workerTitle = models.ForeignKey(SystemArg, verbose_name=u'职业技能等级', blank=True, null=True, related_name='workerTitle')
    profession = models.ForeignKey(SystemArg, verbose_name=u'所从事专业', related_name='professionIn')
    projectId = models.ForeignKey(Project)
    projectPosition = models.ForeignKey(SystemArg, verbose_name=u'项目职位', related_name='positionPosition', blank=True, null=True)



