# testing 2
webpage.title.text
len(webpage.find_all('a'))
len(webpage.select('div.filmo-row span.year_column'))
raw_year_list = [e.text.strip() for e in webpage.select('div.filmo-row span.year_column')]
