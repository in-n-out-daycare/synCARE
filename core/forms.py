from django import forms
from core.models import Activity

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('activity_type',)