from django import forms
from .models import CandidatiUomo


class CandidatiUomoVotes(forms.ModelForm):


    class Meta:
        model= CandidatiUomo
        fields= ['votes']