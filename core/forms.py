from django import forms
from core.models import Activity



class BottleForm(forms.Form):
    activity_type = 'BT'
    
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        passclass Meta:
        model = 
        fields = ('activity_type',)

class NewActivityForm(forms.Form):
    task = forms.CharField(
        label='Task',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'add a new task'}))

    def save(self, **kwargs):
        if self.is_valid():
            task_props = {"description": self.cleaned_data['task']}
            task_props.update(kwargs)
            return Task.objects.create(**task_props)
        return None

class VisitForm(forms.Form):
    
    class Meta:
        model = Visit
        fields = ['check_in','check_out', 'child', 'comment']