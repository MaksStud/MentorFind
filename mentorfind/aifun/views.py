from rest_framework import viewsets
from rest_framework.response import Response
from g4f.client import Client
import g4f
from googletrans import Translator


class TextGenerationViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        content = request.query_params.get('c', '')
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": 'user', "content": content}],  # Використовувати переданий рядок у запиті
        )
        task_content = response.choices[0].message.content
        return Response({"content": task_content})


class ImageGenerationViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        def translate_to_english(text):
            translator = Translator()
            translated_text = translator.translate(text, dest='en').text
            return translated_text
        try:
            prompt = request.query_params.get('p', '')
            client = Client()
            response = client.images.generate(
                model="gemini",
                prompt=str(translate_to_english(prompt)),
            )
            image_url = response.data
            image_urls_list = [image.url for image in image_url]
        except g4f.errors.NoImageResponseError:
            return Response({'error': 'No data'}, status=400)
        else:
            return Response(image_urls_list)