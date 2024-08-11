# test_script.py

from datetime import datetime

import pytest
import requests

from common import BASE_URL, logger, get_user_data


class TestUserAPI:

    def test_create_users_with_list(self, logger, get_user_data):
        # POST request to create users
        response = requests.post(f"{BASE_URL}/user/createWithList", json=get_user_data)

        # Log the status code
        logger.info(f"POST {BASE_URL}/user/createWithList - Status Code: {response.status_code}")

        # Check the status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    def test_get_user(self, logger, get_user_data):
        for user in get_user_data:
            # GET request to retrieve the user
            response = requests.get(f"{BASE_URL}/user/{user['username']}")

            # Log the status code and response
            logger.info(
                f"GET {BASE_URL}/user/{user['username']} - Status Code: {response.status_code}, Response: {response.json()}")

            # Check the status code
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

            # Parse the JSON response
            json_data = response.json()

            # Check the user details
            assert json_data["id"] == user["id"], logger.info(f"Expected id {user['id']}, but got {json_data['id']}")
            assert json_data["username"] == user["username"], logger.info(
                f"Expected username {user['username']}, but got {json_data['username']}")
            assert json_data["firstName"] == user["firstName"], logger.info(
                f"Expected firstName {user['firstName']}, but got {json_data['firstName']}")
            assert json_data["lastName"] == user["lastName"], logger.info(
                f"Expected lastName {user['lastName']}, but got {json_data['lastName']}")
            assert json_data["email"] == user["email"], logger.info(
                f"Expected email {user['email']}, but got {json_data['email']}")
            assert json_data["phone"] == user["phone"], logger.info(
                f"Expected phone {user['phone']}, but got {json_data['phone']}")
            assert json_data["userStatus"] == user["userStatus"], logger.info(
                f"Expected userStatus {user['userStatus']}, but got {json_data['userStatus']}")

    def test_user_login(self, logger, get_user_data):
        for user in get_user_data:
            # GET request to login the user
            response = requests.get(f"{BASE_URL}/user/login",
                                    params={"username": user["username"], "password": user["password"]})

            # Log the status code and response
            logger.info(f"GET {BASE_URL}/user/login - Status Code: {response.status_code}, Response: {response.text}")

            # Check the status code
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    def test_user_logout(self, logger):
        # GET request to logout the user
        response = requests.get(f"{BASE_URL}/user/logout")

        # Log the status code
        logger.info(f"GET {BASE_URL}/user/logout - Status Code: {response.status_code}")

        # Check the status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pytest.main([f"--html=report_{timestamp}.html", "-s", "-v", "--capture=tee-sys"])
