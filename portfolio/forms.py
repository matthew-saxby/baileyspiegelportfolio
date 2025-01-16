from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=50, 
        required=True, 
        label="First Name", 
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name", "class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=50, 
        required=True, 
        label="Last Name", 
        widget=forms.TextInput(attrs={"placeholder": "Enter your last name", "class": "form-control"})
    )
    email = forms.EmailField(
        required=True, 
        label="Your Email", 
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address", "class": "form-control"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Write your message here", "rows": 5, "class": "form-control"}), 
        required=True, 
        label="Message"
    )
    honeypot = forms.CharField(
        required=False, 
        widget=forms.HiddenInput, 
        label="Leave empty"
    )

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if honeypot:
            raise forms.ValidationError("Spam detected.")
        return honeypot
