from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import GroceryItemsList, ItemsList, ListsList
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/1.0/groceries/',
        GroceryItemsList.as_view(), name='grocery-list'),

    url(r'^api/1.0/itemslist/(?P<pk>\d+)/',
        ItemsList.as_view(), name='items-list-pk'),
    url(r'^api/1.0/itemslist/',
        ItemsList.as_view(), name='items-list'),

    url(r'^api/1.0/lists/(?P<pk>\d+)/',
        ListsList.as_view(), name='lists-list-pk'),
    url(r'^api/1.0/lists/',
        ListsList.as_view(), name='lists-list'),

    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^shoping/', include('shoping.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
