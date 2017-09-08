# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SampleForm(forms.Form):
    desc1 = forms.CharField(
        label='',
        widget=SummernoteWidget()
    )
    desc2 = forms.CharField(
        label='',
        widget=SummernoteInplaceWidget()
    )


def index(request):
    return render(request, 'index.html', {
        'desc1': request.POST.get('desc1'),
        'desc2': request.POST.get('desc2'),
        'form': SampleForm(),
    })
