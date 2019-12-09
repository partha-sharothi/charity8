import django_tables2 as tables
from .models import UserProfileInfo, Histry , WithdrawalHistry

class UserInfoTable(tables.Table):
    # username = tables.Column(linkify=("member:details", {"pk": tables.A("pk")}))

    class Meta:
        model = UserProfileInfo
        template_name = 'django_tables2/bootstrap.html'
        fields = ('user_profile.username', 'sponsor','phone_number')

class SingleLegUserTable(tables.Table):
    class Meta:
        model = UserProfileInfo
        template_name = 'django_tables2/bootstrap.html'
        fields = ('user_profile.username','country.country','country.flag')

class HistryTable(tables.Table):
    class Meta:
        model = Histry
        template_name = 'django_tables2/bootstrap.html'
        fields = ('invoice_date','person','level_income','refferal_level_income','reward','withdrawal') 


class  WithdrawalHistryTable(tables.Table):
    class Meta:
        model = WithdrawalHistry
        template_name = 'django_tables2/bootstrap.html'
        fields = ('btc_address', 'ammount', 'date', 'payment_status')