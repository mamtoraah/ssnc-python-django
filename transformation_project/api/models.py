from django.db import models


class RequestLog(models.Model):
    """
    Model to log API requests and responses.
    Attributes:
        request_body (JSONField): The body of the request in JSON format.
        response_body (JSONField): The body of the response in JSON format.
        timestamp (DateTimeField): The timestamp when the log entry was created, automatically set to the current date and time.
    """
    request_body = models.JSONField()
    response_body = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
