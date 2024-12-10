from django import forms
from .models import Announce, Reply
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AnnounceForm(forms.ModelForm):
    text = forms.CharField(label='Текст объявления', widget=CKEditorUploadingWidget())

    class Meta:
        model = Announce
        fields = [
            'category',
            'title',
            'text',
        ]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        labels = {'text': ('Оставьте отклик')}
        widgets = {'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 200, 'rows': 2})}
