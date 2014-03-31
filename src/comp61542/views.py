from comp61542 import app, sorter
from database import database
from flask import (render_template, request)

def format_data(data):
    fmt = "%.2f"
    result = []
    for item in data:
        if type(item) is list:
            result.append(", ".join([ (fmt % i).rstrip('0').rstrip('.') for i in item ]))
        else:
            result.append((fmt % item).rstrip('0').rstrip('.'))
    return result

@app.route("/averages")
def showAverages():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":"averages"}
    args['title'] = "Averaged Data"
    tables = []
    headers = ["Average", "Conference Paper", "Journal", "Book", "Book Chapter", "All Publications"]
    averages = [ database.Stat.MEAN, database.Stat.MEDIAN, database.Stat.MODE ]
    tables.append({
        "id":1,
        "title":"Average Authors per Publication",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_authors_per_publication(i)[1])
                for i in averages ] })
    tables.append({
        "id":2,
        "title":"Average Publications per Author",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_publications_per_author(i)[1])
                for i in averages ] })
    tables.append({
        "id":3,
        "title":"Average Publications in a Year",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_publications_in_a_year(i)[1])
                for i in averages ] })
    tables.append({
        "id":4,
        "title":"Average Authors in a Year",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_authors_in_a_year(i)[1])
                for i in averages ] })

    args['tables'] = tables
    return render_template("averages.html", args=args)

@app.route("/coauthors")
def showCoAuthors():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    PUB_TYPES = ["Conference Papers", "Journals", "Books", "Book Chapters", "All Publications"]
    args = {"dataset":dataset, "id":"coauthors"}
    args["title"] = "Co-Authors"

    start_year = db.min_year
    if "start_year" in request.args:
        start_year = int(request.args.get("start_year"))

    end_year = db.max_year
    if "end_year" in request.args:
        end_year = int(request.args.get("end_year"))

    pub_type = 4
    if "pub_type" in request.args:
        pub_type = int(request.args.get("pub_type"))

    args["data"] = db.get_coauthor_data(start_year, end_year, pub_type)
    args["start_year"] = start_year
    args["end_year"] = end_year
    args["pub_type"] = pub_type
    args["min_year"] = db.min_year
    args["max_year"] = db.max_year
    args["start_year"] = start_year
    args["end_year"] = end_year
    args["pub_str"] = PUB_TYPES[pub_type]
    return render_template("coauthors.html", args=args)

@app.route("/")
def showStatisticsMenu():
    dataset = app.config['DATASET']
    args = {"dataset":dataset}
    return render_template('statistics.html', args=args)

@app.route("/statisticsdetails/<status>")
def showPublicationSummary(status):
#     print status
    
    strings = status.split("+")
    status = strings[0]
    index = int(strings[1])
    sortBool  = strings[2]
    
    if sortBool == "false":
        isDesc = False
    elif sortBool == "true":
        isDesc = True
    
#     print status
#     print index

    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":status}

    if (status == "publication_summary"):
        args["title"] = "Publication Summary"
        data = db.get_publication_summary()
#         args["data"] = db.get_publication_summary()

    if (status == "publication_author"):
        args["title"] = "Author Publication"
        data = db.get_publications_by_author()     
#         args["data"] = data

    if (status == "publication_year"):
        args["title"] = "Publication by Year"
        data = db.get_publications_by_year()

    if (status == "author_year"):
        args["title"] = "Author by Year"
        
        sort = sorter.Sorter()
        data = db.get_author_totals_by_year()   
        
#         args["data"] = db.get_author_totals_by_year()

    sort = sorter.Sorter()
    if isDesc:
        sortedData = sort.sort_desc(data[1], index )
    else:
        sortedData = sort.sort_asc(data[1], index )
    args["data"] = (data[0],sortedData)
        
    args["sort_index"] = index
    args["sortBool"] = isDesc
    
    return render_template('statistics_details.html', args=args)

@app.route("/search/<status>")
def showSearch(status):
    
    strings = status.split("+")
    status = strings[0]
    index = int(strings[1])
    sortBool  = strings[2]
    
    if sortBool == "false":
        isDesc = False
    elif sortBool == "true":
        isDesc = True
    
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":"search"}
    args["title"] = "Search"
    
    author=""
    if "author" in request.args:
        author = request.args.get("author")
    
    sort = sorter.Sorter()
    if isDesc:
        sortedData = sort.sort_desc(db.search_authors(author)[1], index )
    else:
        sortedData = sort.sort_asc(db.search_authors(author)[1], index )
    args["data"] = (db.search_authors(author)[0],sortedData)
        
    args["sort_index"] = index
    args["sortBool"] = isDesc
    args["author"] = author
    
    return render_template('search.html', args=args)

@app.route("/show_author")
def showAuthor():
    
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":"show_author"}

    author = "xesto"
    if "author" in request.args:
        author = request.args.get("author")
    args["title"] = "Author Details for " + author
    
    args["data"] = (db.get_author_publications(author))
        
    args["author"] = author
    
    
    tables = []
    headers = ["Conference Paper", "Journal", "Book", "Book Chapter", "All Publications"]
    tables.append({
        "id":1,
        "title":"Number of Publications",
        "header":headers,
        "rows":db.get_author_publications(author)[1]})
    tables.append({
        "id":2,
        "title":"Number of times First Author",
        "header":headers,
        "rows":db.get_author_first_place(author)[1]})
    tables.append({
        "id":3,
        "title":"Number of times Last Author",
        "header":headers,
        "rows":db.get_author_last_place(author)[1]})
    tables.append({
        "id":4,
        "title":"Number of times Sole Author",
        "header":headers,
        "rows":db.get_author_sole_place(author)[1]})


    args['tables'] = tables
    
    
    
    
    return render_template('show_author.html', args=args)