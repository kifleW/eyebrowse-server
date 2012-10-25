from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
    url(r'^profile/$', 'profile'),
    url(r'^profile/edit$', 'edit_profile'),

    url(r'^$', include('registration.urls')),
)