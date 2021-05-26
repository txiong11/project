from django import forms
from .models import Profile

#this use to dispay the form for update
class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'bio', 'avatar', 'country')