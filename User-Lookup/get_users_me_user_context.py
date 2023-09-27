from requests_oauthlib import OAuth1Session
import os
import json

# In your terminal please set your environment variables by running the following lines of code.
# export 'API_KEY'='<your_api_key>'
# export 'API_SECRET_KEY'='<your_api_secret_key>'

api_key = os.environ.get("API_KEY")
api_secret_key = os.environ.get("API_SECRET_KEY")

# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld
fields = "created_at,description"
params = {"user.fields": fields}

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

# # Get authorization
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

response = oauth.get("https://api.twitter.com/2/users/me", params=params)

if response.status_code != 200:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

json_response = response.json()

print(json.dumps(json_response, indent=4, sort_keys=True))
