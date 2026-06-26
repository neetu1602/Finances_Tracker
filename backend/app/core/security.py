from passlib.context import CryptContext


# Configure password hashing algorithm 
pwd_context = CryptContext(
  schemes=["bcrypt"],
  deprecated="auto"
)

#create hash function (plain password -> get_password_hash() --> Hashed Password )
def get_password_hash(password:str) ->str:
  return pwd_context.hash(password)

#create verify function (login password -> verify_password() -> stored hash -> true/false)
def verify_password(
    plain_password:str,
    hashed_password:str
) -> bool:
  return pwd_context.verify(
    plain_password,
    hashed_password
  )