from selene import browser, have, be


class AdminMessagesPage:
    def __init__(self):
        self.message_rows = browser.all(".messages").all(".row.detail.read-false")
        self.authors_of_message = self.message_rows.all("[data-testid^=message]").all(
            "p"
        )
        self.subject_of_message = self.message_rows.all(
            "[data-testid^=messageDescription]"
        ).all("p")
        self.opened_message_items = browser.element("[data-testid=message]").all(
            ".form-row"
        )

    def check_if_certain_message_exists(self, author, subject):
        self.authors_of_message.element_by(have.exact_text(author)).should(be.visible)
        self.subject_of_message.element_by(have.exact_text(subject)).should(be.visible)

    def open_message(self, subject):
        self.subject_of_message.element_by(have.exact_text(subject)).click()

    def check_content_of_message(self, author, email, phone, subject, message):
        self.opened_message_items.element_by(
            have.exact_texts(
                ("From: ", f"{author}"),
                ("Phone: ", f"{phone}"),
                ("Email: ", f"{email}"),
                (f"{subject}"),
                (f"{message}"),
            )
        )
