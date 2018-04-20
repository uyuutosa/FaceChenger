from django import forms
from app.models import UploadFile

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000)
    sender  = forms.EmailField()

#class ContactForm(forms.Form):
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField(max_length=1000)
#    sender  = forms.EmailField()


class HelloForm(forms.Form):
    your_name = forms.CharField(
            label='名前',
            max_length=20,
            required=True,
            widget=forms.TextInput()
    )

#class ImageForm(forms.Form):
#    raw_image = forms.ImageField('raw', upload_to='images/')
#    clipped_image = forms.ImageField('clipped', upload_to='images/')
#    result_image = forms.ImageField('result', upload_to='images/')

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file')

class CheckForm(forms.Form):
    bald = forms.BooleanField(
        label='Bald',
        widget = forms.CheckboxInput(attrs={'id':'bald'}),
        required=False,
#        widget=forms.CheckboxInput(attrs={'class':'check'}),
    )

    black_hair = forms.BooleanField(
        label='Black Hair',
        widget = forms.CheckboxInput(attrs={'id':'Black_Hair'}),
        required=False,
#        widget=forms.CheckboxInput(attrs={'class':'check'}),
    )

    blond_hair = forms.BooleanField(
        label='Blond Hair',
        widget = forms.CheckboxInput(attrs={'id':'Blond_Hair'}),
        required=False,
#        widget=forms.CheckboxInput(attrs={'class':'check'}),
    )

    brown_hair = forms.BooleanField(
        label='Brown Hair',
        widget = forms.CheckboxInput(attrs={'id':'Brown_Hair'}),
        required=False,
    )

    gray_hair = forms.BooleanField(
        label='Gray Hair',
        widget = forms.CheckboxInput(attrs={'id':'Gray_Hair'}),
        required=False,
    )

    male = forms.BooleanField(
        label='Male',
        widget = forms.CheckboxInput(attrs={'id':'Male'}),
        required=False,
    )

    straight_hair = forms.BooleanField(
        label='Strait Hair',
        widget = forms.CheckboxInput(attrs={'id':'Strait_Hair'}),
        required=False,
    )

    Wavy_hair = forms.BooleanField(
        label='Wavy Hair',
        widget = forms.CheckboxInput(attrs={'id':'Wavy_Hair'}),
        required=False,
    )

    young = forms.BooleanField(
        label='Young',
        widget = forms.CheckboxInput(attrs={'id':'young'}),
        required=False,
    )

