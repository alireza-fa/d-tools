from django.test import SimpleTestCase
from uuid import uuid4

from d_tools.file.base import change_filename_to_uuid4


class TestFile(SimpleTestCase):

    def test_change_filename_to_uuid4(self):
        new_filename = change_filename_to_uuid4(filename="image.png")
        self.assertNotEquals("image.png", new_filename)
        uuid = uuid4()
        new_filename = change_filename_to_uuid4(filename="image.png", uuid=uuid)
        self.assertEqual("%s.png" % str(uuid), new_filename)
