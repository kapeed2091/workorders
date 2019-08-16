from sqreen_demo.dispatchers import IDispatcher


class SMSDispatcher(IDispatcher):
    def _notify(self):
        from sqreen_demo.utilities.send_sms import send_sms
        send_sms()
