from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException


from api.serializers import SessionSerializer, PreferenceSerializer
from api.models import Session, Preference, User


class SessionViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = SessionSerializer

    def retrieve(self, request: Request):
        try:
            user_id = int(request.query_params.get('user_id'))
            session = Session.find_by_user(user_id)
            if session is None:
                serializer = SessionSerializer(
                    data={'user_id': user_id, 'page_size': request.query_params.get('page_size')})
                if not serializer.is_valid():
                    raise APIException(str(serializer.errors))
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
            serializer = SessionSerializer(instance=session)
        except Exception as error:
            raise APIException(error)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        try:
            user_id = int(request.query_params.get('user_id'))
            session = Session.find_by_user(user_id)
            serializer = SessionSerializer(
                data=request.data,
                instance=session,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            raise APIException(error)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreferenceViewSet(viewsets.ViewSet):
    serializer_class = PreferenceSerializer

    def list(self, request):
        user_id = int(request.query_params.get('user'))
        session = Session.find_by_user(user_id)
        arr_preferences = session.preferences.values()
        preference_set = PreferenceSerializer([Preference for Preference in arr_preferences if Preference.type == "LIKE"], many=True).data
        return Response(preference_set, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PreferenceSerializer(
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            preference: Preference = serializer.save()
            user_id = int(request.data.get('user'))
            session = Session.find_by_user(user_id)
            session.preferences[preference.restaurant_id] = preference
            session.save()
            return Response({'success': True}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
