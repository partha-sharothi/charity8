from .models import WithdrawalHistry,UserProfileInfo
import django_filters

class WithdrawalHistryFilter(django_filters.FilterSet):
    
    class Meta:
        model = WithdrawalHistry
        fields = ['user','date','payment_status','btc_address']
