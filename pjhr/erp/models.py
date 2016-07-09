# encoding:utf-8
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
    IDNumber = models.CharField(max_length=18, null=True, blank=True, unique=True)  # 身份证号
    name = models.CharField(max_length=255)
    positionStatus = models.ForeignKey(SystemArg, verbose_name=u'岗位状态', related_name='positionStatus')
    company = models.ForeignKey(Company, verbose_name=u'人事子范围')
    etype = models.ForeignKey(SystemArg, verbose_name=u'人员组', related_name='eType')  # 人员组
    position = models.CharField(max_length=255)
    gender = models.ForeignKey(SystemArg, verbose_name=u'性别', related_name='gender')
    birthday = models.DateField()
    rationality = models.ForeignKey(SystemArg, verbose_name=u'民族', related_name='rationality')
    hometown = models.CharField(max_length=255)
    country = models.ForeignKey(SystemArg, verbose_name=u'国籍', related_name='country')
    education = models.ForeignKey(SystemArg, verbose_name=u'学历', related_name='educationalBackground')  # 学历
    graduateDate = models.DateField()
    school = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    workDate = models.DateField()
    positionType = models.ForeignKey(SystemArg, verbose_name=u'职位序列', related_name='positionType')  # 职位序列
    rank = models.ForeignKey(SystemArg, verbose_name=u'职级', related_name='rank')  # 职级
    title = models.ForeignKey(SystemArg, verbose_name=u'职称', blank=True, null=True, related_name='title')  # 职称
    workerTitle = models.ForeignKey(SystemArg, verbose_name=u'职业技能等级', blank=True, null=True,
                                    related_name='workerTitle')
    profession = models.ForeignKey(SystemArg, verbose_name=u'所从事专业', related_name='professionIn')
    projectId = models.ForeignKey(Project)
    projectPosition = models.ForeignKey(SystemArg, verbose_name=u'项目职位', related_name='positionPosition', blank=True,
                                        null=True)


class SalaryStandard(models.Model):
    # sapId = models.CharField(max_length=8, unique = True)
    employee = models.ForeignKey(Employee) #员工编号
    basicSalary = models.FloatField()

    subsidy1 = models.FloatField()  # 资质津贴
    subsidy2 = models.FloatField()  # 大车津贴
    subsidy3 = models.FloatField()  # 高技能津贴
    subsidy4 = models.FloatField()  # 班长津贴
    subsidy5 = models.FloatField()  # 住房补贴
    subsidyAdjust = models.FloatField()  # 津补贴补发补扣

    bound1 = models.FloatField()  # 兑现奖
    bound2 = models.FloatField()  # 绩效奖
    bound3 = models.FloatField()  # 考核奖
    bound4 = models.FloatField()  # 计件奖
    bound5 = models.FloatField()  # 年终及其他奖金
    boundAdjust = models.FloatField()  # 奖金补发补扣

    wageAdjust = models.FloatField()  # 应发调整

    insuranceBase = models.FloatField()  # 社保基数
    houseFundBase = models.FloatField()  # 公积金基数
    annuityBase = models.FloatField() #年金基数

    tax = models.FloatField() #个税计算
    afterTaxAdjust = models.FloatField() #税后补发扣减




class SalaryTemplate(models.Model):
    company = models.ForeignKey(Company)
    pPensionRatio = models.FloatField() #个人养老缴费比例
    ePensionRatio = models.FloatField() #企业养老缴费比例
    pHealthRatio  = models.FloatField() #个人医疗缴费比例
    eHealthRatio  = models.FloatField() #企业医疗缴费比例
    pBirthRatio = models.FloatField() #个人生育缴费比例
    eBirthRatio = models.FloatField() #企业生育缴费比例
    pJobRatio = models.FloatField()  #个人失业缴费比例
    eJobRatio = models.FloatField()  #企业失业缴费比例
    pInjuryRatio = models.FloatField() #个人工伤缴费比例
    eInjuryRatio =  models.FloatField() #企业工伤缴费比例
    pHouseFundRatio = models.FloatField() #个人公积金缴费比例
    eHouseFundRatio = models.FloatField() #企业公积金缴费比例
    pAnnuityRatio = models.FloatField() #个人年金缴费比例
    eAnnuityRatio = models.FloatField() #企业年金缴费比例


class Attendance(models.Model):
    attendDays = models.IntegerField() #出勤天数
    absentDays =  models.IntegerField()  #缺勤天数
    illDays =  models.IntegerField(default = 0) #病假天数
    annualLeaveDays =  models.IntegerField(default= 0) #年休假天数
    pAffairLeaveDays =  models.IntegerField(default=0) #事假天数
    marryLeaveDays =  models.IntegerField(default=0)  #婚假天数
    homeLeaveDays =  models.IntegerField(default=0)  #探亲假天数
    overtimeDays =  models.IntegerField(default=0)  #加班天数




