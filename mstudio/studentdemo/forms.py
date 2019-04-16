from django import forms

class UserRegistrar(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput( ))
    last_name = forms.CharField(required=True, widget=forms.TextInput( ))
    age = forms.CharField(required=True, widget=forms.TextInput( ))
    date_of_birth = forms.DateTimeField(required=True, widget=forms.TextInput( ))


class DegreeRegistrar(forms.Form):
    Student_Degree= forms.CharField(required=True, widget=forms.TextInput( ))