django-summernote
=================
[![Build Status](https://travis-ci.org/lqez/django-summernote.png?branch=master)](https://travis-ci.org/lqez/django-summernote)

[Summernote](https://github.com/HackerWins/summernote) is a simple WYSIWYG editor based on Twitter's Bootstrap.

`django-summernote` plugin allows you to embed Summernote into your Django admin page very handy.

![django-summernote](https://raw.github.com/lqez/pastebin/master/img/django-summernote.png "Screenshot of django-summernote")



SETUP
-----

1. Install `django-summernote` to your python environment.

        pip install django-summernote

2. Add `django_summernote` to `INSTALLED_APP` in `settings.py`.

        INSTALLED_APPS += ('django_summernote', )

3. Add `django_summernote.urls` to `urls.py`.

        urlpatterns = patterns('',
            ...
            (r'^summernote/', include('django_summernote.urls')),
            ...
        )

4. Run `syncdb` for preparing attachment model.

        python manage.py syncdb 
        

USAGE
-----

In `admin.py`,

    from django_summernote.admin import SummernoteModelAdmin

    # Apply summernote to all TextField in model.
    class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        ...

Or, in `forms`,

    from django_summernote.widgets import SummernoteWidget

    # Apply summernote to specific fields.
    class SomeForm(forms.Form):
        foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

And don't forget to use it with `safe` filter in templates.


OPTIONS
-------

Support customization via settings.
Put `SUMMERNOTE_CONFIG` into your settings file.

In settings.py, 

    SUMMERNOTE_CONFIG = {
        # Change editor size
        'width': '100%',
        'height': '480',

        # Customize toolbar buttons
        'toolbar': [
            ['style', ['style']],
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol', 'height']],
            ['insert', ['link']],
        ],

        # Set `upload_to` function for attachments.
        'attachment_upload_to': my_custom_upload_to_func(),

        # Set custom storage class for attachments.
        'attachment_storage_class': 'my.custom.storage.class.name',
    }

About toolbar customization, please refer [Summernote document](http://hackerwins.github.io/summernote/features.html#customtoolbar).

Or, you can styling editor via attributes of the widget. These adhoc styling will override settings from `SUMMERNOTE_CONFIG`.

    # Apply adhoc style via attibutes
    class SomeForm(forms.Form):
        foo = forms.CharField(widget=SummernoteWidget(attrs={'width': '50%', 'height': '400px'}))

(TODO) Document for addtional settings will be added, soon. :^`D

AUTHOR
------

Park Hyunwoo([@lqez](https://twitter.com/lqez))


THANKS TO
---------

  - [jaeyoung](https://github.com/jeyraof) : Debugging on Django 1.4
  - [kroisse](https://github.com/kroisse) : Fixing problem on importing module

LICENSE
-------

`django-summernote` is distributed under MIT license.

And also uses below libraries.

  - jQuery File Upload : http://blueimp.github.io/jQuery-File-Upload/
