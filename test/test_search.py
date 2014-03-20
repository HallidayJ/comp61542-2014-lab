from os import path
import unittest

from comp61542.database import database

class TestSearch(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        self.data_dir = path.join(dir, "..", "data")    
    
    def test_get_author_publication_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_publication_number(author)
        self.assertEqual(number, 18)
    
    def test_get_author_conference_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_conference_number(author)
        self.assertEqual(number, 8)
    
    
    def test_get_author_journal_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_journal_number(author)
        self.assertEqual(number, 9)
    
    def test_get_author_bookchapter_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_bookchapter_number(author)
        self.assertEqual(number, 1)
    
    def test_get_author_book_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_book_number(author)
        self.assertEqual(number, 0)
        
    def test_get_author_coauthor_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_coauthor_number(author)
        self.assertEqual(number, 20)
    
    def test_get_author_first_on_paper_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_first_on_paper_number(author)
        self.assertEqual(number, 7)
        
    def test_get_author_last_on_paper_number(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_last_on_paper_number(author)
        self.assertEqual(number, 1)
    
if __name__ == '__main__':
    unittest.main()