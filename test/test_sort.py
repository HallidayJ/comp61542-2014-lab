from os import path
import unittest

from comp61542 import sorter

class TestSearch(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        self.data_dir = path.join(dir, "..", "data")    
    
    def test_sort_asc(self):
        
        # 123
        data = [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ]
        # sort_asc(data_to_be_sorted, column_number_to_sort_on)
        _, sortedData = sorter.sort_asc(data,0)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        _, sortedData = sorter.sort_asc(data,2)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        # 132
        data = [ ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30) ]
        _, sortedData = sorter.sort_asc(data,0)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        _, sortedData = sorter.sort_asc(data,2)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        # 213
        data = [ ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26) ]
        _, sortedData = sorter.sort_asc(data,0)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        _, sortedData = sorter.sort_asc(data,2)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        #231
        data = [ ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10) ]
        _, sortedData = sorter.sort_asc(data,0)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        _, sortedData = sorter.sort_asc(data,2)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])        
        
        #312
        data = [ ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30) ]
        _, sortedData = sorter.sort_asc(data,0)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        _, sortedData = sorter.sort_asc(data,2)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
                
        #321
        data = [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ]
        _, sortedData = sorter.sort_asc(data,0)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
        
        _, sortedData = sorter.sort_asc(data,2)
        self.assertEqual(sortedData, [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ])
    
    def test_sort_desc(self):

        # 123
        data = [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26) ]
        # sort_desc(data_to_be_sorted, column_number_to_sort_on)
        _, sortedData = sorter.sort_desc(data,0)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        _, sortedData = sorter.sort_desc(data,2)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        # 132
        data = [ ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30) ]
        _, sortedData = sorter.sort_desc(data,0)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        _, sortedData = sorter.sort_desc(data,2)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        # 213
        data = [ ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10), ('Author3', 5, 6, 7, 8, 26) ]
        _, sortedData = sorter.sort_desc(data,0)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        _, sortedData = sorter.sort_desc(data,2)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        #231
        data = [ ('Author2', 6, 4, 6, 9, 30), ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10) ]
        _, sortedData = sorter.sort_desc(data,0)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        _, sortedData = sorter.sort_desc(data,2)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])       
        
        #312
        data = [ ('Author3', 5, 6, 7, 8, 26), ('Author1', 1, 2, 3, 4, 10), ('Author2', 6, 4, 6, 9, 30) ]
        _, sortedData = sorter.sort_desc(data,0)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        _, sortedData = sorter.sort_desc(data,2)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
                
        #321
        data = [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ]
        _, sortedData = sorter.sort_desc(data,0)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
        
        _, sortedData = sorter.sort_desc(data,2)
        self.assertEqual(sortedData, [ ('Author3', 5, 6, 7, 8, 26), ('Author2', 6, 4, 6, 9, 30), ('Author1', 1, 2, 3, 4, 10) ])
    
    
    
if __name__ == '__main__':
    unittest.main()