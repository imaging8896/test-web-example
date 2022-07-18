# test-web-example
It's a example automated test for a web. 

## Prerequisite
1. Python 3.10：`which python` is `Python 3.10`
1. Create virtualenv：`python -m venv .venv`
1. Use the virtual env：`source .venv/bin/activate`
1. Install dependencies：`pip install -r requirements.txt`
1. Run tests：`pytest tests`

## Project structure
1. `tests/conftest.py`: Global tests setting. I use `pytest_runtest_makereport` to pass test info to take a screenshot when test failed. Screenshots will be in the `test_error_log`
1. `tests/driver`: Selenium setting and test config such as capability test config
1. `tests/user`: User behaviors to browser