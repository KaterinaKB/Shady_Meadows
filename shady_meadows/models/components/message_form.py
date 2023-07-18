from selene import browser, have, be


class MessageForm:
    def __init__(self):
        self.name = browser.element("#name")
        self.email = browser.element("#email")
        self.phone = browser.element("#phone")
        self.subject = browser.element("#subject")
        self.message = browser.element("#description")
        self.submit_button = browser.element("#submitContact")
        self.thanks_for_message = browser.element('.col-sm-5').element('h2')
        self.subject_in_reply = browser.element('.col-sm-5').element('''//p[text()="We'll get back to you about"]/following::p[1]''')

    def fill_name(self, name):
        self.name.type(name)
        return self

    def fill_email(self,email):
        self.email.type(email)
        return self

    def fill_phone(self, phone):
        self.phone.type(phone)
        return self

    def fill_subject(self, subject):
        self.subject.type(subject)
        return self

    def fill_message(self,message):
        self.message.type(message)
        return self

    def submit(self):
        self.submit_button.click()

    def check_reply_to_message(self, name, subject):
        self.thanks_for_message.should(have.exact_text(f'Thanks for getting in touch {name}!'))
        self.subject_in_reply.should(have.exact_text(f'{subject}'))
