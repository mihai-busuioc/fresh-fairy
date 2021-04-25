from django import forms
from .models import Services


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'
