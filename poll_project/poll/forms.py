from django import forms
from .models import Poll


class PollForm(forms.ModelForm):

    language = forms.ModelChoiceField(
        queryset=Poll.objects.all(),
        empty_label="Select a language"
    )

    class Meta:
        model = Poll
        fields = ['language']