# test_script.py

from datetime import datetime
import pytest
import requests
import logging
from common import BASE_URL, PET_DATA


class TestPetstoreAPI:

    def test_create_pet(self):
        response = requests.post(f"{BASE_URL}/pet", json=PET_DATA)
        logging.info(f"Test data: {PET_DATA}")
        logging.info(f"Response: {response.text}")
        assert response.status_code == 200, f"Status code is not 200, response: {response.text}"
        assert 'id' in response.json(), f"ID not in response, response: {response.text}"
        assert response.json()['name'] == PET_DATA['name'], f"Incorrect pet name, response: {response.text}"
        assert response.json()['status'] == PET_DATA['status'], f"Incorrect pet status, response: {response.text}"

    def test_get_pet_by_id(self):
        response = requests.get(f"{BASE_URL}/pet/{PET_DATA['id']}")
        logging.info(f"Test data: {PET_DATA}")
        logging.info(f"Response: {response.text}")
        assert response.status_code == 200, f"Status code is not 200, response: {response.text}"
        assert response.json()['id'] == PET_DATA['id'], f"Incorrect pet id, response: {response.text}"
        assert response.json()['name'] == PET_DATA['name'], f"Incorrect pet name, response: {response.text}"
        assert response.json()['status'] == PET_DATA['status'], f"Incorrect pet status, response: {response.text}"

    def test_update_pet(self):
        response = requests.put(f"{BASE_URL}/pet", json=PET_DATA)
        logging.info(f"Test data: {PET_DATA}")
        logging.info(f"Response: {response.text}")
        assert response.status_code == 200, f"Status code is not 200, response: {response.text}"
        assert 'id' in response.json(), f"ID not in response, response: {response.text}"
        assert response.json()['name'] == PET_DATA['name'], f"Incorrect pet name, response: {response.text}"
        assert response.json()['status'] == PET_DATA['status'], f"Incorrect pet status, response: {response.text}"

    def test_find_pets_by_status(self):
        response = requests.get(f"{BASE_URL}/pet/findByStatus", params={"status": "available"})
        logging.info(f"Test data: {PET_DATA}")
        logging.info(f"Response: {response.text}")
        assert response.status_code == 200, f"Status code is not 200, response: {response.text}"
        assert isinstance(response.json(), list), f"Response is not a list, response: {response.text}"
        assert len(response.json()) > 0, f"No pets found, response: {response.text}"
        assert all(pet['status'] == 'available' for pet in
                   response.json()), f"Not all pets have status 'available', response: {response.text}"


if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pytest.main([f"--html=report_{timestamp}.html", "-s", "-v", "--capture=tee-sys"])
