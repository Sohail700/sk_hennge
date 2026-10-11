import base64
import hashlib
import hmac
import json
import time
import urllib.request


ENDPOINT = "https://api.challenge.hennge.com/challenges/backend-recursion/004"


def generate_totp(email):
    secret = (email + "HENNGECHALLENGE004").encode("ascii")

    counter = int(time.time()) // 30
    counter_bytes = counter.to_bytes(8, byteorder="big")

    digest = hmac.new(
        secret,
        counter_bytes,
        hashlib.sha512,
    ).digest()

    offset = digest[-1] & 0x0F

    binary = int.from_bytes(
        digest[offset:offset + 4],
        byteorder="big",
    ) & 0x7FFFFFFF

    otp = binary % 10**10

    return f"{otp:010d}"


def main():
    email = "suhaylkhan19@gmail.com"
    github_url = "https://gist.github.com/Sohail700/3438837f4fbbc0ff1bcb0077bb0e1dab"

    payload = {
        "github_url": github_url,
        "contact_email": email,
        "solution_language": "python",
    }

    body = json.dumps(payload).encode("utf-8")

    totp = generate_totp(email)

    credentials = f"{email}:{totp}".encode("utf-8")
    encoded_credentials = base64.b64encode(credentials).decode("ascii")

    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json",
            "Accept": "*/*",
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")

            print(f"HTTP {response.status}")
            print(response_body)

    except urllib.error.HTTPError as error:
        print(f"HTTP {error.code}")
        print(error.read().decode("utf-8"))


if __name__ == "__main__":
    main()
