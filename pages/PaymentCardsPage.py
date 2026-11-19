from playwright.sync_api import Locator

from pages.BasePage import BasePage
from utilities.config import DUMMY_PAY_URL


class PaymentCardsPage(BasePage):

    PATH = f"{DUMMY_PAY_URL}/cards"

    def __init__(self, page):
        super().__init__(page)

    @property
    def title(self) -> Locator:
        return self.page.get_by_role("heading", name="Payment Cards")

    @property
    def sub_title(self) -> Locator:
        return self.page.get_by_text("Manage your simulated payment")

    @property
    def alert(self) -> Locator:
        return self.page.get_by_role("alert")

    @property
    def list_of_payment_cards(self) -> Locator:
        return self.page.get_by_role("list")

    @property
    def empty_state(self) -> Locator:
        return self.page.get_by_text("No cards yetAdd a simulated")

    @property
    def add_card_button(self) -> Locator:
        return self.page.get_by_role("button", name="Add card")

    @property
    def add_card_dialog(self) -> Locator:
        return self.page.get_by_role("dialog", name="Add a simulated card")

    @property
    def card_alert_dialog(self) -> Locator:
        return self.page.get_by_role("alertdialog", name="Remove card ending in")
    
    @property
    def card_holder_name(self) -> Locator:
        return self.page.get_by_role("textbox", name="Cardholder name")

    @property
    def card_alert_dialog_remove_button(self) -> Locator:
        return self.page.get_by_role("button", name="Remove")
    
    @property
    def card_notification(self) -> Locator:
        return self.page.get_by_role("region", name="Notifications alt+T").get_by_role("listitem")

    @property
    def card_notification_added(self) -> Locator:
        return self.card_notification.get_by_text("Simulated card added.")

    @property
    def card_notification_removed(self) -> Locator:
        return self.card_notification.get_by_text("Card removed.")
    
    @property
    def remove_card_buttons(self) -> Locator:
        return self.page.get_by_role("button", name="Remove card ending in")
    
    def navigateToPage(self) -> None:
        self.page.goto(self.PATH)

    def open_add_card_dialog(self) -> None:
        self.add_card_button.click()
        self.add_card_dialog.wait_for(state="visible")

    def fill_dialog_name(self, card_holder_name) -> None:
        self.add_card_dialog.get_by_role("textbox", name="Cardholder name").fill(card_holder_name)

    def fill_dialog_card_number(self, card_number) -> None:
        self.add_card_dialog.get_by_role("textbox", name="Card number").fill(card_number)

    def fill_dialog_card_expiry(self, card_number) -> None:
        self.add_card_dialog.get_by_role("textbox", name="Expiry (MM/YY)").fill(card_number)

    def fill_dialog_card_cvv(self, card_cvv) -> None:
        self.add_card_dialog.get_by_role("textbox", name="CVV").fill(card_cvv)

    def addCardButtonClick(self) -> None:
        self.add_card_dialog.get_by_role("button", name="Add card").click()
        
    def get_number_of_cards(self) -> int:
        return self.remove_card_buttons.count()