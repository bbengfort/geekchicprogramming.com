from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from followers.views import AddFollower
from feedback.views import ContactFormView
from simplepage.views import SimplePageView
from auth.views import TeacherProfileView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^404/$', TemplateView.as_view(template_name="404.html"), name="404"),
    url(r'^500/$', TemplateView.as_view(template_name="500.html"), name="500"),
    url(r'^legal/$', TemplateView.as_view(template_name="legal.html"), name="legal"),
    url(r'^privacy/$', TemplateView.as_view(template_name="privacy.html"), name="privacy"),
    url(r'^contact-us/$', ContactFormView.as_view(), name="contact"),
    url(r'^signup/$', AddFollower.as_view(), name="email_signup"),
    url(r'^t/(?P<username>\w+)/', TeacherProfileView.as_view(), name="teacher_profile"),
    url(r'^programs/', include('events.urls')),
    url(r'^apply/', include('apply.urls')),
    url(r'^workshops/', include('workshop.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('auth.urls')),
    url(r'^blog/', include('zinnia.urls'), name="blog"),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # This must be on the last line
    url(r'^((?P<section>\w+)/)?(?P<name>\w+)/$', SimplePageView.as_view(), name="simplepage_page"),
)


# REMOVE THIS! DEBUG ONLY
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', kwargs={'document_root': '/Users/benjamin/repos/git/geekchicprogramming.com/media_tmp/'}), )
