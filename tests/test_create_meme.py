def test_create_meme_positive(create_meme_endpoint):
    body = {
        "text": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"],
        "info": {"format": "jpeg"}
    }
    create_meme_endpoint.create_meme(payload=body)
    create_meme_endpoint.check_status_code(200)
    create_meme_endpoint.check_values_matches()

def test_create_meme_invalid_body(create_meme_endpoint):
    body = {
        "textddd": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"]
    }
    create_meme_endpoint.create_meme(payload=body)
    create_meme_endpoint.check_status_code(400)

def test_create_meme_not_json_body(create_meme_endpoint):
    body = None
    create_meme_endpoint.create_meme(payload=body)
    create_meme_endpoint.check_status_code(500)