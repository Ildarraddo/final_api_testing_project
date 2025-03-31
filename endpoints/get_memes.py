import allure

from endpoints.endpoint import Endpoint, AuthorizedEndpoint


class GetMemes(AuthorizedEndpoint):

    @allure.step('Getting all memes')
    def get_all_memes(self):
        self.request(self.url)
        # return self.response

    @allure.step('Check response structure')
    def check_response_structure(self):
        self.parsed_response = self.response.json()
        assert isinstance(self.parsed_response, dict)
        assert 'data' in self.parsed_response
        assert isinstance(self.parsed_response['data'], list)