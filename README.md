# Test Automation Project

This project contains test automation scripts using Selenium WebDriver and Python. It is designed to test web applications across different browsers (Chrome and Firefox) and handle various functionalities such as theme switching and cookie notifications.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Chrome and/or Firefox browsers installed

### Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:gorniaq/website-ui-automation.git
   cd test-automation-project
   
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

3. Running Tests

   To run all tests:
      ```bash
      pytest
      ```
   To run tests and generate Allure reports:
      ```bash
      pytest --alluredir=allure-results
      allure serve allure-results
      ```

## Allure Test Report
![Allure Report](https://imgur.com/YybyaQS.png)

## Test Case Summary

This is a summary of the test cases that did not pass:

   **Case 4. Check the Policies List**

   Failed - The test expected 6 items, but 9 items are displayed on the site.
   
![Case 4 Allure Report](https://imgur.com/CGOaN89.png)
