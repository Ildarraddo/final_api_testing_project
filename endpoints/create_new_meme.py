import allure

from endpoints.endpoint import Endpoint, AuthorizedEndpoint


class CreateMeme(AuthorizedEndpoint):

    @allure.step('Creating new meme')
    def create_meme(self, payload):
        self.payload = payload
        self.request(self.url, method='POST', payload=self.payload)
        self.response_formatted_to_json = self.response.json() if self.response.status_code == 200 else None
        return self.response

    @allure.step('Check that payload values matches response values')
    def check_values_matches(self):
        for key, value in self.payload.items():
            assert self.response_formatted_to_json[key] == value