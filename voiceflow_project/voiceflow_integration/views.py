from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConversationSerializer
import requests
from django.conf import settings

class StartConversationView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id", "")
        url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact"
        response = requests.post(url, headers={"Authorization": settings.VOICEFLOW_API_KEY})
        response['Access-Control-Allow-Origin'] = '*'

        # Save the conversation history (optional)
        serializer = ConversationSerializer(data={"user_id": user_id, "output_text": response.text})
        if serializer.is_valid():
            serializer.save()

        return Response(response.json(), status=status.HTTP_200_OK)

class SendUserInputView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id", "")
        user_input = request.data.get("user_input", "")

        url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact"
        body = {"action": {"type": "text", "payload": user_input}}
        response = requests.post(url, json=body, headers={"Authorization": settings.VOICEFLOW_API_KEY})
        response['Access-Control-Allow-Origin'] = '*'

        # Save the conversation history (optional)
        serializer = ConversationSerializer(data={"user_id": user_id, "input_text": user_input, "output_text": response.text})
        if serializer.is_valid():
            serializer.save()

        return Response(response.json(), status=status.HTTP_200_OK)
