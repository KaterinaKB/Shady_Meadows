from selenium.webdriver import ActionChains
from selene.core.wait import Command
from selene.core.entity import Element


def click_hold_and_move(target_element: Element):
    def func(element: Element):
        located_sourse_element = element.locate()
        located_target_element = target_element.locate()
        driver = element.config.driver
        actions: ActionChains = ActionChains(driver)

        actions.click_and_hold(located_sourse_element).move_by_offset(10,10).move_to_element(located_target_element).release().perform()

    command = Command(f'click, hold and move to element ={target_element}', func)

    return command
