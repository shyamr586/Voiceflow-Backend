from django.urls import path
from .views import StartConversationView, SendUserInputView

urlpatterns = [
    path('api/start_conversation/', StartConversationView.as_view(), name='start_conversation'),
    path('api/send_user_input/', SendUserInputView.as_view(), name='send_user_input'),
    # Add other URL patterns as needed
]
