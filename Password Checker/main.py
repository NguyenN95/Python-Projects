import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + str(query_char)
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the api and try again"
        )
    return response


def pwned_api_check(password: str):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_chars, tail = hashed_password[:5], hashed_password[5:]
    response = request_api_data(first5_chars)
    return get_password_leaks_count(response, tail)


def get_password_leaks_count(response: requests.Response, hash_to_check):
    hashes = (line.split(":") for line in response.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should probably change your password"
            )
        else:
            print(f"{password} was NOT found. Carry on!")
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
