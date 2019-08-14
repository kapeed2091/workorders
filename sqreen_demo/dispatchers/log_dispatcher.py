from sqreen_demo.dispatchers import IDispatcher


class LogDispatcher(IDispatcher):
    def _notify(self):
        import logging
        from sqreen_demo.config import SUBJECT
        logging.debug('{}: {}'.format(SUBJECT, str(self.data)))
