from selene import browser, by, be


def test_issue_on_github():
    browser.open('/')

    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys("qaguru-learn/dz_10").press_enter()
    browser.element(by.link_text("qaguru-learn/dz_10")).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text("#1")).should(be.visible)
