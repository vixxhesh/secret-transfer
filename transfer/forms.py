from django import forms
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']

class UniqueCodeForm(forms.Form):
    unique_code = forms.UUIDField()
