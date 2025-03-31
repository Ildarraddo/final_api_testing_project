def test_get_one_meme_success(meme, get_meme_endpoint):
    get_meme_endpoint.get_one_meme(meme['id'])
    get_meme_endpoint.check_status_code(200)
    get_meme_endpoint.check_response_structure()

def test_get_one_meme_not_found(meme, get_meme_endpoint):
    wrong_id = 999999
    get_meme_endpoint.get_one_meme(wrong_id)
    get_meme_endpoint.check_status_code(404)
