from django.urls import path

from commentApp.views import CommentCreateView

app_name = 'commentApp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    # path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]