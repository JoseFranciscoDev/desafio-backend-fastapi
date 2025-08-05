from jwt import decode

from api.security import create_access_token, SECRET_KEY


def test_jwt():
    data = {"teste": "teste"}
    token = create_access_token(data)
    decoded = decode(token, SECRET_KEY)

    assert decoded["test"] == data["teste"]
    assert "exp" in decoded
