# API Testing

This project contains automated tests for various APIs using Python, pytest, and the requests library.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or higher.
- You have installed the necessary Python libraries. You can install them using pip:

```bash
pip install pytest requests faker

Project Structure
The project contains the following files:

- common.py: This file contains the base URL of the APIs and the test data for a pet and a user.
- test_petstore.py: This file contains the test cases for the Petstore API.
- test_user.py: This file contains the test cases for the User API.
- test_script.py: This file contains additional test cases for the User API.
Running the Tests
To run the tests, follow these steps:

Clone the repository to your local machine.
Navigate to the directory containing the test scripts.
Run the tests using the following command:
 python3 -m pytest test_store.py --html=$(date +"%Y-%m-%d_%H-%M-%S")_report.html


Replace <test_file> with the name of the test file you want to run (test_petstore, test_user, or test_script). This will run all the tests in the specified file and generate an HTML report with the results. The report will be named report_<timestamp>.html, where <timestamp> is the current date and time.

Test Cases
Each test file contains several test cases for the corresponding API. Each test case logs its actions and assertions, so you can follow along in the console output or the HTML report.

Contact
If you want to contact me you can reach me at chiragkhanduja786@gmail.com.



