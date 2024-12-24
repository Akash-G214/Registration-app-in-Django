from django.forms import ModelForm
from learnapp.models import Person

class PersonForm(ModelForm):
    class Meta:
        model=Person 
        fields='__all__'