import allure

from endpoints.endpoint import AuthorizedEndpoint


class ChangeMeme(AuthorizedEndpoint):

    @allure.step('Sending put request')
    def change_meme(self, payload, meme_id = None):
        self.payload = payload
        self.request(f'{self.url}/{meme_id or payload["id"]}', method='PUT', payload=payload)
        self.response_formatted_to_json = self.response.json() if self.response.status_code == 200 else None
        return self.response

    @allure.step('Check that payload values matches response values')
    def check_values_matches(self):
        for key, value in self.payload.items():
            if key == 'id':
                assert self.response_formatted_to_json[key] == str(value)
                continue
            assert self.response_formatted_to_json[key] == value
