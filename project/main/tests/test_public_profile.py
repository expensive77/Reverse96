from .test_setUp import Test_SetUp
from django.contrib.auth import get_user_model


class TestPublicProfileView(Test_SetUp):

    def test_user_can_get_existing_public_profile(self):
        user = get_user_model().objects.create_user(
            username=self.user_data['username'],
            password=self.user_data['password'],
            phone_number=self.user_data['phone_number'],
            address=self.user_data['address'],
            email=self.user_data['email'],
            name=self.user_data['name'],
            is_active=True
        )
        user2 = get_user_model().objects.create_user(
            username=self.user_data2['username'],
            password=self.user_data2['password'],
            phone_number=self.user_data2['phone_number'],
            address=self.user_data2['address'],
            email=self.user_data2['email'],
            name=self.user_data2['name'],
            is_active=True
        )

        data = {
            "username": self.user_data['username'],
            "password": self.user_data['password'],
        }
        res = self.client.post(self.login_url, data, format='json')

        public_profile_url = f"/api/public-profile/{user2.username}"
        header =self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % res.json()['access'])
        response = self.client.get(public_profile_url, format="json")
        #import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_user_cant_see_non_existing_user(self):
        user = get_user_model().objects.create_user(
            username=self.user_data['username'],
            password=self.user_data['password'],
            phone_number=self.user_data['phone_number'],
            address=self.user_data['address'],
            email=self.user_data['email'],
            name=self.user_data['name'],
            is_active=True
        )
        data = {
            "username": self.user_data['username'],
            "password": self.user_data['password'],
        }
        res = self.client.post(self.login_url, data, format='json')

        public_profile_url = f"/api/public-profile/dfjksf"
        header = self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % res.json()['access'])
        response = self.client.get(public_profile_url, format="json")
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 404)


    def test_user_can_get_public_profile_with_wrong_access_token(self):
        user = get_user_model().objects.create_user(
            username=self.user_data['username'],
            password=self.user_data['password'],
            phone_number=self.user_data['phone_number'],
            address=self.user_data['address'],
            email=self.user_data['email'],
            name=self.user_data['name'],
            is_active=True
        )
        user2 = get_user_model().objects.create_user(
            username=self.user_data2['username'],
            password=self.user_data2['password'],
            phone_number=self.user_data2['phone_number'],
            address=self.user_data2['address'],
            email=self.user_data2['email'],
            name=self.user_data2['name'],
            is_active=True
        )

        data = {
            "username": self.user_data['username'],
            "password": self.user_data['password'],
        }
        res = self.client.post(self.login_url, data, format='json')

        public_profile_url = f"/api/public-profile/{user2.username}"
        header =self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % f"{res.json()['access']}h")
        response = self.client.get(public_profile_url, format="json")
        #import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 401)