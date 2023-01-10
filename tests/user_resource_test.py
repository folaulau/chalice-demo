
import os

def test_get_home_success(mocker, test_client):
    # This is to test a successful request to the endpoint
    response = test_client.http.get(
        '/',
        headers={"Content-Type": "application/json",
                 "X-Api-Key": "my-good-api-key"},
    )
    assert response.status_code == 200

def test_get_name_success(mocker, test_client):

    # mocker.patch('controllers.UserResource.UserService.get_name', return_value = 'Sione')

    response = test_client.http.get(
        '/user/name',
        headers={"Content-Type": "application/json"},
    )
    res_json = response.json_body
    print("res_json:{}".format(res_json))
    assert response.status_code == 400
    assert res_json['name'] == 'John'

def test_get_status_success(mocker, test_client):
    # mocker.patch('controllers.UserController.UserService.get_name', return_value = 'Sione')

    response = test_client.http.get(
        '/user/status',
        headers={"Content-Type": "application/json"},
    )
    res_json = response.json_body
    assert res_json['status'] == 'Folau'
    assert response.status_code == 200