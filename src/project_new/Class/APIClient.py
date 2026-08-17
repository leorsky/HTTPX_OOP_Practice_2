import httpx

class APIClient:
    def __init__(self, base_url):
        self.client = httpx.Client(base_url=base_url)

    def get(self, endpoint='', params=None):
        response = self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint='', data=None):
        response = self.client.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint='', data=None):
        response = self.client.put(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint='', data=None):
        response = self.client.patch(endpoint, json=data)
        response.raise_for_status()
        return response.json()