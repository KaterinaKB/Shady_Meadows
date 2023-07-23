from selene import browser

from shady_meadows.model.api.shadow_meadows_api import ShadowMeadowsAPI
from shady_meadows.model.components.booking_form import BookingForm
from shady_meadows.model.components.message_form import MessageForm
from shady_meadows.model.pages.admin_messages_page import AdminMessagesPage
from shady_meadows.model.pages.admin_page import AdminPage
from shady_meadows.model.pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.booking_form = BookingForm()
        self.message_form = MessageForm()
        self.admin_page = AdminPage()
        self.admin_message_page = AdminMessagesPage()
        self.api = ShadowMeadowsAPI()


app = Application()