
from sqreen_demo.dispatchers import IDispatcher


class HTTPDispatcher(IDispatcher):
    def _notify(self):
        import json
        import requests
        from sqreen_demo.config import HTTP_DISPATCHER_URL

        request_data = {'data': json.dumps(self.data)}
        requests.post(HTTP_DISPATCHER_URL, json=request_data,
                      headers={'Content-Type': 'application/json'})
