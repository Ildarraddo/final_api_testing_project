import allure
import requests


class Endpoint:
    base_url = 'http://167.172.172.115:52355'
    url = f'{base_url}/meme'
    url_for_auth = f'{base_url}/authorize'
    test_user = 'IIM'
    response = None
    response_formatted_to_json = None

    def authorization(self):
        response = requests.post(f'{self.url_for_auth}', json={"name": self.test_user})
        return response.json()['token']

    def delete_meme(self, meme_id):
        requests.delete(f'{self.url}/{meme_id}')

    @allure.step('Check status code')
    def check_status_code(self, code):
        assert self.response.status_code == code

    # @allure.step('Check that response is not success')
    # def check_that_status_is_not_200(self):
    #     assert self.response.status_code != 200




class AuthorizedEndpoint(Endpoint):

    def __init__(self, token):
        self.token = token

    def request(self, url, method = "GET", payload = None, token = None):
        self.response = requests.request(method, url, json=payload, headers={"Authorization": token or self.token})

