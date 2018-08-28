from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from ..factories import ForumFactory, TopicFactory, TopicCommentFactory
from vote.factories import UserFactory


class ForumDetailTestCase(TestCase):
    def test_200(self):
        """Should return 200 if logged in. """

        forum = ForumFactory()
        user = UserFactory()
        url = forum.get_absolute_url()
        client = Client()
        client.force_login(user)
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_302(self):
        """Should return 302 if not logged in. """

        forum = ForumFactory()
        url = forum.get_absolute_url()
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 302)
        

class ForumCreateViewTestCase(TestCase):
    def test_200(self):
        """Should return 200 if logged in."""

        user = UserFactory()
        url = reverse("messageboard:forum_create")
        client = Client()
        data = {}
        client.force_login(user)
        response = client.get(url, data)

        self.assertEqual(response.status_code, 200)

    def test_302_successful_post(self):
        """Should return 302 if logged in and created successfully. """

        user = UserFactory()
        url = reverse("messageboard:forum_create")
        client = Client()
        data = {}
        client.force_login(user)
        response = client.post(url, data)

        self.assertEqual(response.status_code, 302)

    def test_302(self):
        """ Should return 302 if not logged in. """

        url = reverse("messageboard:forum_create")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 302)


class ForumListViewTestCase(TestCase):
    def test_200(self):
        """ Should return 200 if logged in. """

        user = UserFactory()
        url = reverse("messageboard:forum_list")
        client = Client()
        client.force_login(user)
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_302(self):
        """ Should return 302 if not logged in. """

        url = reverse("messageboard:forum_list")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 302)


class ForumDeleteViewTestCase(TestCase):
    def test_302(self):
        """ Should return 302 if logged in and successfully deleted."""

        forum = ForumFactory()
        user = UserFactory()
        # url = "/{}/forum_delete".format(forum.slug)
        url = reverse_lazy("messageboard:forum_delete", args=(forum.slug,))
        client = Client()
        client.force_login(user)
        response = client.post(url)

        self.assertEqual(response.status_code, 302)

    def test_302_no_user(self):
        """ Should return 302 if not logged in."""

        forum = ForumFactory()
        url = reverse_lazy("messageboard:forum_delete", args=(forum.slug,))
        client = Client()
        response = client.post(url)

        self.assertEqual(response.status_code, 302)


class TopicCreateViewTestCase(TestCase):
    def test_302(self):
        """Should return 302 if loggged in and created successfully."""

        user = UserFactory()
        forum = ForumFactory()
        data = {"forum_slug":forum.slug}
        url = reverse("messageboard:topic_create")
        client = Client()
        client.force_login(user)
        response = client.post(url, data)

        self.assertEqual(response.status_code, 302)

    def test_302_unsuccessful_post(self):
        """Should return 302 if not loggged in."""

        forum = ForumFactory()
        data = {"forum_slug":forum.slug}
        url = reverse("messageboard:topic_create")
        client = Client()
        response = client.post(url, data)

        self.assertEqual(response.status_code, 302)


class TopicDetailTestCase(TestCase):
    def test_200(self):
        """Should return 200 if logged in. """

        topic = TopicFactory()
        user = UserFactory()
        url = topic.get_absolute_url()
        client = Client()
        client.force_login(user)
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_302(self):
        """Should return 302 if not logged in. """

        topic = TopicFactory()
        url = topic.get_absolute_url()
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 302)


class TopicCommentCreateViewTestCase(TestCase):
    def test_302(self):
        """ Should return 302 if not logged in. """

        url = reverse("messageboard:topic_comment_create")
        client = Client()
        response = client.post(url)

        self.assertEqual(response.status_code, 302)
