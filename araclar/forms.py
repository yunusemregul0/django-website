from django import forms
from django.forms import SelectMultiple, TextInput, Textarea

from araclar.models import araclar, marka

# class aracolustur(forms.Form):
#     title = forms.CharField(
#         label="kurs başlığı",
#         required=True, 
#         error_messages= {
#             "required":"kurs başlığı girmelisiniz."}, 
#         widget=forms.TextInput(attrs={"class":"form-control"}))
        
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))

class aracolustur(forms.ModelForm):
    class Meta:
        model = araclar
        fields = ('title','description','image','slug')
        labels = {
            'title':"Arac Markası",
            'description':'açıklama'
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required":"arac markası girmelisiniz",
                "max_length": "maksimum 50 karakter girmelisiniz"
            },
            "description": {
                "required":"araç açıklaması gereklidir."
            }
        }
        
class arabaduzenleme(forms.ModelForm):
    class Meta:
        model = araclar
        fields = ('title','description','image','slug','marka','isActive')
        labels = {
            'title':"Araç Markası",
            'description':'açıklama'
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            "marka": SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required":"araç markası girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz"
            },
            "description": {
                "required":"araç açıklaması gereklidir."
            }
        }
        

class UploadForm(forms.Form):
    image = forms.ImageField()
    