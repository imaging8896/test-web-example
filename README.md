# test-web-example
It's a example automated test for a web. 

## Prerequisite
1. Python 3.9 or 3.10, use `tox` to run all Python versiosn, and you can skip some Python versions by removing the Python version in `tox.ini`. You can install Python versions from [here](https://www.python.org/downloads/)
1. Install dependencies：`pip install -r requirements_tox.txt`
1. Run tests command：`tox`

## Project structure
1. `Test Plan.xlsx`: Test plan and issues, 格式有誤可直接看 [Google Drive 內容](https://docs.google.com/spreadsheets/d/1n7X14ZKllbGAj6nsAIcyYBTeE297GziyxdhS1gv0F6k/edit?usp=sharing)
1. `tests/conftest.py`: Global tests setting. I use `pytest_runtest_makereport` to pass test info to take a screenshot when test failed. Screenshots will be in the `test_error_log`
1. `tests/driver`: Selenium setting and test config such as capability test config
1. `tests/user`: User behaviors to browse the webpage
1. `tests/barco_com`: Tests for barco.com
1. `tests/barco_com/data_warranty_info`: Test warranty info
1. `tests/barco_com/page`: Page object
1. `tests/barco_com/tests`: Tests script
1. `tests/barco_com/model`: Class use in tests or test data

## More
- [Partial screenshot](https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python) 
