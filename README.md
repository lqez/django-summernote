django-summernote
=================

[Summernote](https://github.com/HackerWins/summernote) is a simple WYSIWYG editor based on Twitter's Bootstrap.

`django-summernote` plugin allows you to embed Summernote into your Django admin page very handy.

![django-summernote](https://raw.github.com/lqez/pastebin/master/img/django-summernote.png "Screenshot of django-summernote")



SETUP
-----

1. Install `django-summernote` to your python environment.

        pip install django-summernote

2. Add `django_summernote` to `INSTALLED_APP` in `settings.py`.

        INSTALLED_APPS += ('django_summernote')

3. Add `django_summernote.urls` to `urls.py`.

        urlpatterns = patterns('',
            ...
            (r'^summernote/', include('django_summernote.urls')),
            ...
        )

USAGE
-----

1. In `admin.py`,

        from django_summernote.admin import SummernoteModelAdmin

        # Apply summernote to all TextField in model.
        class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
            ...

2. Or, in `forms`,

        from django_summernote.widgets import SummernoteWidget

        # Apply summernote to specific fields.
        class SomeForm(forms.Form):
            foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea


OPTIONS
-------

(under development)


AUTHOR
------

Park Hyunwoo([@lqez](https://twitter.com/lqez))


LICENSE
-------

Distributed under MIT license.
