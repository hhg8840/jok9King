from django.conf.urls import url
from policy.views import privacy

app_name = "policy"

urlpatterns = [
    url('privacy/', privacy),
]