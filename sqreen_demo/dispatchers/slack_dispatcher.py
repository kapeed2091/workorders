from sqreen_demo.dispatchers import IDispatcher


class SlackDispatcher(IDispatcher):
    def _notify(self):
        import json
        import requests
        from sqreen_demo.config import SLACK_WEBHOOK

        requests.post(
            url=SLACK_WEBHOOK, json={'text': json.dumps(self.data)},
            headers={'Content-Type': 'application/json'})
