from telegram.ext import BaseFilter


class GoogleIOFilter(BaseFilter):
    def filter(self, message):
        return 'google io' in message.text.lower()


class Done(BaseFilter):
    def filter(self, message):
        return 'Done!' in message.text


class Opcion1(BaseFilter):
    def filter(self, message):
        return 'Opción 1' in message.text


class Opcion2(BaseFilter):
    def filter(self, message):
        return 'Opción 2' in message.text


class Opcion3(BaseFilter):
    def filter(self, message):
        return 'Opción 3' in message.text


class Opcion4(BaseFilter):
    def filter(self, message):
        return 'Opción 4' in message.text
