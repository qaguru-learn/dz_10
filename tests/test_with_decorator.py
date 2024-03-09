import allure
from selene import browser, by, be


def test_decorator_steps():
    open_main_page()
    search("qaguru-learn/dz_10")
    open_issues()
    check_issue_visible(1)


@allure.step('Open main page')
def open_main_page():
    browser.open('/')


@allure.step('Search repository {repo}')
def search(repo):
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys(repo).press_enter()
    browser.element(by.link_text("qaguru-learn/dz_10")).click()


@allure.step('Open issues')
def open_issues():
    browser.element('#issues-tab').click()


@allure.step('Check issue with number #{number}')
def check_issue_visible(number):
    browser.element(by.partial_text(f"#{number}")).should(be.visible)
