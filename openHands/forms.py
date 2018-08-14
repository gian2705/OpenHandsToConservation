from django import forms
from django.contrib.auth import authenticate

from openHands.models import CustomerReview, Post


class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview

        fields = [
            'name',
            'email',
            'user_contribution'
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=[
            'title',
            'content',
            'uploaded_media',
            'image_caption',

        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password  = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Sorry, You are not registered.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
        return super(LoginForm, self).clean()
