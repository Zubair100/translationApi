from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns


from api.views import translate

urlpatterns = [
       url(r'^test/?$', translate)
]
