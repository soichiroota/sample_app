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