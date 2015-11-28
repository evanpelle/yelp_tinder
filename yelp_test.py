from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="6U-EYdtGCpNoaq5PqqQz-g",
    consumer_secret="RfOJP1Dlzz-J0h-k1fu9O_tdMT8",
    token="0WujndcH-wshwjSHdTm1x-hWh52YytIX",
    token_secret="3O1Nyl4E2glK5Eo3MzrjlEXoOMw"  
)

client = Client(auth)