# Twitter API v2 sample code [![v2](https://img.shields.io/endpoint?url=https%3A%2F%2Ftwbadges.glitch.me%2Fbadges%2Fv2)](https://developer.twitter.com/en/docs/twitter-api)

Sample code for the Twitter API v2 endpoints.
Individual API features have folders where you can find examples of usage in several coding languages (Java, Node.js, Python, R, and Ruby).

* [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)

## Prerequisites

* Twitter API Essential Access ([sign up here](https://t.co/signup))
* A Project and an App created [in the dashboard](https://developer.twitter.com/en/portal/dashboard)

## Using the code samples

In order to run the samples in this repository you will need to set up some environment variables. You can find your credentials and bearer token in the App inside of your Project in the [dashboard of the developer portal](https://developer.twitter.com/en/portal/projects-and-apps).

For OAuth 1.0a samples, you will need to export your consumer key and secret in your terminal. Be sure to replace `<your_consumer_key>` and `<your_consumer_secret>` with your own credentials without the `< >`.

```bash
export CONSUMER_KEY='<your_consumer_key>'
export CONSUMER_SECRET='<your_consumer_secret>'
```

For samples which use bearer token authentication, you will need to export the bearer token. Be sure to replace  `<your_bearer_token>` with your own bearer token without the `< >`.

```bash
export BEARER_TOKEN='<your_bearer_token>'
```

## programming language requirements

### Python environment set up

You will need to have Python 3 installed to run this code. The Python samples use `requests==2.24.0` which uses `requests-oauthlib==1.3.0`.

(Optionally) It is common and recommended not to install required package globally, but locally under project subfolder using `venv`:

```bash
python3 -m venv venv
source venv/bin/activate
```

You can install these packages as follows:

```bash
pip install -r requirements
```

## Additional resources

We maintain a [Postman](https://getpostman.com) Collection which you can use for exercising individual API endpoints.

* [Using Postman with the Twitter API](https://developer.twitter.com/en/docs/tutorials/postman-getting-started)
* [Twitter API v2 on the Postman website](https://t.co/twitter-api-postman)

## Support

* For general questions related to the API and features, please use the v2 section of our [developer community forums](https://twittercommunity.com/c/twitter-api/twitter-api-v2/65).

* If there's an bug or issue with the sample code itself, please create a [new issue](https://github.com/twitterdev/Twitter-API-v2-sample-code/issues) here on GitHub.

## Contributing

We welcome pull requests that add meaningful additions to these code samples, particularly for languages that are not yet represented here.

We feel that a welcoming community is important and we ask that you follow Twitter's [Open Source Code of Conduct](https://github.com/twitter/.github/blob/main/code-of-conduct.md) in all interactions with the community.

## License

Copyright 2021 Twitter, Inc.

Licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0

# house cleaning (remove non python enpoint files)
```bash
E='\.java'; for I in $(tree -P *$E -f -i | grep -e "$E"); do rm $I; done
E='\.r'; for I in $(tree -P *$E -f -i | grep -e "$E"); do rm $I; done
E='\.rb'; for I in $(tree -P *$E -f -i | grep -e "$E"); do rm $I; done
E='\.js'; for I in $(tree -P *$E -f -i | grep -e "$E"); do rm $I; done
```
