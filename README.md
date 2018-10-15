# WM_assignment

## Prerequisites

Install Selenium with the Python 3 binding along with the latest version of chromedriver.
Instructions can be found here: https://selenium-python.readthedocs.io/installation.html

## Running the scripts

The WorkMarket.py and login_workmarket.py scripts can be executed via terminal like so,
```
python WorkMarket.py
python login_workmarket.py
```

The WorkMarket script ensures the login is successful and verifies each search result contains the string 'test'.

The login_workmarket scripts validates the following login page responses:

  - Invalid user name or password.
  - If we have your email address on file, we've sent you password reset instructions. (reset password)
  - reCAPTCHA response is required
