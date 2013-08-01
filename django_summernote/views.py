from django.shortcuts import render


def editor(request, id):
    return render(request, 'django_summernote/editor.html', {'id': id})
