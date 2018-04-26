from uuid import uuid4

from django.test import TestCase
from oauth2_provider.models import AccessToken, Application, Grant, RefreshToken, Client
from student.tests.factories import UserFactory

from ..data_retirement_utils import (
    delete_from_oauth2_provider_accesstoken,
    delete_from_oauth2_provider_application,
    delete_from_oauth2_provider_grant,
    delete_from_oauth2_provider_refreshtoken,
    delete_from_oauth_consumer,
    delete_from_oauth_token,
)


class TestRetireUserFromOauth2AccessToken(TestCase):

    def setUp(self):
        super(TestRetireUserFromOauth2AccessToken, self).setUp()
        self.user = UserFactory.create()
        # self.client = Client.objects.create()

    def test_delete_from_oauth2_accesstoken(self):
        # token = AccessToken.objects.create(user=self.user, client=self.client)
        self.assertTrue(delete_from_oauth2_provider_accesstoken(self.user))
