from selene import browser, have, be
from shady_meadows.models.utils import actions
from shady_meadows.data import client_and_booking as data


class BookingForm:
    def __init__(self):
        self.firstname = browser.element("[name=firstname]")
        self.lastname = browser.element("[name=lastname]")
        self.email = browser.element("[name=email]")
        self.phone = browser.element("[name=phone]")
        self.date = browser.all("div[role=cell]:not(.rbc-off-range)")
        self.weeks = browser.all(".rbc-row-content[role=row]")
        self.book_button = browser.all(".book-room").element_by(have.exact_text("Book"))
        self.confirmation_modal = browser.element(".confirmation-modal")
        self.dates_in_confirmation = self.confirmation_modal.element(
            "p:nth-child(even)"
        )
        self.close_button_on_confirmation_modal = self.confirmation_modal.element(
            "button"
        )

    def fill_firstname(self, firstname):
        self.firstname.type(firstname)
        return self

    def fill_lastname(self, lastname):
        self.lastname.type(lastname)
        return self

    def fill_email(self, email):
        self.email.type(email)
        return self

    def fill_phone(self, phone):
        self.phone.type(phone)
        return self

    def choose_dates(self, start_date, end_date):
        source_day = self.date.element_by(have.exact_text(start_date.strftime("%d")))
        target_day = self.date.element_by(have.exact_text(end_date.strftime("%d")))
        source_day.perform(actions.click_hold_and_move(target_day))
        return self

    def book(self):
        self.book_button.click()

    def check_if_confirmation_modal_is_visible(self):
        self.confirmation_modal.should(be.visible)

    def check_if_booking_dates_are_right(self, start_date, end_date):
        self.dates_in_confirmation.should(
            have.text(
                f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}"
            )
        )

    def close_confirmation_modal(self):
        self.close_button_on_confirmation_modal.click()

    def day_in_a_week(self, week_number, date):
        return (
            self.weeks[week_number]
            .all("div[role=cell]:not(.rbc-off-range)")
            .element_by(have.exact_text(date.strftime("%d")))
        )

    def unavailable_spot_in_a_week(self, week_number):
        return self.weeks[week_number].element(".rbc-event.rbc-event-allday")

    def unavailable_segment_with_relative_size(self, week_number, size):
        return (
            self.weeks[week_number]
            .element(f".rbc-row-segment[style*='{size}']")
            .element(".rbc-event.rbc-event-allday")
        )

    def is_booking_within_one_week(self, start_date, end_date):
        one_week = None
        start_week = None
        for week_number in range(len(self.weeks)):
            if self.day_in_a_week(week_number, start_date).wait_until(be.visible):
                if self.day_in_a_week(week_number, end_date).wait_until(be.visible):
                    one_week = True
                    start_week = week_number
                    break
                one_week = False
                start_week = week_number
                break
        return one_week, start_week

    def check_unavailable_status_in_calendar(self, start_date, end_date):
        one_week, start_week = self.is_booking_within_one_week(start_date, end_date)
        print(self.unavailable_spot_in_a_week(start_week).__call__().location["x"])
        print(self.day_in_a_week(start_week, start_date).__call__().location["x"] + 1)
        print(
            self.unavailable_segment_with_relative_size(
                start_week, "28.5714%"
            ).wait_until(be.visible)
        )
        if one_week:
            self.unavailable_segment_with_relative_size(start_week, "28.5714%").should(
                be.visible
            )
            assert (
                self.unavailable_spot_in_a_week(start_week).__call__().location["x"]
                == self.day_in_a_week(start_week, start_date).__call__().location["x"]
                + 1
            )
        else:
            self.unavailable_segment_with_relative_size(
                start_week + 1, "14.2857%"
            ).should(be.visible)
            self.unavailable_segment_with_relative_size(start_week, "14.2857%").should(
                be.visible
            )
            assert (
                self.unavailable_spot_in_a_week(start_week).__call__().location["x"]
                == self.day_in_a_week(start_week, start_date).__call__().location["x"]
                + 1
            )
