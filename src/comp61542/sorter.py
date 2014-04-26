
class Sorter:

    def sort_asc(self, data, index):   
        
#         return data.sort(key=lambda tup: tup[index])
        for idx in range(0, len(data)):
            tmpAuthor = list(data[idx])
            # Split the name into an array
#             print tmpAuthor[0]
            
            nameArray = str(tmpAuthor[0]) .split(" ")
            
#             print len(nameArray)
            
            if len(nameArray) >1:                      
                # The name is the first item in the list 
                name = nameArray[0]
                # Position of surname is the last item in the list
                surnamePos = len(nameArray) - 1
                # Get surname
                surname = nameArray[surnamePos] 
                # Join the surname+name using "_"
                toSortName = "_".join([surname,name])
    #             print toSortName
                # Make the first entry the newly created joined name
                nameArray[0] = toSortName
                # Remove the surname 
                nameArray.pop()     
                # Join the new name     
                tmpAuthor[0] = " ".join(nameArray)

                data[idx] = tuple(tmpAuthor)
#             print data[idx][0]
                     
        data = sorted(data, key=lambda tup: tup[0])
        if index != 0: 
            data = sorted(data, key=lambda tup: tup[index])

        for idx in range(0, len(data)):
            tmpAuthor = list(data[idx])
            # Split the name using spaces
            nameArray = str(tmpAuthor[0]).split(" ")
#             print nameArray
            # Take the Join surname_name
            nameSurName = nameArray[0]
            # Split them using "_"
            tmpArray = nameSurName.split("_")
            if len(tmpArray) > 1:
                # Take surname and name from list
                surName = tmpArray[0]
                name  = tmpArray[1]
                # Name takes it's correct position
                nameArray[0] = name
                # Surname goes last
                nameArray.append(surName)
             
            # Join the name and place it in the author data
            tmpAuthor[0] = " ".join(nameArray)                 
            
            data[idx] = tuple(tmpAuthor)
#             print author

        return data

    def sort_desc(self, data, index):                        
        for idx in range(0, len(data)):
            tmpAuthor = list(data[idx])
#             print tmpAuthor
            # Split the name into an array
            nameArray = str(tmpAuthor[0]).split(" ")
            
#             print "after split"
            
            if len(nameArray) > 1:
                # The name is the first item in the list 
                name = nameArray[0]
                # Position of surname is the last item in the list
                surnamePos = len(nameArray) - 1
                # Get surname
                surname = nameArray[surnamePos] 
                # Join the surname+name using "_"
                toSortName = "_".join([surname,name])
    #             print toSortName
                # Make the first entry the newly created joined name
                nameArray[0] = toSortName
                # Remove the surname 
                nameArray.pop()     
                # Join the new name     
                tmpAuthor[0] = " ".join(nameArray)
    #             print author[0]
                data[idx] = tuple(tmpAuthor)
                
        data = sorted(data, key=lambda tup: tup[0], reverse=True)
        if index != 0:  
            data = sorted(data, key=lambda tup: tup[index], reverse=True)
        for idx in range(0, len(data)):
            tmpAuthor = list(data[idx])
            # Split the name using spaces
            nameArray = str(tmpAuthor[0]).split(" ")          
            # Take the Join surname_name
            nameSurName = nameArray[0]
            # Split them using "_"
            tmpArray = nameSurName.split("_")
            if len(tmpArray) > 1:
                # Take surname and name from list
                surName = tmpArray[0]
                name  = tmpArray[1]
                # Name takes it's correct position
                nameArray[0] = name
                # Surname goes last
                nameArray.append(surName)
                # Join the name and place it in the author data
            tmpAuthor[0] = " ".join(nameArray)                 
#             print author[0]
            data[idx] = tuple(tmpAuthor)
        return data
    