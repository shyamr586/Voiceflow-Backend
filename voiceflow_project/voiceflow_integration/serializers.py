from rest_framework import serializers

class ConversationSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    input_text = serializers.CharField(required=False)
    output_text = serializers.CharField()
