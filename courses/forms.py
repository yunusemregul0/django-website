from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        label="kurs başlığı",
        required=True, 
        error_messages= {
            "required":"kurs başlığı girmelisiniz."}, 
        widget=forms.TextInput(attrs={"class":"form-control"}))
        
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))