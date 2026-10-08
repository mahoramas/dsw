from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
