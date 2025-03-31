def test_change_meme_positive(change_meme_endpoint, meme_id):
    body = {
        "id": meme_id,
        "text": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"],
        "info": {"format": "jpeg"}
    }
    change_meme_endpoint.change_meme(payload=body,meme_id=meme_id)
    change_meme_endpoint.check_status_code(200)
    change_meme_endpoint.check_values_matches()

def test_change_meme_invalid_body(change_meme_endpoint, meme_id):
    body = {
        "id": meme_id,
        "texeet": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"],
        "info": {"format": "jpeg"}
    }
    change_meme_endpoint.change_meme(payload=body)
    change_meme_endpoint.check_status_code(400)
    
def test_change_meme_not_json_body(change_meme_endpoint, meme_id):
    body = None
    change_meme_endpoint.change_meme(payload=body, meme_id=meme_id)
    change_meme_endpoint.check_status_code(500)

def test_change_meme_not_found(change_meme_endpoint):
    body = {
        "id": 999999,
        "text": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"],
        "info": {"format": "jpeg"}
    }
    change_meme_endpoint.change_meme(payload=body)
    change_meme_endpoint.check_status_code(404)

def test_change_meme_forbidden(change_meme_endpoint):
    body = {
        "id": 1,
        "text": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"],
        "info": {"format": "jpeg"}
    }
    change_meme_endpoint.change_meme(payload=body)
    change_meme_endpoint.check_status_code(403)