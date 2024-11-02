from django import forms
from .models import Publication


class AddPublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5})
        }
