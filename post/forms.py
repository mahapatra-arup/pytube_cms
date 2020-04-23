from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    #Edit particular Field
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your comments',
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        model = Comments
        fields = ('content', )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        
        