import allure

from endpoints.endpoint import AuthorizedEndpoint


class DeleteMeme(AuthorizedEndpoint):
    @allure.step('Deleting meme')
    def delete_meme(self, meme_id):
        self.request(f'{self.url}/{meme_id}', method='DELETE')
        return self.response