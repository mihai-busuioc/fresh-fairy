from django import forms
from .widgets import CustomClearableFileInput
from .models import Services, Review


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'


class ReviewForm(forms.ModelForm):
    """Create review form."""
    class Meta:
        model = Review
        fields = [
            'title',
            'review_text'
        ]

    title = forms.CharField(
        required=True,
        label='Title',
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control border-black rounded-3',
        })
    )

    review_text = forms.CharField(
        required=True,
        label='Review',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control border-black rounded-3',
        })
    )
