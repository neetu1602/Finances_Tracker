from app.core.security import (
    get_password_hash,
    verify_password
)

password = "Welcome@123"

hashed = get_password_hash(password)

print("Original :", password)
print("Hash     :", hashed)

print(
    verify_password(
        "Welcome@123",
        hashed
    )
)

print(
    verify_password(
        "WrongPassword",
        hashed
    )
)