from .ini import OAUTH_CREDENTIALS

class OAuthSignIn(object):
  providers = None

  def __init__(self, provider_name):
    self.provider_name = provider_name
    credentials = OAUTH_CREDENTIALS[provider_name]
    self.consumer_id = credentials['id']
    self.consumer_secret = credentials['secret']

  ## initiates the authorization process
  def authorize(self):
    pass

  ## after authorization is complete, provider redirects back to app
  def callback(self):
    pass

  def get_callback_url(self):
    return url_for('oauth_callback', provider=self.provider_name, _external=True)

  @classmethod
  def get_provider(self, provider_name):
    if self.provider is None:
      self.providers = {}
      for provider_class in self.__subclasses__():
        provider = provider_class()
        self.providers[provider.provider_name] = provider
    return self.providers[provider_name]

class FacebookSignIn(OAuthSignIn):
  pass