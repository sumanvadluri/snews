from .models import News_model

from django import forms
from django.core import validators

class News_form(forms.Form):
    error_css_class='error'
    required_css_class='required'

    # class Meta:
    #     model=News_model
    #     fields =['Title','Discription','Image','Category']
            # ['Title','Discription','Image','Category']
    #     widgets = {
    #         'body': forms.Textarea(attrs={'cols': 80, 'rows': 20})
    #     }
    title = forms.CharField(label="Enter Your Title",
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'News Title Name',
                                    'class': 'form-control',
                                    'cols': 80,
                                    'rows': 20
                                }
                            )
                            )

    Discription = forms.CharField(label="Enter title Discription",
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'News Discription ',
                                          'class': 'form-control'
                                      }
                                  ))
    News_resources = forms.CharField(label="Enter Your News-Resources",
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'News resurces',
                                    'class': 'form-control',
                                    'cols': 80,
                                    'rows': 20
                                }
                            )
                            )

    Image = forms.FileField()
    CHOICES = (
        ('ALL','ALL'),
        ('తెలంగాణ', 'తెలంగాణ'),
        ('ఆంధ్రప్రదేశ్', 'ఆంధ్రప్రదేశ్'),
        ('జాతీయం', 'జాతీయం'),
        ('అంతర్జాతీయం', 'అంతర్జాతీయం'),
        ('క్రిడలు', 'క్రిడలు'),
        ('సినిమా', 'సినిమా')
    )
    catogeroy = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    DISPLAY_CHOICES = (
        ("Notification_on", "Notification_on"),
        ("Notification_off", "Notification_off")
    )

    Notification = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)
    DISPLAY_CHOICES2 = (
        ("Image", "Image"),
        ("Video", "Video")
    )

    Upload_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES2)


    def clean_Discription(self):
        inputDiscription=self.cleaned_data['Discription']
        if len(inputDiscription)>500:
            raise forms.ValidationError("Maximum no.of characters 500 pls decreas count")
        return inputDiscription


class Full_image_video_form(forms.Form):
    DISPLAY_CHOICES3 = (
        ("Image", "Image"),
        ("Video", "Video")
    )

    upload_field_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES3)
    Image = forms.FileField()




