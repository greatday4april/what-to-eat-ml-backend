from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException


from api.serializers import SessionSerializer, PreferenceSerializer
from api.models import Session, Preference

from ipware import get_client_ip

import sys
import geocoder


class SessionViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = SessionSerializer

    def retrieve(self, request: Request):
        try:
            user_id = int(request.query_params.get('user_id'))
            session = Session.find_by_user(user_id)
            page_size = request.query_params.get('page_size')
            page_size = int(page_size) if page_size else None
            if session is None:
                ip_address, _is_routable = get_client_ip(request)
                location = geocoder.ip(ip_address)
                if not location.lat:
                    location = geocoder.ip('me')
                print('create a session for {}, ip: {}'.format(
                    location.city, ip_address))
                serializer = SessionSerializer(
                    data={
                        'user_id': user_id,
                        'page_size': page_size,
                        'location': location.latlng
                    }
                )
                if not serializer.is_valid():
                    raise APIException(str(serializer.errors),
                                       code=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
            else:
                if page_size not None:
                    session.page_size = page_size
                serializer = SessionSerializer(instance=session)
                session.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as error:
            print(error)
            raise APIException(error)
        finally:
            sys.stdout.flush()


class PreferenceViewSet(viewsets.ViewSet):
    serializer_class = PreferenceSerializer

    def list(self, request):
        try:
            user_id = int(request.query_params.get('user'))
            session = Session.find_by_user(user_id)
            arr_preferences = session.preferences.values()
            preference_set = PreferenceSerializer(
                [Preference for Preference in arr_preferences if Preference.type == "LIKE"], many=True).data
            return Response(preference_set, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            raise APIException(error)
        finally:
            sys.stdout.flush()

    def create(self, request):
        try:
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
            raise APIException(str(serializer.errors),
                               code=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(error)
            raise APIException(error)
        finally:
            sys.stdout.flush()
