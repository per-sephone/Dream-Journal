from flask import redirect, request, url_for, session
from requests_oauthlib import OAuth2Session
from flask.views import MethodView
from oauth_config import client_id, client_secret, token_url, redirect_callback

class Callback(MethodView):
    def get(self):
        google = OAuth2Session(client_id, redirect_uri=redirect_callback, state=session['oauth_state'])
        request.url = request.url.replace('http:','https:')
        token = google.fetch_token(token_url, client_secret=client_secret,
                            authorization_response=request.url)
        session['oauth_token'] = token
        return redirect(url_for('index'))