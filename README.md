# SauceDemo Selenium Automation Testing

## Project Description

This project is an automated testing framework built with **Selenium WebDriver**, **Python**, and **Pytest**.

The purpose of this project is to automate the testing of the SauceDemo web application. The test suite covers the complete user shopping journey, including login, product inventory, shopping cart, checkout process, order completion, and PDF report download functionality.

This project follows the **Page Object Model (POM)** design pattern to improve code readability, maintainability, and reusability.

---

## Technology Stack

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Report
- Page Object Model (POM)

---

## Project Structure

```text
selenium-python-automation/

├── page/
│   ├── login.py
│   ├── inventory.py
│   ├── shopping_cart.py
│   ├── checkout.py
│   └── checkout_complete.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_checkout2.py
│
├── screenshots/
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
└── README.md
```

---

## Features

- Page Object Model (POM) architecture
- Pytest-based test framework
- Browser automation using Selenium WebDriver
- Reusable page objects and fixtures
- Automated functional testing for SauceDemo
- HTML test report generation
- Automated browser interaction and element validation

---

## Test Coverage

The project contains automated test cases covering the following modules.

### Login Module

Test scenarios include:

- Successful login
- Login with Enter key
- Invalid username validation
- Invalid password validation
- Empty username validation
- Empty password validation
- Locked user validation
- Invalid credentials validation
- Username case sensitivity validation
- Password case sensitivity validation
- Username whitespace validation

---

### Inventory Module

Test scenarios include:

- Product list verification
- Product image loading verification
- Product price validation
- Add product to cart
- Add multiple products to cart
- Remove product from cart
- Remove multiple products from cart
- Add specific product
- Sort products by price (low to high)
- Sort products by price (high to low)
- Sort products by name (A-Z)
- Sort products by name (Z-A)

---

### Shopping Cart Module

Test scenarios include:

- Verify product displayed in cart
- Verify cart item count
- Verify product name consistency
- Verify added product appears in cart
- Verify multiple products appear in cart
- Remove product from cart
- Remove multiple products from cart
- Verify empty cart behaviour
- Continue shopping functionality
- Checkout navigation

---

### Checkout Module

Test scenarios include:

- Successful checkout submission
- Required field validation
- Empty first name validation
- Empty last name validation
- Empty postal code validation
- Cancel checkout functionality

---

### Checkout Complete Module

Test scenarios include:

- Order completion verification
- Generate PDF report download verification
- Back to products navigation

---

## Test Statistics

**Total Automated Test Cases: 44**

Test types include:

- Functional Testing
- Positive Testing
- Negative Testing
- Validation Testing
- UI Testing
- Download Testing

*Test results depend on the actual test execution.*

---

## Installation

Clone the repository:

```bash
git clone <repository-url>

cd selenium-python-automation
```

Install dependencies:

```bash
pip install selenium pytest pytest-html
```

Make sure Google Chrome is installed. Selenium Manager can automatically manage the appropriate browser driver in supported environments.

---

## Run Tests

Run all test cases:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Make sure the `reports` directory exists before generating the report.

---

## Test Report

After test execution, an HTML report will be generated.

The report includes:

- Test case results
- Pass/fail status
- Test execution duration
- Execution details

Example:

```text
44 passed
0 failed
```

The example above is illustrative. Actual results may differ depending on the test execution.

---

## Framework Design

This project uses the **Page Object Model (POM)** design pattern.

Structure:

- Page classes contain web element locators and page actions.
- Test files contain test scenarios and assertions.
- `conftest.py` manages reusable fixtures and test setup.
- Selenium WebDriver controls browser interactions.
- Pytest executes test cases and manages test results.

This structure improves maintainability and allows the framework to be extended with additional test scenarios.

---

## Learning Objectives

This project was created to practice and demonstrate:

- Selenium WebDriver fundamentals
- Web element locators
- Browser interaction and navigation
- Explicit waits and element handling
- Page Object Model design
- Pytest fixtures
- Test automation framework design
- Automated UI testing practices

---

## Notes

This repository demonstrates automated testing practices using Selenium WebDriver and Pytest.

The framework can be extended with additional test scenarios and improvements.

---

## Author

Name: CHAN KAH LOK
