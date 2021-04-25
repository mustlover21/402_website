from django import forms
#from django.forms import modelformset_factory
from . import models
from .models import Event, Position, ClaimedPosition

class CreateEvent(forms.ModelForm):
    class Meta:
        model = models.Event
        fields ='__all__'
        #fields = ['eventTitle', 'eventDate', 'startTime', 'endTime', 'address', 'city', 'state', 'zip', ]

class ClaimPosition(forms.ModelForm):
    inner_qs = ClaimedPosition.objects.all()
    #available_positions_list = Position.objects.exclude(id__in=inner_qs)
    available_positions_list = Position.objects.exclude(claimedposition__in=inner_qs)
    positionID = forms.ModelChoiceField(queryset=available_positions_list, label="Position")
    class Meta:
        model = models.ClaimedPosition
        fields = ['positionID']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.queryset = ClaimPosition.objects.filter(Donation.objects.filter(claimeddonation = None))
