from django.urls import include, path, re_path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^api/v1/WTBs/(?P<pk>........-....-....-....-............+)$',
        views.get_delete_update_WTB.as_view(),
        name='get_delete_update_WTB'
    ),
    path('api/v1/WTBs/', # urls list all and create new one
        views.post_WTB.as_view(),
        name='post_WTB'),
]