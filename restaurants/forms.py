# -*- coding: utf-8 -*-
from django import forms
from DjangoUeditor.forms import UEditorField

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20, required=False, label='E-mail')
    content = UEditorField(u"评论内容",initial=u"很好吃",width=800,height=100)
    # content = forms.CharField(max_length=200, widget=forms.Textarea())

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 5:
            raise forms.ValidationError(u'字数不足')
        return content