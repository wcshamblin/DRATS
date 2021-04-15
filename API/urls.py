from django.urls import include, path, re_path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^api/v1/tickets/(?P<pk>........-....-....-....-............+)$',
        views.get_delete_update_ticket.as_view(),
        name='get_delete_update_ticket'
    ),
    path('api/v1/tickets/', # urls list all and create new one
        views.post_ticket.as_view(),
        name='post_ticket'),
]