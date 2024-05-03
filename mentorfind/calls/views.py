from rest_framework import viewsets
from rest_framework.response import Response
from .models import WebRTCSession
from .serializers import WebRTCSessionSerializer
from aiortc import RTCPeerConnection, RTCSessionDescription

# class WebRTCSessionViewSet(viewsets.ViewSet):
#     queryset = WebRTCSession.objects.all()
#     serializer_class = WebRTCSessionSerializer
#
#     async def create(self, request):
#         session_id = request.data.get('session_id')
#         # Тут ви можете використовувати session_id для створення нової сесії в базі даних
#
#         # Створення об'єкта PeerConnection
#         pc = RTCPeerConnection()
#
#         async def on_track(track):
#             kind = track.kind
#             params = track.get_parameters()
#
#         @pc.on('track')
#         async def on_track_cb(track):
#             await on_track(track)
#
#         offer = await pc.createOffer()
#         await pc.setLocalDescription(offer)
#
#         return Response({'sdp': pc.localDescription.sdp})
#
#     async def join(self, request, pk=None):
#         session_id = request.data.get('session_id')
#         # Отримання сесії за session_id з бази даних
#         session = WebRTCSession.objects.get(session_id=session_id)
#
#         # Створення об'єкта PeerConnection
#         pc = RTCPeerConnection()
#
#         async def on_track(track):
#             kind = track.kind
#             params = track.get_parameters()
#
#         @pc.on('track')
#         async def on_track_cb(track):
#             await on_track(track)
#
#         # Створення SDP answer
#         answer = RTCSessionDescription(sdp=request.data.get('sdp'), type='offer')
#         await pc.setRemoteDescription(answer)
#
#         # Створення SDP answer
#         answer = await pc.createAnswer()
#         await pc.setLocalDescription(answer)
#
#         return Response({'message': 'Joined session successfully'})
#
#     def list(self, request):
#         sessions = WebRTCSession.objects.all()
#         serializer = WebRTCSessionSerializer(sessions, many=True)
#         return Response(serializer.data)
#
