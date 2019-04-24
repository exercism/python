#!/usr/bin/env python
import requests
import json


# https://stackoverflow.com/a/17626704
class GitHub(object):
    def __init__(self, **config_options):
        self.__dict__.update(**config_options)
        self.session = requests.Session()
        if hasattr(self, 'api_token'):
            self.session.headers['Authorization'] = 'token %s' % self.api_token
        elif hasattr(self, 'username') and hasattr(self, 'password'):
            self.session.auth = (self.username, self.password)

    def create_issue(
        self,
        owner,
        repo,
        title,
        body=None,
        assignees=None,
        labels=None
    ):
        payload = dict(title=title)
        if body is not None:
            payload['body'] = body
        if assignees is not None:
            payload['assignees'] = assignees
        if labels is not None:
            payload['labels'] = labels
        response = self.session.post(
            'https://api.github.com/repos/{}/{}/issues'.format(owner, repo),
            data=json.dumps(payload),
        )
        if response.status_code != 201:
            raise ValueError('Failed to create issue: ' + response.content)
        return json.loads(response.content)
