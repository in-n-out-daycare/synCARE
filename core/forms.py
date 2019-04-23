from django import forms
from core.models import Activity, Visit


class CommentForm(forms.Form):
    comment = forms.CharField(help_text="Put any teacher comments here (i.e. Need more diapers.)")

    def clean_comment(self):
        data = self.cleaned_data['comment']

        return data
