# Demo project for automation testing of Shadow Meadows
<p align="center">
<img title="Shadow_Meadows_pic" src="images/Shadow_meadows.png">
</p>

##  Contents:

> ➠ [Технологический стек](#classical_building-технологический-стек)
>
> ➠ [Покрытый функционал](#earth_africa-покрытый-функционал)
>
> ➠ [Сборка в Jenkins](#earth_africa-Jenkins-job)
>
> ➠ [Запуск из терминала](#earth_africa-Запуск-тестов-из-терминала)
>
> ➠ [Примеры использования](#earth_africa-Allure-отчет)
>
> ➠ [Allure отчет](#earth_africa-Allure-отчет)
> 
> ➠ [Интеграция с Jira](#earth_africa-Allure-отчет)
>
> ➠ [Отчет в Telegram](#earth_africa-Уведомление-в-Telegram-при-помощи-бота)
>
> ➠ [Видео примеры прохождения тестов](#earth_africa-Примеры-видео-о-прохождении-тестов)

  
## Technology stack

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="images/PyCharm_Icon.png" height="50"  alt="PyCharm"/></a>
<a href="https://www.python.org/"><img src="images/python.png"  height="50"  alt="Python"/></a>
<a href="https://github.com/"><img src="images/GitHub.png"  height="50"  alt="Github"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="images/allure.png" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="images/Jenkins.png" height="50"  alt="Jenkins"/></a> 
</p>

- Autotests were written in <code>Python</code> using <code>Selene</code> for UI tests.
- PageObject is used
- API methods are used in UI tests to speed up the tests
- <code>Allure Report</code> generates test run reports
- <code>Jenkins</code> runs the tests. 
- After the run is completed, notifications are sent using the bot to <code>Telegram</code>.

## Covered functionality

### UI
You can see Shadow Meadows web-site <a href="https://automationintesting.online/#">here</a>

Be aware that database resets every 10 minutes

- [x] Testing of booking creation
- [x] Testing of information in booking confirmation
- [x] Testing of total cost of booking
- [x] Testing of message sending

### API
You can see Shadow Meadows API <a href="https://automationintesting.online/auth/swagger-ui/index.html#/">for authentication</a> and <a href="https://automationintesting.online/booking/swagger-ui/index.html#/">for booking</a>

Be aware that database resets every 10 minutes

- [x] Testing of GET method for receiving information about booking
- [x] Testing of POST method for booking creation (including checking the content in response and schema validation)
- [x] Testing of DELETE method for booking removal

## <img src="images/Jenkins.png" height="30"  alt="Jenkins"/></a> Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/005-KaterinaKB-DiplomaProject/"> job </a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/005-KaterinaKB-DiplomaProject/"><img src="images/JenkinsJob.png" alt="Jenkins"/></a>
</p>

##  Running tests from the terminal
Local launch:
```
pytest ./tests
```

Only UI tests:
```
pytest ./tests/tests_ui
```

Only API tests:
```
pytest ./tests/tests_api
```

Report generation:
```
allure serve ./allure-results
```
## <img src="images/allure.png" height="30"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://jenkins.autotests.cloud/job/005-KaterinaKB-DiplomaProject/11/allure/">Allure report</a>

###  Overview
<p align="center">
<img title="Allure Overview Dashboard" src="images/AllureReportOverview.png">
</p>


### Tests
<p align="center">
<img title="Allure Tests" src="images/AllureReportTests.png">
</p>


## <img src="images/telegram.png" height="30"  alt="Allure"/></a> Telegram Notification


<p align="center">
<img title="Allure Overview Dashboard" src="images/ReportFromBot.png" >
</p>

## Selenoid Test Run example
### <img src="images/selenoid.svg" height="25" alt="Jenkins"/></a> Видео <a target="_blank" href="https://selenoid.autotests.cloud/video/ef6f0961cd61bebe69b39d6591b8a072.mp4">прохождения тестов </a>
<p align="center">
<img title="selenoid test run" src="images/VideoWithTestRun.gif">
</p>