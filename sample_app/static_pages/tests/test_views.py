from django.test import TestCase


class TestHelpView(TestCase):

    def setUp(self):
        pass

    def test_get_success(self):
        # テストクライアントでGETリクエストをシミュレート
        response = self.client.get('/static_pages/help/')

        # レスポンスを検証する
        self.assertEqual(response.status_code, 200)
        # エラーメッセージが出ないことを検証
        self.assertTemplateUsed(response, 'static_pages/help.html')


class TestHomeView(TestCase):

    def setUp(self):
        pass

    def test_get_success(self):
        # テストクライアントでGETリクエストをシミュレート
        response = self.client.get('/static_pages/home/')

        # レスポンスを検証する
        self.assertEqual(response.status_code, 200)
        # エラーメッセージが出ないことを検証
        self.assertTemplateUsed(response, 'static_pages/home.html')

        response = self.client.get('')

        # レスポンスを検証する
        self.assertEqual(response.status_code, 200)
        # エラーメッセージが出ないことを検証
        self.assertTemplateUsed(response, 'static_pages/home.html')


class TestAboutView(TestCase):

    def setUp(self):
        pass

    def test_get_success(self):
        # テストクライアントでGETリクエストをシミュレート
        response = self.client.get('/static_pages/about/')

        # レスポンスを検証する
        self.assertEqual(response.status_code, 200)
        # エラーメッセージが出ないことを検証
        self.assertTemplateUsed(response, 'static_pages/about.html')


class TestContactView(TestCase):

    def setUp(self):
        pass

    def test_get_success(self):
        # テストクライアントでGETリクエストをシミュレート
        response = self.client.get('/static_pages/contact/')

        # レスポンスを検証する
        self.assertEqual(response.status_code, 200)
        # エラーメッセージが出ないことを検証
        self.assertTemplateUsed(response, 'static_pages/contact.html')