from django.test import TestCase
from .models import Artifact

class ArtifactTests(TestCase):

    def test_str(self):
        test_name = Artifact(name='An Artifact')
        self.assertEqual(str(test_name), 'An Artifact')
