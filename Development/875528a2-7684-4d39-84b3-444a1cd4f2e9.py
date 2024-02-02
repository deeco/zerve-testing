'1972' in raw_year_list
[year for year in raw_year_list if not year.isnumeric()]
year_list = [year for year in raw_year_list if year.isnumeric()]
','.join(year_list)
import collections
year_freq = collections.Counter(year_list)
for year in sorted(year_freq.keys()):
    print (year)+': '+('+'*year_freq[year])