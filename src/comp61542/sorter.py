
class Sorter:

    def sort_asc(self, data, index):   
#         return data.sort(key=lambda tup: tup[index])
        return sorted(data, key=lambda tup: tup[index])

    def sort_desc(self, data, index):
#         return data.sort(key=lambda tup: tup[index], reverse=True)
        return sorted(data, key=lambda tup: tup[index], reverse=True)