import abc


class IDispatcher:
    __metaclass__ = abc.ABCMeta

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def _notify(self):
        pass

    def notify(self):
        self._notify()


def notify():
    pass
