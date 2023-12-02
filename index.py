"""
Default view
Handles GET request for all entries in dream journal
Handles POST request to post a new entry
"""

from flask import render_template, request, url_for, redirect, session
from flask.views import MethodView
from requests_oauthlib import OAuth2Session
from oauth_config import client_id, authorization_base_url, redirect_callback
import gbmodel
from text_analysis import text_analysis
from image_gen import generate_image, save_img, get_img
from datetime import datetime


class Index(MethodView):
    def get(self):
        if 'oauth_token' in session:
            google = OAuth2Session(client_id, token=session['oauth_token'])
            user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
            model = gbmodel.get_model()
            entries = [dict(id=row[0], text=row[1], timestamp=row[2], sentiment=row[3], img=get_img(row[0])) for row in model.select()]
            return render_template('index.html',entries=entries)
        else: #no oauth
            google = OAuth2Session(client_id=client_id, redirect_uri=redirect_callback, scope='https://www.googleapis.com/auth/userinfo.email')
            authorization_url, state = google.authorization_url(authorization_base_url, prompt='login')
            session['oauth_state'] = state
            return redirect(authorization_url)
    
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        if 'oauth_token' in session:
            journal_text = request.form['text']
            model = gbmodel.get_model()
            sentiment = text_analysis(journal_text)
            base64_img = generate_image(journal_text)
            entry_id = model.insert(request.form['text'], datetime.now(), sentiment)
            save_img(id=entry_id, base64_img=base64_img)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
