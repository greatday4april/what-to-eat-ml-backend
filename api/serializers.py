from rest_framework import serializers
from api.models import Session, PreferenceType
from typing import Dict


class SessionSerializer(serializers.Serializer):
    next_restaurant = serializers.DictField(read_only=True)

    user_id = serializers.CharField(write_only=True, required=True)
    restaurant_id = serializers.CharField(write_only=True, required=False)
    preference_type = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data: Dict) -> Session:
        session = Session(user_id=validated_data['user_id'])
        session.save()
        return session

    def update(self, session: Session, validated_data: Dict) -> Session:
        session.add_preference(
            validated_data['restaurant_id'],
            PreferenceType(validated_data['preference_type']),
        )
        session.save()
        return session
