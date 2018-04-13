from telegram.ext import BaseFilter


class GoogleIOFilter(BaseFilter):
    def filter(self, message):
        return 'google io' in message.text.lower()
