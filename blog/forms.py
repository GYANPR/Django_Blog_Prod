from django import forms
from .models import Comment


# Since the form input will be saved in the database models we are gonna use the Django’s ModelForm.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']


"""
    By default, Django will generate a form dynamically from all fields of the model 
    but we can explicitly define the fields we want the forms to have, 
    that is what fields attribute is doing here.
    
"""