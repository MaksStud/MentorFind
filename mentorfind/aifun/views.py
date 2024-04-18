from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TaskRequestSerializer
from g4f.client import Client


class TaskResponseViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        content = request.query_params.get('content', '')  # Отримати рядок з параметрів запиту
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": 'user', "content": content}],  # Використовувати переданий рядок у запиті
        )
        task_content = response.choices[0].message.content

        serializer = TaskRequestSerializer({"content": task_content})
        return Response(serializer.data)

