from django import forms

class RecentProduct(forms.Form):
    mobile = forms.CharField(label="Enter Mobile Name")
    laptop = forms.CharField(label="Enter Laptop Name")
    email = forms.EmailField(initial="demo@gmail.com")
    password = forms.CharField(widget=forms.PasswordInput)
    about = forms.CharField(label="About", widget=forms.Textarea, help_text="Enter your details")  