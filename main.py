def book_list_view(library):
    if library == {}:
        result = 'Пока нет данных.'
    else:
        result = library.keys()
    print(result)


library = {'Harry Potter 1' : {'author' : 'Rowling J.', 'year' : '1997', 'is_available' : 'yes'},
           'Harry Potter 2' : {'author' : 'Rowling J.', 'year' : '1998', 'is_available' : 'yes'},
           'Harry Potter 3' : {'author' : 'Rowling J.', 'year' : '1999', 'is_available' : 'no'},
           'Harry Potter 4' : {'author' : 'Rowling J.', 'year' : '2000', 'is_available' : 'yes'},
           'Harry Potter 5' : {'author' : 'Rowling J.', 'year' : '2003', 'is_available' : 'no'},
           'Harry Potter 6' : {'author' : 'Rowling J.', 'year' : '2005', 'is_available' : 'no'},
           'Harry Potter 7' : {'author' : 'Rowling J.', 'year' : '2007', 'is_available' : 'yes'}
           }


book_list_view(library)