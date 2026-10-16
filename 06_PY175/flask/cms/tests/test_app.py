import unittest
import shutil
import os
from app import app

class CMSTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.data_path = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(self.data_path, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.data_path, ignore_errors=True)

    def create_document(self, name, content=""):
        with open(os.path.join(self.data_path, name), "w") as file:
            file.write(content)

    def test_index(self):
        self.create_document("about.md")
        self.create_document("changes.txt")

        with self.client.get("/") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn("about.md", response.get_data(as_text=True))
            self.assertIn("changes.txt", response.get_data(as_text=True))

    def test_viewing_text_document(self):
        self.create_document("history.txt",
                             "Python 0.9.0 (initial release) is released.")

        with self.client.get("/history.txt") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/plain; charset=utf-8")
            self.assertIn("Python 0.9.0 (initial release) is released.", response.get_data(as_text=True))

    def test_document_not_found(self):
        # Attempt to access a nonexistent file and verify a redirect happens
        with self.client.get("/notafile.ext") as response:
            self.assertEqual(response.status_code, 302)
        # Verify redirect and message handling works
        with self.client.get(response.headers["Location"]) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("notafile.ext does not exist",
                          response.get_data(as_text=True))

        # Assert that a page reload removes the message
        with self.client.get("/") as response:
            self.assertNotIn("notafile.ext does not exist",
                             response.get_data(as_text=True))

    def test_viewing_markdown_document(self):
        self.create_document("about.md", "*This* is my **app**.")

        with self.client.get("/about.md") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn("<p><em>This</em> is my <strong>app</strong>.</p>", response.get_data(as_text=True))

    def test_editing_document(self):
        self.create_document("changes.txt")

        with self.client.get("/changes.txt/edit") as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("<textarea", response.get_data(as_text=True))
            self.assertIn('<button type="submit"', response.get_data(as_text=True))

    def test_updating_document(self):
        self.create_document("changes.txt", content="old content")

        with self.client.post("/changes.txt",
                              data={'content': "new content"}) as response:
            self.assertEqual(response.status_code, 302)

        with self.client.get(response.headers["Location"]) as follow_response:
            self.assertIn("changes.txt has been updated",
                          follow_response.get_data(as_text=True))

        with self.client.get("/changes.txt") as content_response:
            self.assertEqual(content_response.status_code, 200)
            self.assertIn("new content",
                          content_response.get_data(as_text=True))

    def test_view_new_document_form(self):
        with self.client.get("/new") as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("<input", response.get_data(as_text=True))
            self.assertIn('<button type="submit"', response.get_data(as_text=True))

    def test_create_new_document(self):
        with self.client.post("/create",
                              data={"filename": "test.txt"},
                              follow_redirects=True) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("test.txt has been created",
                          response.get_data(as_text=True))

        with self.client.get("/") as index_response:
            self.assertIn("test.txt", index_response.get_data(as_text=True))

    def test_create_new_document_without_filename(self):
        with self.client.post("/create", data={"filename": ""}) as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("A name is required", response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
