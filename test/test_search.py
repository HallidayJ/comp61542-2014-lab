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
    
    def test_get_author_sole_on_paper_number(self):
        author = "Stefano Ceri"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, number = db.get_author_sole_on_paper_number(author)
        self.assertEqual(number, 8)
        
    def test_search_by_name_part(self):
        authorpart = "Car"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, data = db.get_author_details(authorpart)
        self.assertEqual(len(data), 23)
    
    def test_count_get_author_by_publication(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, data = db.get_author_publications(author)
        self.assertEqual(data, [[8, 9, 0, 1, 18]])

    def test_count_get_author_first_place_by_publication(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, data = db.get_author_first_place(author)
        self.assertEqual(data, [[2, 4, 0, 1, 7]])
  
    def test_count_get_author_last_place_by_publication(self):
        author = "Caroline Jay"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, data = db.get_author_last_place(author)
        self.assertEqual(data, [[1, 0 ,0 ,0 ,1]])
  
    def test_count_get_author_sole_place_by_publication(self):
        author = "Stefano Ceri"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_curated_sample.xml")))
        _, data = db.get_author_sole_place(author)
        self.assertEqual(data, [[7, 0, 0, 1, 8]])
        
    def test_degree_of_seperation_seperationof0(self):
        author1 = "Author A"
        author2 = "Author B"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_seperation_test.xml")))
        data = db.degree_of_separation(author1, author2)
        self.assertEqual(data, [0])
    
    def test_degree_of_seperation_seperationof1(self):
        author1 = "Author C"
        author2 = "Author D"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_seperation_test.xml")))
        data = db.degree_of_separation(author1, author2)
        self.assertEqual(data, [1])

    def test_degree_of_seperation_seperationof2(self):
        author1 = "Author E"
        author2 = "Author C"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_seperation_test.xml")))
        data = db.degree_of_separation(author1, author2)
        self.assertEqual(data, [2])

    def test_degree_of_seperation_noconnection(self):
        author1 = "Author A"
        author2 = "Author F"
        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_seperation_test.xml")))
        data = db.degree_of_separation(author1, author2)
        self.assertEqual(data, ["X"])

  
if __name__ == '__main__':
    unittest.main()