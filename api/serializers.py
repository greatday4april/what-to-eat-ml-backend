from rest_framework import serializers
from api.models import Session, PreferenceType, Preference
from typing import Dict


class SessionSerializer(serializers.Serializer):
    next_restaurants = serializers.ListField(read_only=True)

    user_id = serializers.CharField(write_only=True, required=True)
    page_size = serializers.IntegerField(write_only=True, required=False)
    restaurant_id = serializers.CharField(write_only=True, required=False)
    preference_type = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data: Dict) -> Session:
        page_size = validated_data['page_size'] if 'page_size' in validated_data else None
        session = Session(user_id=validated_data['user_id'], page_size=page_size)
        session.save()
        return session

    def update(self, session: Session, validated_data: Dict) -> Session:
        session.add_preference(
            validated_data['restaurant_id'],
            PreferenceType(validated_data['preference_type']),
        )
        session.save()
        return session


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
