# Demo project for automation testing of Shadow Meadows
<p align="center">
<img title="Shadow_Meadows_pic" src="images/Shadow_meadows.png">
</p>

##  Contents:

> ➠ [Technology stack](#Technology_stack)
>
> ➠ [Covered functionality](#covered_functionality)
>
> ➠ [Running tests from the terminal](#Running_tests)
>
> ➠ [Allure report](#allure_report)
>
> ➠ [Telegram Notification](#telegram_notification)
>
> ➠ [Selenoid Test Run example](#selenoid_run)
  
## Technology stack <a name="technology_stack"></a> 

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="images/PyCharm_Icon.png" height="50"  alt="PyCharm"/></a>
<a href="https://www.python.org/"><img src="images/python.png"  height="50"  alt="Python"/></a>
<a href="https://aerokube.com/selenoid/"><img src="images/selenoid.svg"  height="50"  alt="Selenoid"/></a>
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

## Covered functionality <a name="сovered_functionality"></a> 

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

## <img src="images/Jenkins.png" height="30"  alt="Jenkins"/></a> Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/005-KaterinaKB-DiplomaProject/"> job </a> <a name="jenkins_job"></a> 
<p align="center">
<a href="https://jenkins.autotests.cloud/job/005-KaterinaKB-DiplomaProject/"><img src="images/JenkinsJob.png" alt="Jenkins"/></a>
</p>

##  Running tests from the terminal <a name="running_tests"></a> 
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
## <a name="allure_report"></a>  <img src="images/allure.png" height="30"  alt="Allure"/></a> <a target="_blank" href="https://jenkins.autotests.cloud/job/005-KaterinaKB-DiplomaProject/11/allure/">Allure report</a>

###  Overview
<p align="center">
<img title="Allure Overview Dashboard" src="images/AllureReportOverview.png">
</p>


### Tests
<p align="center">
<img title="Allure Tests" src="images/AllureReportTests.png">
</p>


## <a name="telegram_notofocation"></a>  <img src="images/telegram.png" height="30"  alt="Allure"/></a> Telegram Notification


<p align="center">
<img title="Allure Overview Dashboard" src="images/ReportFromBot.png" >
</p>

## <a name="selenoid_run"></a> Selenoid Test Run example
### <img src="images/selenoid.svg" height="25" alt="Jenkins"/></a> Video with test run</a>
<p align="center">
<img title="selenoid test run" src="images/VideoWithTestRun.gif">
</p>