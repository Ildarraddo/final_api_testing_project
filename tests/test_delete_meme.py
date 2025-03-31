def test_delete_meme_success(meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_code(200)

def test_delete_meme_not_found(delete_meme_endpoint):
    wrong_id = 999999
    delete_meme_endpoint.delete_meme(wrong_id)
    delete_meme_endpoint.check_status_code(404)

def test_delete_meme_forbidden(delete_meme_endpoint):
    wrong_id = 1
    delete_meme_endpoint.delete_meme(wrong_id)
    delete_meme_endpoint.check_status_code(403)