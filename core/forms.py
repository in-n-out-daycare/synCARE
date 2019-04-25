from django import forms
from core.models import Activity, Visit


class CommentForm(forms.Form):
    comment = forms.CharField()

    def clean_comment(self):
        data = self.cleaned_data['comment']

        return data
