from django import forms

# class AddressForm(forms.Form):
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput())
#     address_1 = forms.CharField(
#         label='Address',
#         widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
#     )
#     address_2 = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
#     )
#     city = forms.CharField()
#     state = forms.ChoiceField(choices=STATES)
#     zip_code = forms.CharField(label='Zip')
#     check_me_out = forms.BooleanField(required=False)

class ContactUsForm(forms.Form):
    #Fields
    name = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True, )#help_text="Enter Your Subject here"
    content = forms.CharField(required=True,widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #place holder
        self.fields['name'].widget.attrs['placeholder'] = "Enter Your Name (Required)"
        self.fields['email'].widget.attrs['placeholder'] = "Enter Your Email (Required)"
        self.fields['subject'].widget.attrs['placeholder'] = "Enter Your Subject (Required)"
        self.fields['content'].widget.attrs['placeholder'] = "What do you want to say?"
        
        