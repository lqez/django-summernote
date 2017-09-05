# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from django_summernote.widgets import SummernoteInplaceWidget


class SampleForm(forms.Form):
    desc = forms.CharField(
        label='',
        widget=SummernoteInplaceWidget()
    )


def index(request):
    return render(request, 'index.html', {
        'submitted': request.POST.get('desc'),
        'form': SampleForm(),
    })
