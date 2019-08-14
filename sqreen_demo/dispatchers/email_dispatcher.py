from sqreen_demo.dispatchers import IDispatcher


class EmailDispatcher(IDispatcher):
    def _notify(self):
        import json
        from sqreen_demo.utilities.send_email import send_email
        send_email(json.dumps(self.data, indent=4))
