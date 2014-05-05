from comp61542.statistics import average
from comp61542 import sorter
import itertools
import numpy as np
import re
from xml.sax import handler, make_parser, SAXException

PublicationType = [
    "Conference Paper", "Journal", "Book", "Book Chapter"]

class Publication:
    CONFERENCE_PAPER = 0
    JOURNAL = 1
    BOOK = 2
    BOOK_CHAPTER = 3

    def __init__(self, pub_type, title, year, authors):
        self.pub_type = pub_type
        self.title = title
        if year:
            self.year = int(year)
        else:
            self.year = -1
        self.authors = authors

class Author:
    def __init__(self, name):
        self.name = name

class Stat:
    STR = ["Mean", "Median", "Mode"]
    FUNC = [average.mean, average.median, average.mode]
    MEAN = 0
    MEDIAN = 1
    MODE = 2

class MyQUEUE: # just an implementation of a queue
    
    def __init__(self):
        self.holder = []
        
    def enqueue(self,val):
        self.holder.append(val)
        
    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]    
        except:
            pass
            
        return val    
        
    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result

class Database:
    def read(self, filename):
        self.publications = []
        self.authors = []
        self.author_idx = {}
        self.min_year = None
        self.max_year = None

        handler = DocumentHandler(self)
        parser = make_parser()
        parser.setContentHandler(handler)
        infile = open(filename, "r")
        valid = True
        try:
            parser.parse(infile)
        except SAXException as e:
            valid = False
            print "Error reading file (" + e.getMessage() + ")"
        infile.close()

        for p in self.publications:
            if self.min_year == None or p.year < self.min_year:
                self.min_year = p.year
            if self.max_year == None or p.year > self.max_year:
                self.max_year = p.year

        return valid

    def get_all_authors(self):
        return self.author_idx.keys()

    def get_coauthor_data(self, start_year, end_year, pub_type):
        coauthors = {}
        for p in self.publications:
            if ((start_year == None or p.year >= start_year) and
                (end_year == None or p.year <= end_year) and
                (pub_type == 4 or pub_type == p.pub_type)):
                for a in p.authors:
                    for a2 in p.authors:
                        if a != a2:
                            try:
                                coauthors[a].add(a2)
                            except KeyError:
                                coauthors[a] = set([a2])
        def display(db, coauthors, author_id):
            return "%s (%d)" % (db.authors[author_id].name, len(coauthors[author_id]))

        header = ("Author", "Co-Authors")
        data = []
        for a in coauthors:
            data.append([ display(self, coauthors, a),
                ", ".join([
                    display(self, coauthors, ca) for ca in coauthors[a] ]) ])

        return (header, data)

    def get_average_authors_per_publication(self, av):
        header = ("Conference Paper", "Journal", "Book", "Book Chapter", "All Publications")

        auth_per_pub = [[], [], [], []]

        for p in self.publications:
            auth_per_pub[p.pub_type].append(len(p.authors))

        func = Stat.FUNC[av]

        data = [ func(auth_per_pub[i]) for i in np.arange(4) ] + [ func(list(itertools.chain(*auth_per_pub))) ]
        return (header, data)

    def get_average_publications_per_author(self, av):
        header = ("Conference Paper", "Journal", "Book", "Book Chapter", "All Publications")

        pub_per_auth = np.zeros((len(self.authors), 4))

        for p in self.publications:
            for a in p.authors:
                pub_per_auth[a, p.pub_type] += 1

        func = Stat.FUNC[av]

        data = [ func(pub_per_auth[:, i]) for i in np.arange(4) ] + [ func(pub_per_auth.sum(axis=1)) ]
        return (header, data)

    def get_average_publications_in_a_year(self, av):
        header = ("Conference Paper",
            "Journal", "Book", "Book Chapter", "All Publications")

        ystats = np.zeros((int(self.max_year) - int(self.min_year) + 1, 4))

        for p in self.publications:
            ystats[p.year - self.min_year][p.pub_type] += 1

        func = Stat.FUNC[av]

        data = [ func(ystats[:, i]) for i in np.arange(4) ] + [ func(ystats.sum(axis=1)) ]
        return (header, data)

    def get_average_authors_in_a_year(self, av):
        header = ("Conference Paper",
            "Journal", "Book", "Book Chapter", "All Publications")

        yauth = [ [set(), set(), set(), set(), set()] for _ in range(int(self.min_year), int(self.max_year) + 1) ]

        for p in self.publications:
            for a in p.authors:
                yauth[p.year - self.min_year][p.pub_type].add(a)
                yauth[p.year - self.min_year][4].add(a)

        ystats = np.array([ [ len(S) for S in y ] for y in yauth ])

        func = Stat.FUNC[av]

        data = [ func(ystats[:, i]) for i in np.arange(5) ]
        return (header, data)

    def get_publication_summary_average(self, av):
        header = ("Details", "Conference Paper",
            "Journal", "Book", "Book Chapter", "All Publications")

        pub_per_auth = np.zeros((len(self.authors), 4))
        auth_per_pub = [[], [], [], []]

        for p in self.publications:
            auth_per_pub[p.pub_type].append(len(p.authors))
            for a in p.authors:
                pub_per_auth[a, p.pub_type] += 1

        name = Stat.STR[av]
        func = Stat.FUNC[av]

        data = [
            [name + " authors per publication"]
                + [ func(auth_per_pub[i]) for i in np.arange(4) ]
                + [ func(list(itertools.chain(*auth_per_pub))) ],
            [name + " publications per author"]
                + [ func(pub_per_auth[:, i]) for i in np.arange(4) ]
                + [ func(pub_per_auth.sum(axis=1)) ] ]
        return (header, data)

    def get_publication_summary(self):
        header = ("Details", "Conference Paper",
            "Journal", "Book", "Book Chapter", "Total")

        plist = [0, 0, 0, 0]
        alist = [set(), set(), set(), set()]

        for p in self.publications:
            plist[p.pub_type] += 1
            for a in p.authors:
                alist[p.pub_type].add(a)
        # create union of all authors
        ua = alist[0] | alist[1] | alist[2] | alist[3]

        data = [
            ["Number of publications"] + plist + [sum(plist)],
            ["Number of authors"] + [ len(a) for a in alist ] + [len(ua)] ]
        return (header, data)

    def get_average_authors_per_publication_by_author(self, av):
        header = ("Author", "Number of conference papers",
            "Number of journals", "Number of books",
            "Number of book chapers", "All publications")

        astats = [ [[], [], [], []] for _ in range(len(self.authors)) ]
        for p in self.publications:
            for a in p.authors:
                astats[a][p.pub_type].append(len(p.authors))

        func = Stat.FUNC[av]

        data = [ [self.authors[i].name]
            + [ func(L) for L in astats[i] ]
            + [ func(list(itertools.chain(*astats[i]))) ]
            for i in range(len(astats)) ]
        return (header, data)

    def get_publications_by_author(self):
        header = ("Author", "Number of conference papers",
            "Number of journals", "Number of books",
            "Number of book chapers", "Total")

        astats = [ [0, 0, 0, 0] for _ in range(len(self.authors)) ]
        for p in self.publications:
            for a in p.authors:
                astats[a][p.pub_type] += 1

        data = [ [self.authors[i].name] + astats[i] + [sum(astats[i])]
            for i in range(len(astats)) ]
        return (header, data)

    def get_average_authors_per_publication_by_year(self, av):
        header = ("Year", "Conference papers",
            "Journals", "Books",
            "Book chapers", "All publications")

        ystats = {}
        for p in self.publications:
            try:
                ystats[p.year][p.pub_type].append(len(p.authors))
            except KeyError:
                ystats[p.year] = [[], [], [], []]
                ystats[p.year][p.pub_type].append(len(p.authors))

        func = Stat.FUNC[av]

        data = [ [y]
            + [ func(L) for L in ystats[y] ]
            + [ func(list(itertools.chain(*ystats[y]))) ]
            for y in ystats ]
        return (header, data)

    def get_publications_by_year(self):
        header = ("Year", "Number of conference papers",
            "Number of journals", "Number of books",
            "Number of book chapers", "Total")

        ystats = {}
        for p in self.publications:
            try:
                ystats[p.year][p.pub_type] += 1
            except KeyError:
                ystats[p.year] = [0, 0, 0, 0]
                ystats[p.year][p.pub_type] += 1

        data = [ [y] + ystats[y] + [sum(ystats[y])] for y in ystats ]
        return (header, data)

    def get_average_publications_per_author_by_year(self, av):
        header = ("Year", "Conference papers",
            "Journals", "Books",
            "Book chapers", "All publications")

        ystats = {}
        for p in self.publications:
            try:
                s = ystats[p.year]
            except KeyError:
                s = np.zeros((len(self.authors), 4))
                ystats[p.year] = s
            for a in p.authors:
                s[a][p.pub_type] += 1

        func = Stat.FUNC[av]

        data = [ [y]
            + [ func(ystats[y][:, i]) for i in np.arange(4) ]
            + [ func(ystats[y].sum(axis=1)) ]
            for y in ystats ]
        return (header, data)

    def get_author_totals_by_year(self):
        header = ("Year", "Number of conference papers",
            "Number of journals", "Number of books",
            "Number of book chapers", "Total")

        ystats = {}
        for p in self.publications:
            try:
                s = ystats[p.year][p.pub_type]
            except KeyError:
                ystats[p.year] = [set(), set(), set(), set()]
                s = ystats[p.year][p.pub_type]
            for a in p.authors:
                s.add(a)
        data = [ [y] + [len(s) for s in ystats[y]] + [len(ystats[y][0] | ystats[y][1] | ystats[y][2] | ystats[y][3])]
            for y in ystats ]
        return (header, data)

    def add_publication(self, pub_type, title, year, authors):
        if year == None or len(authors) == 0:
            print "Warning: excluding publication due to missing information"
            print "    Publication type:", PublicationType[pub_type]
            print "    Title:", title
            print "    Year:", year
            print "    Authors:", ",".join(authors)
            return
        if title == None:
            print "Warning: adding publication with missing title [ %s %s (%s) ]" % (PublicationType[pub_type], year, ",".join(authors))
        idlist = []
        for a in authors:
            try:
                idlist.append(self.author_idx[a])
            except KeyError:
                a_id = len(self.authors)
                self.author_idx[a] = a_id
                idlist.append(a_id)
                self.authors.append(Author(a))
        self.publications.append(
            Publication(pub_type, title, year, idlist))
        if (len(self.publications) % 100000) == 0:
            print "Adding publication number %d (number of authors is %d)" % (len(self.publications), len(self.authors))

        if self.min_year == None or year < self.min_year:
            self.min_year = year
        if self.max_year == None or year > self.max_year:
            self.max_year = year

    def _get_collaborations(self, author_id, include_self):
        data = {}
        for p in self.publications:
            if author_id in p.authors:
                for a in p.authors:
                    try:
                        data[a] += 1
                    except KeyError:
                        data[a] = 1
        if not include_self:
            del data[author_id]
        return data

    def get_coauthor_details(self, name):
        author_id = self.author_idx[name]
        data = self._get_collaborations(author_id, True)
        return [ (self.authors[key].name, data[key])
            for key in data ]

    def get_network_data(self):
        na = len(self.authors)

        nodes = [ [self.authors[i].name, -1] for i in range(na) ]
        links = set()
        for a in range(na):
            collab = self._get_collaborations(a, False)
            nodes[a][1] = len(collab)
            for a2 in collab:
                if a < a2:
                    links.add((a, a2))
        return (nodes, links)
    
    def _get_collaborations_d(self, author_id, include_self):
        data = {}
        for p in self.publications:
            if author_id in p.authors:
                for a in p.authors:
                    try:
                        data[self.authors[a].name] = 1
                    except KeyError:
                        data[a] = 1
        if not include_self:
            del data[self.authors[author_id].name]
        return data
    
    def get_graph_d(self):
        graph = {}
        authors = self.get_all_authors()
        for author in authors:
            author_id = self.author_idx[author]
            data = self._get_collaborations_d(author_id, True)
            graph[author] = data
        return graph

    def dijkstra(self, s, t):
        # sanity check
        if s == t:
            #return "The start and terminal nodes are the same. Minimum distance is 0."
            return ([s])
        net = self.get_graph_d()
        if net.has_key(s)==False:
            #return "There is no start node called " + str(s) + "."
            return ("F")
        if net.has_key(t)==False:
            #return "There is no terminal node called " + str(t) + "."
            return ("F")
        # create a labels dictionary
        labels={}
        # record whether a label was updated
        order={}
        # populate an initial labels dictionary
        for i in net.keys():
            if i == s: labels[i] = 0 # shortest distance form s to s is 0
            else: labels[i] = float("inf") # initial labels are infinity
        from copy import copy
        drop1 = copy(labels) # used for looping
        
        ## begin algorithm
        while len(drop1) > 0:
            # find the key with the lowest label
            minNode = min(drop1, key = drop1.get) #minNode is the node with the smallest label
            # update labels for nodes that are connected to minNode
            for i in net[minNode]:
                if labels[i] > (labels[minNode] + net[minNode][i]):
                    labels[i] = labels[minNode] + net[minNode][i]
                    drop1[i] = labels[minNode] + net[minNode][i]
                    order[i] = minNode
            del drop1[minNode] # once a node has been visited, it's excluded from drop1

        ## end algorithm
        # print shortest path
        temp = copy(t)
        rpath = []
        path = []
        while 1:
            rpath.append(temp)
            if order.has_key(temp): temp = order[temp]
            #else: return "There is no path from " + str(s) + " to " + str(t) + "."
            else: return ("X")
            if temp == s:
                rpath.append(temp)
                break
        for j in range(len(rpath)-1,-1,-1):
            path.append(rpath[j])
        #return "The shortest path from " + s + " to " + t + " is " + str(path) + ".
        return (path)

    def degree_of_separation(self,start,end):
        
        if start == "" or end == "":
            return (-1)
        
        #path = self.BFS(start,end)
        path = self.dijkstra(start, end)
        
        if len(path) == 1:
            if start in path:
                return ("0")
            elif "X" in path:
                return ("X")
            elif "F" in path:
                return ("F")
            
        return ([len(path)-2])
    
    def separation_path(self,start,end):
        
        if start == "" or end == "":
            return (-1)
        
        #path = self.BFS(start,end)
        path = self.dijkstra(start, end)
        
        if len(path) == 1:
            if start in path:
                return ("0")
            elif "X" in path:
                return ("X")
            elif "F" in path:
                return ("F")
            
        return path

    def get_author_publication_number(self, authorname):
        headers = "Publications"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                try:
                    data[self.author_idx[authorname]] += 1
                except KeyError:
                    data[self.author_idx[authorname]] = 1
        
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_publications(self, authorname):
        headers = ("Conference Papers", "Journals", "Books", "Book Chapters", "Overall")
        
        data = [0,0,0,0,0]
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                data[4] += 1
                data[p.pub_type] += 1

        return (headers, [data])
        
    def get_author_conference_number(self, authorname):
        headers = "Conference Papers"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if p.pub_type == 0:
                    try:
                        data[self.author_idx[authorname]] += 1
                    except KeyError:
                        data[self.author_idx[authorname]] = 1
        
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_journal_number(self, authorname):
        headers = "Journals"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if p.pub_type == 1:
                    try:
                        data[self.author_idx[authorname]] += 1
                    except KeyError:
                        data[self.author_idx[authorname]] = 1
        
        return (headers, data[self.author_idx[authorname]])
       
    def get_author_bookchapter_number(self, authorname):
        headers = "Book Chapters"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if p.pub_type == 3:
                    try:
                        data[self.author_idx[authorname]] += 1
                    except KeyError:
                        data[self.author_idx[authorname]] = 1
        
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_book_number(self, authorname):
        headers = "Books"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if p.pub_type == 2:
                    try:
                        data[self.author_idx[authorname]] += 1
                    except KeyError:
                        data[self.author_idx[authorname]] = 1
        
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_coauthor_number(self, authorname):
        headers = "Co-authors"
        
        data = {}
        data = self.get_coauthor_details(authorname)
        
        count = 0
        for author in data:
            if author[0] != authorname:
                count += 1
            
        return (headers, count)
    
    
    def get_author_first_on_paper_number(self, authorname):
        headers = "First on paper"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if len(p.authors) != 1:
                    if p.authors[0] == self.author_idx[authorname]:
                        try: 
                            data[self.author_idx[authorname]] += 1
                        except KeyError:
                            data[self.author_idx[authorname]] = 1
#
# This may need putting back in if we are to count second author entries as first
#
#                if p.authors[len(p.authors) - 1] != self.author_idx[authorname]:
#                    try: 
#                        data[self.author_idx[authorname]] += 1
#                    except KeyError:
#                        data[self.author_idx[authorname]] = 1
                
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_first_place(self, authorname):
        headers = ("Conference Papers", "Journals", "Books", "Book Chapters", "Overall")
        
        data = [0,0,0,0,0]
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if len(p.authors) != 1:
                    if p.authors[0] == self.author_idx[authorname]:
                        data[4] += 1
                        data[p.pub_type] += 1

        return (headers, [data])    
    
    def get_author_last_on_paper_number(self, authorname):
        headers = "Last on Paper"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if len(p.authors) != 1:
                    if p.authors[len(p.authors) - 1] == self.author_idx[authorname]:
                        try: 
                            data[self.author_idx[authorname]] += 1
                        except KeyError:
                            data[self.author_idx[authorname]] = 1
                            
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_last_place(self, authorname):
        headers = ("Conference Papers", "Journals", "Books", "Book Chapters", "Overall")
        
        data = [0,0,0,0,0]
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if len(p.authors) != 1:
                    if p.authors[len(p.authors) - 1] == self.author_idx[authorname]:
                        data[4] += 1
                        data[p.pub_type] += 1

        return (headers, [data])  
    
    def get_author_sole_on_paper_number(self, authorname):
        headers = "Sole Author"
        
        data = {}
        data[self.author_idx[authorname]] = 0
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if len(p.authors) == 1:
                    try: 
                        data[self.author_idx[authorname]] += 1
                    except KeyError:
                        data[self.author_idx[authorname]] = 1
                        
        return (headers, data[self.author_idx[authorname]])
    
    def get_author_sole_place(self, authorname):
        headers = ("Conference Papers", "Journals", "Books", "Book Chapters", "Overall")
        
        data = [0,0,0,0,0]
        
        for p in self.publications:
            if self.author_idx[authorname] in p.authors:
                if len(p.authors) == 1:
                    data[4] += 1
                    data[p.pub_type] += 1

        return (headers, [data])  
      
    def search_authors(self, searchname):
        header = ("Names")
        
        if searchname == "":
            return ([],[])

        pattern = "^"+searchname

        surnames = []
        forenames = []
        names = []
        count = 0
        
        for au in self.get_all_authors():
            flag = 0
            
            if searchname.lower() in au.lower():
                flag = 1
            
            nameArray = str(au).split(" ")        
            if len(nameArray) > 1:                      
                # The name is the first item in the list 
                name = nameArray[0]
                # Position of surname is the last item in the list
                surnamePos = len(nameArray) - 1
                # Get surname
                surname = nameArray[surnamePos] 

            if re.search("^"+searchname+"$", au, re.IGNORECASE):
                surnames.append([au])
                count += 1
                flag = 0
            else:
                if re.search(pattern, surname, re.IGNORECASE):
                    surnames.append([au])
                    count += 1
                    flag = 0  
                
                if re.search(pattern, name, re.IGNORECASE):
                    forenames.append([au])
                    count += 1
                    flag = 0  

            if flag == 1:
                names.append([au])
                
        if count == 0:
            return ([],[])
        
        data = []
        
        sort = sorter.Sorter()
        
        sortednames = sort.sort_asc(surnames, 0)
        
        for n in sortednames:
            data.append(n)
            
        sortednames = sorted(forenames, key=lambda tup: tup[0])
        
        for n in sortednames:
            data.append(n)

        sortednames = sorted(names, key=lambda tup: tup[0])
        
        for n in sortednames:
            data.append(n)
        
        return (header,data)
    
    def get_author_details(self, authorname):
        if authorname == "":
            return ([],[])

        names = []
        count = 0
        
        for au in self.get_all_authors():          
            if authorname.lower() in au.lower():
                count += 1
                names.append(au)
                
        if count == 0:
            return ([],[])
        
        data = []       
        for authorn in names:
            da = []
            da.append(self.get_author_publication_number(authorn))
            da.append(self.get_author_conference_number(authorn))
            da.append(self.get_author_journal_number(authorn))
            da.append(self.get_author_bookchapter_number(authorn))
            da.append(self.get_author_book_number(authorn))
            da.append(self.get_author_coauthor_number(authorn))
            da.append(self.get_author_first_on_paper_number(authorn))
            da.append(self.get_author_last_on_paper_number(authorn))
            da.append(self.get_author_sole_on_paper_number(authorn)) 
                    
            data.append([authorn, da[0][1],da[1][1], da[2][1], da[3][1], da[4][1], da[5][1], da[6][1], da[7][1], da[8][1] ])
        
        header = ("Name", da[0][0],da[1][0], da[2][0], da[3][0], da[4][0], da[5][0], da[6][0], da[7][0], da[8][0])
        
        return (header,data)
        
class DocumentHandler(handler.ContentHandler):
    TITLE_TAGS = [ "sub", "sup", "i", "tt", "ref" ]
    PUB_TYPE = {
        "inproceedings":Publication.CONFERENCE_PAPER,
        "article":Publication.JOURNAL,
        "book":Publication.BOOK,
        "incollection":Publication.BOOK_CHAPTER }

    def __init__(self, db):
        self.tag = None
        self.chrs = ""
        self.clearData()
        self.db = db

    def clearData(self):
        self.pub_type = None
        self.authors = []
        self.year = None
        self.title = None

    def startDocument(self):
        pass

    def endDocument(self):
        pass

    def startElement(self, name, attrs):
        if name in self.TITLE_TAGS:
            return
        if name in DocumentHandler.PUB_TYPE.keys():
            self.pub_type = DocumentHandler.PUB_TYPE[name]
        self.tag = name
        self.chrs = ""

    def endElement(self, name):
        if self.pub_type == None:
            return
        if name in self.TITLE_TAGS:
            return
        d = self.chrs.strip()
        if self.tag == "author":
            self.authors.append(d)
        elif self.tag == "title":
            self.title = d
        elif self.tag == "year":
            self.year = int(d)
        elif name in DocumentHandler.PUB_TYPE.keys():
            self.db.add_publication(
                self.pub_type,
                self.title,
                self.year,
                self.authors)
            self.clearData()
        self.tag = None
        self.chrs = ""

    def characters(self, chrs):
        if self.pub_type != None:
            self.chrs += chrs