def test_get_all_memes(meme, get_memes_endpoint):
    get_memes_endpoint.get_all_memes()
    get_memes_endpoint.check_status_code(200)
    get_memes_endpoint.check_response_structure()


