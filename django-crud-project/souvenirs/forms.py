from django import forms  
from souvenirs.models import BookingRecords
from django.forms import fields

class BookingForm(forms.ModelForm):  
    class Meta:  
        model = BookingRecords 
        fields = "__all__"  