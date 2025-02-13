from requests_oauthlib import OAuth1Session
import os
import json

# In your terminal please set your environment variables by running the following lines of code.
# export 'API_KEY'='<your_api_key>'
# export 'API_SECRET_KEY'='<your_api_secret_key>'
api_key = os.environ.get("API_KEY")
api_secret_key = os.environ.get("API_SECRET_KEY")

# Be sure to replace your-user-id with your own user ID or one of an authenticated user
# You can find a user ID by using the user lookup endpoint
id = "your-user-id"

# You can replace Tweet ID given with the Tweet ID you wish to like.
# You can find a Tweet ID by using the Tweet lookup endpoint
tweet_id = "1354143047324299264"

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(api_key, client_secret=api_secret_key)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the api_key or api_secret_key you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    api_key,
    client_secret=api_secret_key,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    api_key,
    client_secret=api_secret_key,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.delete(
    "https://api.twitter.com/2/users/{}/likes/{}".format(id, tweet_id)
)

if response.status_code != 200:
    raise Exception(
        "Request returned an error: {} {}".format(
            response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
