from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import get_object_or_404

from datetime import datetime
from datetime import timedelta 

from django.contrib.auth.models import User
import pytz

utc=pytz.UTC





# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,name='user_profile')
    phone_number = PhoneNumberField()
    confirm = models.BooleanField(default=False)
    confirmation_date = models.DateTimeField( null=True, blank=True)
    application_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sponsor = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE,null=True, blank=True, related_name ='sponsored' )
    country = models.ForeignKey('Country',on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    # wallet = models.OneToOneField('EWallet',on_delete='CASCADE',null=True, blank=True)
    account = models.FloatField(default=0)
    refferal_level_income =  models.FloatField(default=0)
    # refferal_level_income_date = models.DateTimeField(null=True, blank=True)
    level_income = models.FloatField(default=0)
    # level_income_date = models.DateTimeField(null=True, blank=True)
    user_activation = models.BooleanField(default=False)
    btc_activation = models.BooleanField(default=False)


    
    def __str__(self):
        return self.user_profile.username

    def user_confirmation(self):
        self.confirm = True
        self.confirmation_date = utc.localize(datetime.now())
        self.active = True
        self.save()
        return None

    def level_bonus(self):
        user = self.user
        user = get_object_or_404(UserProfileInfo, user_profile=user)
        
        name = user
        name1 = list(name.sponsored.filter(confirm=True))
        name2 = []
        name3 = []
        name4 = []
        name5 = []
        name6 = []
        name7 = []
        name8 = []
        name9 = []
        name10 = []
        for x1 in name1:
            name2 += list(x1.sponsored.filter(confirm=True))
        for x2 in name2:
            name3 += list(x2.sponsored.filter(confirm=True))
        for x3 in name3:
            name4 += list(x3.sponsored.filter(confirm=True))
        for x4 in name4:
            name5 += list(x4.sponsored.filter(confirm=True))
        for x5 in name5:
            name6 += list(x5.sponsored.filter(confirm=True))
        for x6 in name6:
            name7 += list(x6.sponsored.filter(confirm=True))
        for x7 in name7:
            name8 += list(x7.sponsored.filter(confirm=True))
        for x8 in name8:
            name9 += list(x8.sponsored.filter(confirm=True))
        for x9 in name9:
            name10 += list(x9.sponsored.filter(confirm=True))

        refferal_bonus=((float(len(name1))*(50.0*10/100))+(float(len(name2))*(50.0*4/100))+(float(len(name3))*(50.0*2/100))+
            (float(len(name4))*(50.0*2/100))+(float(len(name5))*(50*1/100))+
            (float(len(name6))*(50.0*1/100))+(float(len(name7))*(50.0*1/200))+(float(len(name8))*(50.0*1/200))+
            (float(len(name9))*(50.0*1/200))+(float(len(name10))*(50.0*1/200)))
        # import pdb;pdb.set_trace()
        if refferal_bonus>user.refferal_level_income:
            x = user.refferal_level_income
            user.refferal_level_income += (refferal_bonus-x)
            user.account += (refferal_bonus-x) 
            create_histry(user=user,refferal_level_income=(refferal_bonus-x) ,refferal_level_income_date=utc.localize(datetime.now()))        
            user.save()

        return refferal_bonus         




class Country(models.Model):
    country = models.CharField(max_length=150)
    flag = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.country


class Activity(models.Model):
    level = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE, null=True, blank=True)
    level_status = models.BooleanField(default=False)

    def level_status_check(self):
        if self.level_status == False:
            if (self.end_date) <= utc.localize(datetime.now()):
                self.level_status = True
                level = self.level
                profileinfo = get_object_or_404(User, userprofileinfo=self.user)
                user_info =get_object_or_404(UserProfileInfo, user_profile=profileinfo)
                user_account = user_info.account
                user_level_income = user_info.level_income
                values = income_complit_level(user_info,level, user_account, user_level_income)
                user_info.account = values['account']
                user_info.level_income = values['level_income']
                user_info.save()
                
                self.save()
            
        return None  

    def __str__(self):
        return self.user.user_profile.username  




# class EWallet(models.Model):
#     ammount = models.IntegerField(default=0)


def income_complit_level(user,level,account,level_income):
    if level == 1:
        account = account + 20      
        create_histry(user=user, level_income=20, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +20
        
    elif level == 2:
        account = account +30
        create_histry(user=user, level_income=30, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +30

    elif level == 3:
        account = account +80
        create_histry(user=user, level_income=80, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +80

    elif level == 4:
        account = account + 120
        create_histry(user=user, level_income=120, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +120

    elif level == 5:
        account = account +190
        create_histry(user=user, level_income=190, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +190

    elif level == 6:
        account = account +250
        create_histry(user=user, level_income=250, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +250

    elif level == 7:
        account = account +400
        create_histry(user=user, level_income=400, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +400
    elif level == 8:
        account = account +700
        create_histry(user=user, level_income=700, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +700

    elif level == 9:
        account = account +900
        create_histry(user=user, level_income=900, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +900

    elif level == 10:
        account = account +1300
        create_histry(user=user, level_income=1300, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +1300

    elif level == 11:
        account = account +2000
        create_histry(user=user, level_income=2000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +2000

    elif level == 12:
        account = account +4000
        create_histry(user=user, level_income=4000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +4000

    elif level == 13:
        account = account + 6000
        create_histry(user=user, level_income=6000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +6000

    elif level == 14:
        account = account + 9000
        create_histry(user=user, level_income=9000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +9000

    elif level == 15:
        account = account +12000
        create_histry(user=user, level_income=12000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +12000

    elif level == 16:
        account = account +15000
        create_histry(user=user, level_income=15000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +15000

    elif level == 17:
        account = account +18000
        create_histry(user=user, level_income=18000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +18000

    elif level == 18:
        account = account +30000
        create_histry(user=user, level_income=30000, level_income_date=utc.localize(datetime.now()))
        level_income = level_income +30000

    values = {'account':account, 'level_income':level_income}

    return values


class Histry(models.Model):
    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE,null=True, blank=True)
    person = models.CharField(max_length=250,null=True, blank=True)
    date_of_activation = models.DateTimeField(null=True, blank=True)
    level_income = models.FloatField(null=True, blank=True)
    level_income_date = models.DateTimeField(null=True, blank=True)
    refferal_level_income = models.FloatField(null=True, blank=True)
    refferal_level_income_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    reward = models.CharField(max_length=250,null=True, blank=True)
    rewarded_date = models.DateTimeField(null=True, blank=True)
    withdrawal = models.FloatField(null=True, blank=True)
    withdrawal_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.user_profile.username


def create_histry(user,**kwarg):
    histry = Histry.objects.create()
    histry.user = user
    # import pdb; pdb.set_trace()
    if 'person' in kwarg:
        histry.person = kwarg['person']

    if 'date_of_activation' in kwarg:       
        histry.date_of_activation = kwarg['date_of_activation']

    if 'level_income' in kwarg:        
        histry.level_income = kwarg['level_income']

    if 'level_income_date' in kwarg:        
        histry.level_income_date = kwarg['level_income_date']

    if 'refferal_level_income' in kwarg:        
        histry.refferal_level_income = kwarg['refferal_level_income']

    if 'refferal_level_income_date' in kwarg:
        histry.refferal_level_income_date = kwarg['refferal_level_income_date']
    
    if 'reward' in kwarg:
        histry.reward = kwarg['reward']

    if 'rewarded_date' in kwarg:        
        histry.rewarded_date = kwarg['rewarded_date']

    if 'withdrawal' in kwarg:        
        histry.withdrawal = kwarg['withdrawal']

    if 'withdrawal_date' in kwarg:        
        histry.withdrawal_date = kwarg['withdrawal_date']    
    

    histry.save()

    return None




class WithdrawalHistry(models.Model):

    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    )
    
    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE,null=True, blank=True)
    btc_address = models.CharField(max_length=250, null=True, blank=True)
    ammount = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.user.user_profile.username




class Support(models.Model):

    SUPPORT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('complete', 'Complete'),
        ('seen', 'Seen'),
    )


    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE,null=True, blank=True)
    subject = models.TextField()
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    support_status = models.CharField(max_length=50, choices=SUPPORT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.user.user_profile.username


    
class BtcAddress(models.Model):
    user = models.OneToOneField('UserProfileInfo', on_delete=models.CASCADE,null=True, blank=True)
    btc_address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.user_profile.username