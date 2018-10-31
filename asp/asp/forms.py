from django import forms
from asp.models import Hospital

def getHospitalNames():
    return Hospital.objects.all().values_list('id', 'name')

class SignupForm(forms.Form):
    CLINIC_MANAGER = 'CM'
    DISPATCHER = 'DP'
    WAREHOUSE_PERSONNEL = 'WP'
    ADMIN = 'AD'
    ROLES = (
        (CLINIC_MANAGER, 'Clinic Manager'),
        (DISPATCHER, 'Dispatcher'),
        (WAREHOUSE_PERSONNEL, 'Warehouse Personnel'),
        (ADMIN, 'Admin')
    )

    username = forms.CharField(label='name', max_length = 50)
    password = forms.CharField(label='password', max_length = 50)
    email = forms.EmailField(max_length = 254)
    hospital = forms.ChoiceField(choices=getHospitalNames())
    role = forms.ChoiceField(choices = ROLES)

class LoginForm(forms.Form):
    username = forms.CharField(label='name', max_length = 50)
    password = forms.CharField(label='password', max_length = 50)