"""Custom exceptions for the datawrapper package."""


class FailedRequest(Exception):
    """Custom exception for failed API requests."""

    def __init__(self, response):
        msg = f"Request failed with status code {response.status_code}. Response content: {response.content}"
        super().__init__(msg)