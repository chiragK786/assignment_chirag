# test_petstore.py

import requests
import pytest
from datetime import datetime
from common import logger, order_data, BASE_URL


class TestPetstoreAPI:

    def test_get_inventory(self, logger):
        # GET request to retrieve the inventory
        response = requests.get(f"{BASE_URL}/store/inventory")

        # Log the status code and response
        logger.info(
            f"GET {BASE_URL}/store/inventory - Status Code: {response.status_code}, Response: {response.json()}")

        # Check the status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_data = response.json()

        # Check that the response is a dictionary
        assert isinstance(json_data, dict), "Expected a dictionary in the response"

    def test_create_order(self, logger, order_data):
        # POST request to create an order
        response = requests.post(f"{BASE_URL}/store/order", json=order_data)

        # Log the status code and response
        logger.info(f"POST {BASE_URL}/store/order - Status Code: {response.status_code}, Response: {response.json()}")

        # Check the status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    def test_get_order(self, logger, order_data):
        # GET request to retrieve the order
        response = requests.get(f"{BASE_URL}/store/order/{order_data['id']}")

        # Log the status code and response
        logger.info(
            f"GET {BASE_URL}/store/order/{order_data['id']} - Status Code: {response.status_code}, Response: {response.json()}")

        # Check the status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        json_data = response.json()

        # Check the order details
        assert json_data["id"] == order_data["id"], logger.info(
            f"Expected id {order_data['id']}, but got {json_data['id']}")
        assert json_data["petId"] == order_data["petId"], logger.info(
            f"Expected petId {order_data['petId']}, but got {json_data['petId']}")
        assert json_data["quantity"] == order_data["quantity"], logger.info(
            f"Expected quantity {order_data['quantity']}, but got {json_data['quantity']}")
        assert json_data["status"] == order_data["status"], logger.info(
            f"Expected status {order_data['status']}, but got {json_data['status']}")
        assert json_data["complete"] == order_data["complete"], logger.info(
            f"Expected complete {order_data['complete']}, but got {json_data['complete']}")

    def test_delete_order(self, logger, order_data):
        # DELETE request to delete the order
        response = requests.delete(f"{BASE_URL}/store/order/{order_data['id']}")

        # Log the status code
        logger.info(f"DELETE {BASE_URL}/store/order/{order_data['id']} - Status Code: {response.status_code}")

        # Check the status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    def test_order_not_found(self, logger, order_data):
        # GET request to check if the order was deleted
        response = requests.get(f"{BASE_URL}/store/order/{order_data['id']}")

        # Log the status code and response
        logger.info(
            f"GET {BASE_URL}/store/order/{order_data['id']} - Status Code: {response.status_code}, Response: {response.json()}")

        # Check the status code
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"


if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pytest.main([f"--html=report_{timestamp}.html", "-s", "-v", "--capture=tee-sys"])
