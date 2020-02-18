from django import forms

class ContactForm(forms.Form):
    #Fields
    contact_name = forms.CharField(max_length=128, required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(max_length=200, required=True, help_text="Enter Your Subject here")
    content = forms.CharField(required=True,widget=forms.Textarea, help_text="Enter Your content here")

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        #place holder
        self.fields['contact_name'].widget.attrs['placeholder'] = "Enter Your Name (Required)"
        self.fields['contact_email'].widget.attrs['placeholder'] = "Enter Your Email (Required)"
        self.fields['contact_subject'].widget.attrs['placeholder'] = "Enter Your Subject (Required)"
        self.fields['content'].widget.attrs['placeholder'] = "What do you want to say?"
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })