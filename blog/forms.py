from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Service

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
)


class Contact(forms.ModelForm):
    # category =  forms.ModelChoiceField(queryset=Category.objects.all().order_by('pk'))
    #
    service = forms.ModelMultipleChoiceField(label="Service", widget=forms.CheckboxSelectMultiple, queryset=Service.objects.all().order_by('pk'))
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'service',
                  'subject', 'body')
