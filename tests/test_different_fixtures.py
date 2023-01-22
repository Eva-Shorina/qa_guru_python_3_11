"""Вариант с двумя разными фикстурами"""
from selene import be
from selene.support.shared import browser

def test_login_desktop(browser_desktop):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)

def test_login_mobile(browser_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)

"""
Преимущества подхода: простой синтаксис, легко запомнить и пользоваться, легко читается
Недостатки: для каждого нового условия нужна отдельная фикстура, будет повторяющийся код, не компактно
"""