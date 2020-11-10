from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200, label="Email subject", help_text='Insert your subject', initial='Subject')
    name = forms.CharField(max_length=100, label="Full name", help_text="Insert your full name")
    sender = forms.EmailField(label='Email address', help_text="Insert your email address")
    cc = forms.BooleanField(required=False)
    message = forms.CharField(widget=forms.Textarea, help_text="Insert your message.")