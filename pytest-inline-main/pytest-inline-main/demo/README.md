# pytest-inline demo

Run all demos
```
pytest
```

Run an example basic inline test (try: uncomment the failing inline test in example.py and see how the output changes):
```
pytest example.py
```

Explore features supported by pytest-inline in features.py
```
pytest -vv features.py
pytest -vv features.py --inlinetest-group=foo
pytest -vv features.py --inlinetest-order=bar  --inlinetest-order=foo
```

Run inline tests in parallel
```
pip install pytest-xdist
pytest parallel/          # sequential
pytest -n 4 parallel/  # parallel using 4 threads
```

# pytest-inline visualization

## allure

> https://allurereport.org/docs/pytest/

### install allure

1. Download the latest version as a zip archive from Github Releases.
2. Unpack the archive to the allure-commandline directory.
3. Navigate to the bin directory.
4. Use allure. bat for Windows or allure for Unix platforms.
5. Add allure to the system PATH.
6. install allure-pytest: `pip install allure-pytest`

### use allure

Execute all test files and generate reports

```shell
pytest -s -q --alluredir=./result/1
```

Execute the test file example.py and generate a report

```shell
pytest example.py --alluredir=./result/2  
```

View the report

```shell
# Method 1: Open the default browser to display the report
allure serve ./result/2    
```

```shell
# Method 2: Generate a report from the results
# Generate report
allure generate. /result/ -o./report/ --clean (overlay path plus --clean)
# Open a report
allure open -h 127.0.0.1 -p 8883./report/
```

### allure Features - feature, storry, step

Use case description information can be added to the report, such as test function, sub-function or scenario, test steps, and additional test information:

`@allure.feature(' feature name ')` : equivalent to testsuite

`@allure.story(' subfunction name ')` : corresponds to different scenarios under this function or module, equivalent to testcase

`@allure.step(' step ')` : Each step in the test process is placed in a concrete logical method

- `allure.step(' step ')` can only be placed as a decorator on a class or method
- `with allure.step`: Can be placed in the test case method

`@allure.attach(' specific text message ')`:Additional information: data, text, pictures, videos, web pages

### allure features - severity

It is marked by the importance level by allure.severity. There are five levels:

- Blocker level: Block

- Critical Level: Critical

- Normal Level: Normal

- Minor: Indicates that it is minor

- Trivial level: Not important

```
# usage
@allure.severity(allure.severity_level.CRITICAL)
@allure.severity('critical')
```

### allure features - attach

usage:

```
allure.attach(body, name, attachment_type, extension)
```

- body - The original content of the file to be written to

- name - The string containing the file name

- attachment_type - one of the allure.attachment_type values

- extension - The provided extension that will be used to create the file

### allure features - link, issue, testcase

usage:

```
@allure.link()
@allure.issue()
@allure.testcase()
```

### allure features - description

`@allure.description()` :decorator provides a description string

`@allure.description_html()` :provides some HTML in the test case description section

## pytest-html

> [pytest-html documentation](https://pytest-html.readthedocs.io/en/latest/user_guide.html)

install pytest-html

```
pip install pytest-html
```

Generate reports

```
pytest --html=report.html
```

pytest-inline personalization of reports according to official documentation

```python
#add conftest.py
from py.xml import html
import pytest
from time import strftime
from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    config.stash[metadata_key]["start time"] = strftime('%Y-%m-%d %H:%M:%S')

def pytest_html_report_title(report):
    report.title = "My very own title!"



@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["enviroment"] = "http://xxxxxx"
```

add report.css

```css

body {
    font-size: 16px;
}
h1 {
     text-align: center;
     color: #2084D9;
     font-size: 30px;
}
h2 {
    font-size: 24px;
    color: #2084D9;
}
a {
    color: #466AFF;
}
span {
    font-size: 20px;
}
#environment td {
    padding: 10px;
}
#results-table {
   font-size: 16px;
}
#results-table-head th{
    font-size: 20px;
    background-color: #2084D9;
    color: #FFFFFF;
}
td {
    color: #000000;
}
#environment tbody tr td:nth-child(1){
    background-color: #2084D9;
    color: #FFFFFF;
    font-weight:bold;
    font-size: 20px
}

```

Generate reports with css

```
pytest --html=report.html --css=report.css     
```

## reference

[Pytest测试框架（五）：pytest + allure生成测试报告 - 测试开发小记 - 博客园 (cnblogs.com)](https://www.cnblogs.com/hiyong/p/14163298.html#allure特性feature-storry-step)

https://blog.csdn.net/IT_LanTian/article/details/124018836

[pytest--html报告优化（增加错误截图，获取统计数据） - 简书 (jianshu.com)](https://www.jianshu.com/p/99f4b1da5103)

