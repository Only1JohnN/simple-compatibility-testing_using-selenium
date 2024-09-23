# Automated Browser Compatibility Testing using Selenium and Pytest

This project is designed to perform cross-browser testing using Selenium WebDriver and Pytest. The tests involve automated Google searches with random search queries, and results are logged for further analysis. The browsers tested include **Google Chrome** and **Microsoft Edge**.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Customization](#customization)
- [Logging](#logging)
- [License](#license)

![Website Screenshot1](ref/Img_1.png)
![Website Screenshot2](ref/Img_2.png)
![Website Screenshot3](ref/Img_3.png)
![Website Screenshot4](ref/Img_4.png)
[![Watch the demo video](https://github.com/Only1JohnN/simple-login-automation_basic-approach/raw/main/ref/thumbnail.png)](https://youtu.be/7WdKkNK1MEo?si=yG3gtd6T_E5lSXWa)


## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Google Chrome and/or Microsoft Edge browser
- ChromeDriver and EdgeDriver for Selenium (corresponding to your browser versions)

You can download the appropriate drivers from:
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Only1JohnN/simple-compatibility-testing_using-selenium.git
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # For Linux/Mac
   # or
   myenv\Scripts\activate  # For Windows
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the WebDriver binaries:**
   - Place `chromedriver` and `msedgedriver` in your system's PATH or specify their location in your test script.

## Project Structure

```
/tests
  |-- test_compatibility_testing.py    # Main test script
.gitignore                             # Git ignore file
README.md                              # Project documentation
requirements.txt                       # List of Python dependencies
```

- `test_compatibility_testing.py`: The test script that runs the Google search tests on Chrome and Edge.
- `requirements.txt`: Contains the necessary Python packages, such as `selenium` and `pytest`.

## Running Tests

To run the tests, simply use Pytest:

```bash
pytest tests/test_compatibility_testing.py -v
```

This will run the search tests on both Chrome and Edge browsers, logging the search results for each run.

## Customization

### Adding or Modifying Search Queries

The search queries can be modified or extended in the script under the `SEACRH_QUERIES` list. For example:

```python
SEACRH_QUERIES = [
    "Selenium Automation",
    "Web testing best practices",
    "Cross-browser compatibility testing",
    "Adeniyi John",
    "Automated testing using cypress"
]
```

Feel free to add any search queries that are relevant to your project.

### Changing the Browsers Tested

You can add or remove browsers by modifying the `@pytest.fixture` in the script:

```python
@pytest.fixture(params=["Chrome", "Edge"])
def driver(request):
    ...
```

To include Firefox, for instance, you would add it to the `params` list and ensure `geckodriver` is installed:

```python
@pytest.fixture(params=["Chrome", "Edge", "Firefox"])
```

### Adjusting Delays

If you need more time for page loading or results fetching, you can adjust the `sleep()` duration in the test function:

```python
sleep(2)  # Increase to 3 or 5 seconds if necessary
```

## Logging

The script uses Python’s `logging` module to output information about the test's progress and the results returned by Google searches. The logs will be displayed on the console, providing insights into which queries were run and what results were obtained.

```python
logger.info(f"Searching for: {search_query}")
logger.info(f"Results from {driver.capabilities['browserName']} for '{search_query}':")
```

Logs can be customized further by modifying the logging configuration at the top of the script:

```python
logging.basicConfig(level=logging.INFO)
```