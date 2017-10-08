from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns


from api.views import translate, test

urlpatterns = [
       url(r'^translate/?$', translate),
       url(r'^test/?$', test)
]
