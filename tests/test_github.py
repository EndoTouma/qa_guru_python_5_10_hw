import allure
from allure_commons.types import Severity
from selene import browser, be, by


def test_github():
	browser.open("https://github.com")
	
	browser.element(".header-search-input").click()
	browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
	browser.element(".header-search-input").submit()
	
	browser.element(by.link_text("eroshenkoam/allure-example")).click()
	
	browser.element("#issues-tab").click()
	
	browser.element(by.partial_text("#74")).should(be.visible)


def test_dinamic_github():
	with allure.step('Открываем главную страницу'):
		browser.open('https://github.com')
	
	with allure.step('Ищем репозиторий'):
		browser.element(".header-search-input").click()
		browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
		browser.element(".header-search-input").submit()
	
	with allure.step('Переходим по ссылке'):
		browser.element(by.link_text("eroshenkoam/allure-example")).click()
	
	with allure.step('Открываем таб Issues'):
		browser.element("#issues-tab").click()
	
	with allure.step('Проверяем наличие Issue с номером 74'):
		browser.element(by.partial_text("#74")).should(be.visible)


def test_decorator_steps():
	open_main_page()
	search_for_repository("eroshenkoam/allure-example")
	go_to_repository("eroshenkoam/allure-example")
	open_issue_tab()
	should_see_issue_with_number("#74")


@allure.step("Открываем главную страницу")
def open_main_page():
	browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
	browser.element(".header-search-input").click()
	browser.element(".header-search-input").send_keys(repo)
	browser.element(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
	browser.element(by.link_text(repo)).click()


@allure.step("Открываем Issues")
def open_issue_tab():
	browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
	browser.element(by.partial_text(number)).click()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "EndoTouma")
@allure.feature("Название Issue в репозитории")
@allure.story("Тест на проверку названия Issue в репозитории через Web-интерфейс")
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 74"):
        browser.element(by.partial_text("#74")).should(be.visible)
