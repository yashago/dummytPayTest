import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_payment_card_page_structure(payment_cards):
    payment_cards_page = payment_cards
    expect(payment_cards_page.title).to_be_visible()
    expect(payment_cards_page.sub_title).to_be_visible()
    expect(payment_cards_page.alert).to_be_visible()
    expect(payment_cards_page.add_card_button).to_be_visible()
    expect(payment_cards_page.empty_state).to_be_visible()

def test_add_and_remove_card(payment_cards):
    payment_cards_page = payment_cards
    payment_cards_page.open_add_card_dialog()
    expect(payment_cards_page.add_card_dialog).to_be_visible()
    payment_cards_page.fill_dialog_name("Jacob Gontmacher")
    payment_cards_page.fill_dialog_card_number("4111 1111 1111 1111")
    payment_cards_page.fill_dialog_card_expiry("03/30")
    payment_cards_page.fill_dialog_card_cvv("737")
    payment_cards_page.addCardButtonClick()
    expect(payment_cards_page.card_notification_added).not_to_be_visible(timeout=10000)
    expect(payment_cards_page.empty_state).not_to_be_visible()
    payment_cards_page.remove_card_buttons.last.scroll_into_view_if_needed()
    payment_cards_page.remove_card_buttons.last.click()
    expect(payment_cards_page.card_alert_dialog).to_be_visible()
    payment_cards_page.card_alert_dialog_remove_button.click()
    expect(payment_cards_page.card_notification_removed).not_to_be_visible(timeout=10000)
    expect(payment_cards_page.empty_state).to_be_visible()