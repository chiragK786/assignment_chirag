# common.py

import logging
from faker import Faker
import pytest

# Initialize a Faker object
fake = Faker()

# Configure logging
logging.basicConfig(level=logging.INFO)

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def logger(request):
    """
    Logger fixture to log API responses.
    """
    logger = logging.getLogger("pytest_logger")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("test_log.log", mode='w')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def fin():
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

    request.addfinalizer(fin)
    return logger


@pytest.fixture(scope="session")
def get_user_data():
    # Use Faker to generate fake data
    return [
        {
            "id": fake.random_int(min=0, max=9999),  # Generate a random integer between 0 and 9999
            "username": fake.user_name(),  # Generate a random username
            "firstName": fake.first_name(),  # Generate a random first name
            "lastName": fake.last_name(),  # Generate a random last name
            "email": fake.email(),  # Generate a random email
            "password": fake.password(),  # Generate a random password
            "phone": fake.phone_number(),  # Generate a random phone number
            "userStatus": fake.random_int(min=0, max=10)  # Generate a random user status
        }
        for _ in range(5)  # Create 5 users
    ]


@pytest.fixture(scope="session")
def order_data():
    # Use Faker to generate fake data
    return {
        "id": fake.random_int(min=0, max=9999),  # Generate a random integer between 0 and 9999
        "petId": fake.random_int(min=0, max=9999),  # Generate a random integer between 0 and 9999
        "quantity": fake.random_int(min=1, max=10),  # Generate a random integer between 1 and 10
        "shipDate": fake.date_time_this_year().isoformat(),  # Generate a random datetime this year
        "status": fake.random_element(elements=("placed", "approved", "delivered")),  # Randomly select a status
        "complete": fake.boolean()  # Generate a random boolean
    }


PET_DATA = {
    "id": fake.random_int(min=0, max=9999),
    "category": {
        "id": fake.random_int(min=0, max=9999),
        "name": fake.word()
    },
    "name": fake.name(),
    "photoUrls": [
        fake.image_url()
    ],
    "tags": [
        {
            "id": fake.random_int(min=0, max=9999),
            "name": fake.word()
        }
    ],
    "status": "available"
}
