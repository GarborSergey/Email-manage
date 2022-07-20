from django import forms

from .models import Recipient, Company, Position


class MailForm(forms.Form):
    subject = forms.CharField(max_length=400, label='subject')
    message = forms.CharField(widget=forms.Textarea, label='message')


class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient
        fields = [
            'first_name',
            'last_name',
            'email',
            'position',
            'company',
        ]


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = [
            'name'
        ]


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = [
            'name'
        ]
