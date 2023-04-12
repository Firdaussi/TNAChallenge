from django.test import TestCase
from challenge.models import TNARecord

# Create your tests here.
class TestAppModels(TestCase):

    def test_model_str_title_equal(self):
        # Check the __str__ method is using the title if present

        field = TNARecord.objects.create(
            tna_id="test_model_str_title_equal",
            title="Title",
            description="Description",
            citable="Citable")

        self.assertEqual(str(field), "Title")

    def test_model_str_description_equal(self):
        # Check the __str__ method is using the description if present and when
        # the title is empty

        field = TNARecord.objects.create(
            tna_id="test_model_str_description_equal",
            title=None,
            description="Description",
            citable="Citable")

        self.assertEqual(str(field), "Description")

    def test_model_str_citable_equal(self):
        # Check the __str__ method is using the citable if present and when
        # the title and description are empty

        field = TNARecord.objects.create(
            tna_id="test_model_str_citable_equal",
            title=None,
            description=None,
            citable="Citable")

        self.assertEqual(str(field), "Citable")

    def test_model_str_only_id_equal(self):
        # Check the __str__ method is using the tna_id if present and when
        # all other fields are empty

        field = TNARecord.objects.create(
            tna_id="test_model_str_only_id_equal",
            title=None,
            description=None,
            citable=None)

        self.assertEqual(str(field), "test_model_str_only_id_equal")

class TestAppViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        for x in range(20):
            field = TNARecord.objects.create(
                tna_id=f"id{x}",title=f"Title{x}", description=f"Description{x}", citable=f"Citable{x}")

        field = TNARecord.objects.create(tna_id='id-only');

    def test_view_list_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_details_url_exists_at_desired_location(self):
        response = self.client.get('/id1/')
        self.assertEqual(response.status_code, 200)

    def test_view_details_url_does_not_exist_at_desired_location(self):
        response = self.client.get('/id99/')
        self.assertEqual(response.status_code, 200)

    def test_view_details_when_no_fields_populated(self):
        response = self.client.get('/id-only/')
        self.assertEqual(response.status_code, 200)
        

