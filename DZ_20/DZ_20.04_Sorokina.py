import re


def validate_password(password):
    return re.findall(r"[a-z0-9_@-]{6,18}", password, flags=re.IGNORECASE)


print(validate_password("my-p@sSw0rd"))
