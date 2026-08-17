import httpx

class APIClient:
    def __init__(self, base_url):
        self.client = httpx.Client(base_url=base_url)