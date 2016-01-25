class ProjectTests():

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)