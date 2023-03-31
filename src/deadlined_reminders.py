from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(cls):
        pass

class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = parse(text)

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        iter([text, formatted_date])