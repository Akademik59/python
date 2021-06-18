from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'captcha')
        widgets = {
            "name": forms.TextInput(attrs={"class": "reviews_input"}),
            "email": forms.EmailInput(attrs={"class": "reviews_input"}),
            "text": forms.Textarea(attrs={"class": "reviews_input btm", "id": "contactcomment"})
        }
