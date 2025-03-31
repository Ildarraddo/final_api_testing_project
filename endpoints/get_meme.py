import allure

from endpoints.endpoint import AuthorizedEndpoint


class GetMeme(AuthorizedEndpoint):

    @allure.step('Getting one meme')
    def get_one_meme(self, meme_id):
        self.request(f'{self.url}/{meme_id}')

    @allure.step('Check response structure')
    def check_response_structure(self):
        self.parsed_response = self.response.json()
        assert isinstance(self.parsed_response, dict)
        assert isinstance(self.parsed_response['id'], int)

