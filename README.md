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
   git clone https://github.com/gorniaq/test-automation-project
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
