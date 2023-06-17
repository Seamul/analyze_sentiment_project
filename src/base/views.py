
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .sentiment_analysis import perform_sentiment_analysis


class SentimentAnalysisView(APIView):
    """
    API endpoint for performing sentiment analysis on text.
    """

    def get(self, request, format=None):
        """
        Handles GET requests to the sentiment analysis API endpoint.

        Returns:
            Response: JSON response containing a welcome message and an example usage of the API.

        """
        response = {
            "message": "Welcome to the Sentiment Analysis tool! Please feel free to submit your text for analysis using the example provided below.",
            "example": {
                "text": "I went for a walk in the park today."
            }
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Handles POST requests to the sentiment analysis API endpoint.

        Args:
            request (HttpRequest): The POST request object containing the text to be analyzed.

        Returns:
            Response: JSON response containing the sentiment analysis result.

        Raises:
            None

        Example:
            POST /sentiment-analysis/
            Request Body:
            {
                "text": "I love this product! It exceeded my expectations."
            }

            Response:
            {
                "sentiment": "Positive"
            }
        """
        try:
            text = request.data.get('text', '')
            if not text:
                response = {
                    'error': 'Text parameter is missing or empty.'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            sentiment = perform_sentiment_analysis(text)
            response = {
                'sentiment': sentiment
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'error': 'An error occurred while processing the request.'
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
