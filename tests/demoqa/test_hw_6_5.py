import os.path

import allure
from selene import browser
from selene.support.conditions import have, be

@allure.title('Choose form')
def test_student_registration_form():
    with allure.step('Открытие браузера'):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step('Заполнение формы'):
        browser.element('#firstName').should(be.blank).type('Vladimir')
        browser.element('#lastName').should(be.blank).type('Ushakov')
        browser.element('#userEmail').type('test@mail.ru')
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        browser.element('#userNumber').type('89937777777')

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys('July')
        browser.element('.react-datepicker__year-select').send_keys('1998')
        browser.element(f'.react-datepicker__day--0{27}').click()

        browser.element('#subjectsInput').with_(timeout=4).send_keys('Computer Science').press_tab()
        browser.all('#hobbiesWrapper .custom-control-label').element_by(have.exact_text('Music')).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/photo.jpg'))
        browser.element('#currentAddress').type('street test 12')
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

        browser.element('#submit').click()

    with allure.step('Проверка формы'):
        browser.all('.table-responsive .table td:nth-child(2)').should(have.exact_texts(
            'Vladimir Ushakov',
            'test@mail.ru',
            'Male',
            '8993777777',
            '27 July,1998',
            'Computer Science',
            'Music',
            'photo.jpg',
            'street test 12',
            'Haryana Karnal'

        ))
