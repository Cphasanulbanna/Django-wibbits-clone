from django import forms
from django.forms import EmailInput, ModelForm, TextInput, Select
from web.models import Contact
from web.models import COMPANY_SIZE, INDUSTRY, JOB_ROLE, COUNTRY

EMPTY_COMPANY_SIZE = (("","Company Size"),) + COMPANY_SIZE
EMPTY_INDUSTRY = (("","industry"),) + INDUSTRY 
EMPTY_JOB_ROLE = (("","Job Role"),) + JOB_ROLE 
EMPTY_COUNTRY = (("","Country"),) + COUNTRY 

class ContactForm(ModelForm):
    company_size = forms.ChoiceField(choices=EMPTY_COMPANY_SIZE)
    industry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job_role = forms.ChoiceField(choices=EMPTY_JOB_ROLE)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder":"Enter Your Email"}),
            "first_name" : TextInput(attrs={"placeholder":"first name"}),
            "last_name" : TextInput(attrs={"placeholder":"last name"}),
            "company" : TextInput(attrs={"placeholder":"company"}),
            "company_size" : Select(attrs={"class":"select"})
        }
