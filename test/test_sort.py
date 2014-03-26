from os import path
import unittest

from comp61542 import sorter
from comp61542.database import database

class TestSearch(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        self.data_dir = path.join(dir, "..", "data")    
    
#     def test_sort_asc(self):
#         sort = sorter.Sorter()
#         # 123
#         data = [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ]
#         # sort_asc(data_to_be_sorted, column_number_to_sort_on)
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         sortedData = sort.sort_asc(data,2)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         # 132
#         data = [ ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30) ]
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         sortedData = sort.sort_asc(data,2)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         # 213
#         data = [ ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26) ]
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         sortedData = sort.sort_asc(data,2)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         #231
#         data = [ ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10) ]
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         sortedData = sort.sort_asc(data,2)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])        
#         
#         #312
#         data = [ ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30) ]
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         sortedData = sort.sort_asc(data,2)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#                 
#         #321
#         data = [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ]
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#         
#         sortedData = sort.sort_asc(data,2)
#         self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
#     
#     def test_sort_desc(self):
#         sort = sorter.Sorter()
#         # 123
#         data = [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ]
#         # sort_desc(data_to_be_sorted, column_number_to_sort_on)
#         sortedData = sort.sort_desc(data,0)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         sortedData = sort.sort_desc(data,2)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         # 132
#         data = [ ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30) ]
#         sortedData = sort.sort_desc(data,0)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         sortedData = sort.sort_desc(data,2)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         # 213
#         data = [ ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26) ]
#         sortedData = sort.sort_desc(data,0)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         sortedData = sort.sort_desc(data,2)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         #231
#         data = [ ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10) ]
#         sortedData = sort.sort_desc(data,0)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         sortedData = sort.sort_desc(data,2)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])       
#         
#         #312
#         data = [ ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30) ]
#         sortedData = sort.sort_desc(data,0)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         sortedData = sort.sort_desc(data,2)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#                 
#         #321
#         data = [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ]
#         sortedData = sort.sort_desc(data,0)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         
#         sortedData = sort.sort_desc(data,2)
#         self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
#         self.assertNotEqual(sortedData, None)
#         
#     def test_surname_sorting(self):
#         sort = sorter.Sorter()
#                            
#         data = [('Andreas Vlachou', 3), ('Maria Charalambous', 6)]      
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [('Maria Charalambous', 6), ('Andreas Vlachou', 3)])
#                          
#         data = [('Andreas Vlachou', 6), ('Savvas Vlachou', 8)]      
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [('Andreas Vlachou', 6), ('Savvas Vlachou', 8)])                
#                        
#         data = [('Savvas Vlachou', 7), ('Andreas Vlachou', 9)]      
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [('Andreas Vlachou', 9), ('Savvas Vlachou', 7)])                               
#           
#         data = [('Savvas Vlachou', 5), ('Andreas Vlachou', 5), ('Maria Charalambous', 5), ('Oscar Wild', 6), ('Constantina Athanasiadou', 8)]      
#         sortedData = sort.sort_asc(data,0)
#         self.assertEqual(sortedData, [('Constantina Athanasiadou', 8), ('Maria Charalambous', 5), ('Andreas Vlachou', 5), ('Savvas Vlachou', 5), ('Oscar Wild', 6)])
#                             
#         db = database.Database()
#         self.assertTrue(db.read(path.join(self.data_dir, "dblp_sorting_example.xml")))
#         data = db.get_publications_by_author();       
#         sortedData = sort.sort_asc(data[1],0)      
#         self.assertEqual(sortedData, [('Philip A. Bernstein', 1, 0, 0, 0, 1), ('AnHai Doan', 0, 6, 0, 1, 7), ('Pedro Domingos', 1, 1, 0, 1, 3), ('Alon Y. Halevy', 2, 8, 0,1, 11), ('Jayant Madhavan', 1, 0, 0, 1, 2), ('Natalya Fridman Noy', 0, 4, 0, 0, 4)]) 


    def test_sorting_on_attr_other_than_surname(self):
        sort = sorter.Sorter()
#         data = [('Savvas Vlachou', 5), ('Andreas Vlachou', 5), ('Maria Charalambous', 5), ('Oscar Wild', 6), ('Constantina Athanasiadou', 8)]      
#         sortedData = sort.sort_asc(data,1)
#         self.assertEqual(sortedData, [('Maria Charalambous', 5), ('Andreas Vlachou', 5), ('Savvas Vlachou', 5), ('Oscar Wild', 6), ('Constantina Athanasiadou', 8)])

        db = database.Database()
        self.assertTrue(db.read(path.join(self.data_dir, "dblp_sorting_example.xml")))
        data = db.get_publications_by_year()  
        sortedData = sort.sort_asc(data[1],0, 1)      
        
         
if __name__ == '__main__':
    unittest.main()