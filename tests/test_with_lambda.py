import allure
from selene import browser, by, be


def test_lambda_steps():
    with allure.step('Open github'):
        browser.open('/')

    with allure.step('Search'):
        browser.element(".search-input").click()
        browser.element("#query-builder-test").send_keys("qaguru-learn/dz_10").press_enter()
        browser.element(by.link_text("qaguru-learn/dz_10")).click()

    with allure.step('Open issues'):
        browser.element('#issues-tab').click()

    with allure.step('Check issue with number #1'):
        browser.element(by.partial_text("#1")).should(be.visible)
