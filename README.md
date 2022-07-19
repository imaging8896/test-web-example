# test-web-example
It's a example automated test for a web. 

## Prerequisite
1. Python 3.9 or 3.10, use `tox` to run all Python versiosn, and you can skip some Python versions by removing the Python version in `tox.ini`. You can install Python versions from [here](https://www.python.org/downloads/)
1. Install dependencies：`pip install -r requirements_tox.txt`
1. Run tests：`tox`

## Project structure
1. `tests/conftest.py`: Global tests setting. I use `pytest_runtest_makereport` to pass test info to take a screenshot when test failed. Screenshots will be in the `test_error_log`
1. `tests/driver`: Selenium setting and test config such as capability test config
1. `tests/user`: User behaviors to browser

## More
- [Partial screenshot](https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python) 
