from django import forms
from Blog.models import *
from froala_editor.widgets import FroalaEditor

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude  = ['slug']

        widgets = {
            'MainCat': forms.Select(attrs={'class': 'form-control'}),
            'SubCat': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content':FroalaEditor(attrs={
                'class': 'fr-view',  # Add a custom class
            }),
            'pre_content':forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Enter the description'}),
            'Author': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        


class UpdateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude  = ['slug']

        widgets = {
            'MainCat': forms.Select(attrs={'class': 'form-control m-3'}),
            'SubCat': forms.Select(attrs={'class': 'form-control m-3'}),
            'title': forms.TextInput(attrs={'class': 'form-control m-3', 'placeholder': 'Enter the title'}),
            'content':FroalaEditor(attrs={
                'class': 'fr-view',  # Add a custom class
            }),
            'pre_content': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file m-3'}),
        }
        





        