# Tuple

```
   _
 _( )_
o,,,,,o
   :
 _/ \_
```
 
> AKA:

    Record, Structure

> KNOWN FOR:

    Packing and unpacking values. A row in a database

> BASIC USAGE:

    record = (val1, val2, val3)
    a, b, c = record
    val = record[n]

> ACCOMPLICE:

    collections.namedtuple

```py
>>> row = ('Dave', 'Beazley', '5412 N CLARK ST')
>>> row[1]
'Beazley'
>>> row[2]
'5412 N CLARK ST'
```
## prevent hard code indices with namedtuple
```py
>>> from collections import namedtuple
>>> Person = namedtuple('Person', ['first', 'last', 'address'])
>>> row = Person('Dave', 'Beazley', '5412 N CLARK ST')
>>> row.first
'Dave'
>>> row.last
'Beazley'
```

# List
```
   _
  [ ]  /
o--|--/
   :
 _/ \_
```
> AKA:
    
    Mutable Sequence, Array

> KNOWN FOR:
    
    Enforcing order.

> BASIC USAGE:
    
    items = [ val1, val2, ..., valn ]
    x = items[n]
    items[n] = x
    del items[n]
    items.append(value)
    items.sort()

# Set
```
   {}  _
    \_(_)
,_____/ \
,__/    /
```
> AKA:

    Set

> KNOWN FOR:
    
    Uniqueness, membership tests

> BASIC USAGE:
    
    s = { val1, val2, ..., valn {
    s.add(val)
    s.remove(val)
    val in s

```py
>>> names = ['Dave', 'Thomas', 'Paula', 'Lewis', 'Dave']
>>> names
['Dave', 'Thomas', 'Paula', 'Lewis', 'Dave']
>>> names = {'Dave', 'Thomas', 'Paula', 'Lewis', 'Dave'}
>>> names
{'Thomas', 'Dave', 'Lewis', 'Paula'}
```

# Dict
```
   v
  { }
`__M__~  {:}
 _/"\
'   |_
```

> AKA:

    Mapping, Associative Array

> KNOWN FOR:

    Lookup tables, indices

> BASIC USAGE:

    d = { key1: val1, key2: val2, key3: val3 }
    val = d[key]
    d[key] = val
    del d[key]
    key in d

> MERGE TWO DICTS

    { **dict1, **dict2 }

```py
>>> prices = {
...     'ACME': 94.23,
...     'YOW': 45.2
... }
>>> prices['ACME']
94.23
>>> 
>>> from collections import Counter, defaultdict
```

# Counter
```
    _
  \(_)
   \/---
_/\/
  /
  \
  ` 
```
> AKA:

    collections.Counter

> KNOWN FOR:
    
    Counting, histograms, tabulation

> BASIC USAGE:
    
    c = Counter(sequence)
    c[key] += n
    c.most_common(n)

```py
>>> c = Counter('xyzzy')
>>> c
Counter({'y': 2, 'z': 2, 'x': 1})
>>> c['a'] += 10
>>> c['b'] += 13
>>> c
Counter({'b': 13, 'a': 10, 'y': 2, 'z': 2, 'x': 1})
```

# defaultdict
```
_  /
 \_\
   _\
  /{_}\
 /  ^  \
```
> AKA:
    
    collections.defaultdict

> KNOWN FOR:

    Multidicts, one-many relationships, grouping

> BASIC USAGE:

    d = defaultdict(list)
    d[key].append(val)
    values = d[key]

    d = defaultdict(set)
    d[key].add(val)
    unique_values = d[key]

```py
>>> d = defaultdict(list)
>>> d['spam'].append(42)
>>> d['blah'].append(13)
>>> d['spam'].append(10)
>>> d
defaultdict(<class 'list'>, {'spam': [42, 10], 'blah': [13]})
```

# Basic Powers
> ITERATION:
    
    for item in container:
        ...

> VARIANTS:

    for n, item in enumerate(container):
        ...

    for item1, item2, in zip(container1, container2):
        ...

> REDUCTIONS:

    sum(container)
    min(container)
    max(container)
    any(container)
    all(container)

# Superpowers

> LIST COMPREHENSION:

    [ expression for x in iterable if condition ]

> SET COMPREHENSION:

    { expression for x in iterable if condition }

> DICT COMPREHENSION:

    { key: val for key, val in iterable if condition }


```py
>>> nums = [1,2,3,4,5,6]
>>> squares = []
>>> for x in nums:
...     squares.append(x*x)
... 
>>> squares
[1, 4, 9, 16, 25, 36]
>>> squares = [ x*x for x in nums ]
```

# Iterpowers

> GEN COMPREHENSION:

    ( expression for x in iterable if condition )

> COMBINED WITH REDUCTION:

    sum( expression for x in iterable if condition )

> PROTIP:

    Generator experssions allow you to process huge amounts
    of data incrementally--saving a ton of memory.

```py
>>> nums
[1, 2, 3, 4, 5, 6]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x7f4d707d3e60>
>>> for n in squares:
...     print(n)
... 
1
4
9
16
25
36
```

# yield

> list function

    def f(data):
        r = []
        for i in data:
            ...
            r.append(i)
        return r

> generator function

    def f(data):
        for i in data:
            ...
            yield i


# Let's Play!
## City of Chicago Food Inspections
    
    https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5

    A 157MB CSV file with about 130000 rows of data.

# Import the file from csv to list
```py
>>> import csv
>>> food = list(csv.DictReader(open('Food_Inspections.csv')))
>>> len(food)
206966
```

# View the elements
```py
>>> from pprint import pprint
>>> food[0]
OrderedDict([('Inspection ID', '2373731'),
             ('DBA Name', 'IRVING PARK EARLY LEARNING CNT'),
             ('AKA Name', 'IRVING PARK EARLY LEARNING CNT'),
             ('License #', '2215634'),
             ('Facility Type', "Children's Services Facility"),
             ('Risk', 'Risk 1 (High)'),
             ('Address', '3021-3023 W MONTROSE AVE '),
             ('City', 'CHICAGO'),
             ('State', 'IL'),
             ('Zip', '60618'),
             ('Inspection Date', '06/15/2020'),
             ('Inspection Type', 'License'),
             ('Results', 'Pass'),
             ('Violations',
              '49. NON-FOOD/FOOD CONTACT SURFACES CLEAN - Comments: RAW WOODEN '
              'SHELVING IN THE DRY FOOD STORAGE/REFRIGERATION ROOM MUST BE '
              'PAINTED/SEALED TO BE SMOOTH AND CLEANABLE.'),
             ('Latitude', '41.96110410411044'),
             ('Longitude', '-87.70433833416415'),
             ('Location', '(-87.70433833416415, 41.96110410411044)')])
```

# What are all the available results
> ('Results', 'Pass'),

```py
>>> { row['Results'] for row in food }
{'Business Not Located',
 'Fail',
 'No Entry',
 'Not Ready',
 'Out of Business',
 'Pass',
 'Pass w/ Conditions'}
```

# Who failed their food inspections
```py
>>> fail = [ row for row in food if row['Results'] == 'Fail' ]
>>> len(fail)
40019
>>> fail[5]
OrderedDict([('Inspection ID', '2371204'),
             ('DBA Name', 'BABAS STEAK AND LEMONADE'),
             ('AKA Name', ''),
             ('License #', '0'),
             ('Facility Type', 'Restaurant'),
             ('Risk', 'Risk 2 (Medium)'),
             ('Address', '3407 1/2 W MADISON ST '),
             ('City', 'CHICAGO'),
             ('State', 'IL'),
             ('Zip', '60624'),
             ('Inspection Date', '05/28/2020'),
             ('Inspection Type', 'Canvass Re-Inspection'),
             ('Results', 'Fail'),
             ('Violations',
              '38. INSECTS, RODENTS, & ANIMALS NOT PRESENT - Comments: '
              'OBSERVED EVIDENCE OF PEST ACTIVITY ON PREMISE DURING TIME OF '
              'INSPECTION IN THE FOLLOWING AREAS.. APPROXIMATELY 25 SMALL '
              'RODENT DROPPINGS ON FLOOR AROUND TOILET AND SCATTERED ALONG '
              'WALL AS WELL AS 15 IN FRONT PREP AREA ALONG SIDE OF HEAVY GRILL '
              'EQUIPMENT ON FLOOR. INSTRUCTED TO CONTACT PEST CONTROL FOR '
              'SERVICE PRIOR TO RE-INSPECTION AND CLEAN AND SANITIZE EFFECTED '
              'AREAS. MUST ELIMINATE PEST ACTIVITY. PRIORITY FOUNDATION '
              'VIOLATION. 7-38-020 (A). NO CITATION ISSUED. | 40. PERSONAL '
              'CLEANLINESS - Comments: OBSERVED FOOD HANDLER HANDLING FOOD '
              'WITHOUT HAIR RESTRAINT. INSTRUCTED TO PROVIDE AND MAINTAIN. | '
              '47. FOOD & NON-FOOD CONTACT SURFACES CLEANABLE, PROPERLY '
              'DESIGNED, CONSTRUCTED & USED - Comments: OBSERVED TORN RUBBER '
              'GASKETS ON 2 DOOR REFRIGERATION UNIT IN FRONT PREP AREA. MUST '
              'MAINTAIN IN GOOD REPAIR AND TEMPERATURE CONTROL. | 57. ALL FOOD '
              'EMPLOYEES HAVE FOOD HANDLER TRAINING - Comments: OBSERVED NO '
              'FOOD HANDLER TRAINING CERTIFICATES ON SITE FOR REVIEW. '
              'INSTRUCTED TO PROVIDE AS REQUIRED.'),
             ('Latitude', '41.8808046152'),
             ('Longitude', '-87.71137549591673'),
             ('Location', '(-87.71137549591673, 41.8808046152)')])
>>> 
``` 

# What is the worst place to eat in Chicago
```py
>>> worst = Counter(row['DBA Name'] for row in fail)
>>> len(worst)
16111
```

# Top worst places
```py
>>> worst.most_common(25)
[('SUBWAY', 361),
 ('DUNKIN DONUTS', 220),
 ("MCDONALD'S", 114),
 ('7-ELEVEN', 65),
 ('MCDONALDS', 60),
 ('POTBELLY SANDWICH WORKS LLC', 55),
 ('CITGO', 53),
 ('CHIPOTLE MEXICAN GRILL', 48),
 ("HAROLD'S CHICKEN SHACK", 47),
 ('DUNKIN DONUTS/BASKIN ROBBINS', 45),
 ('LAS ISLAS MARIAS', 44),
 ('POTBELLY SANDWICH WORKS', 39),
 ("PAPA JOHN'S PIZZA", 37),
 ('FRESHII', 36),
 ('JIMMY JOHNS', 36),
 ('CORNER BAKERY CAFE', 33),
 ("DOMINO'S PIZZA", 33),
 ('KFC', 32),
 ('DUNKIN DONUTS / BASKIN ROBBINS', 31),
 ('POPEYES', 30),
 ('AU BON PAIN', 30),
 ("McDONALD'S", 30),
 ('SHARKS FISH & CHICKEN', 29),
 ('SUBWAY SANDWICHES', 29),
 ('KENTUCKY FRIED CHICKEN', 29)]
```

# What is correct spelling for Mc Donalds?

## uppercase all DBA Name and remove the single string(') with empty string
```py
>>> fail = [ { **row, 'DBA Name': row['DBA Name'].replace("'", '').upper() } for row in fail ]
>>> worst = Counter(row['DBA Name'] for row in fail)
>>> worst.most_common(25)
[('SUBWAY', 389),
 ('DUNKIN DONUTS', 238),
 ('MCDONALDS', 226),
 ('7-ELEVEN', 73),
 ('CHIPOTLE MEXICAN GRILL', 69),
 ('JIMMY JOHNS', 66),
 ('POTBELLY SANDWICH WORKS LLC', 55),
 ('CITGO', 53),
 ('HAROLDS CHICKEN SHACK', 48),
 ('DUNKIN DONUTS/BASKIN ROBBINS', 46),
 ('LAS ISLAS MARIAS', 44),
 ('PAPA JOHNS PIZZA', 43),
 ('SUBWAY SANDWICHES', 40),
 ('POTBELLY SANDWICH WORKS', 39),
 ('POPEYES', 38),
 ('MC DONALDS', 36),
 ('FRESHII', 36),
 ('DOMINOS PIZZA', 34),
 ('CORNER BAKERY CAFE', 33),
 ('AU BON PAIN', 33),
 ('WHOLE FOODS MARKET', 32),
 ('KFC', 32),
 ('SHARKS FISH & CHICKEN', 31),
 ('DUNKIN DONUTS / BASKIN ROBBINS', 31),
 ('KENTUCKY FRIED CHICKEN', 30)]
```

# Worst street address to go in Chicago for food
```py
>>> bad = Counter(row['Address'] for row in fail)
>>> bad.most_common(5)
[('11601 W TOUHY AVE ', 346),
 ('2300 S THROOP ST ', 107),
 ('324 N LEAVITT ST ', 88),
 ('500 W MADISON ST ', 82),
 ('5700 S CICERO AVE ', 64)]
```

# Tabulate the worst addresses by year
```py
>>> fail[0]['Inspection Date']
'06/11/2020'
>>> fail[0]['Inspection Date'][-4:]
'2020'
>>> fail[0]['Address']
'1352 W TAYLOR ST '
>>> [fail[0]['Inspection Date'][-4:]]
['2020']
>>> [fail[0]['Address']]
['1352 W TAYLOR ST ']
>>> by_year_test = defaultdict(Counter)
>>> by_year_test['2020']['1352 W TAYLOR ST ']
0
>>> by_year_test['2020']['1352 W TAYLOR ST '] += 1
>>> by_year_test['2020']['1352 W TAYLOR ST ']
1
>>> by_year_test['2020']
Counter({'1352 W TAYLOR ST ': 1})
>>>
>>> by_year = defaultdict(Counter)
>>> for row in fail:
...     by_year[row['Inspection Date'][-4:]][row['Address']] += 1
...
>>> by_year['2015'].most_common(5)
[('11601 W TOUHY AVE ', 39),
 ('500 W MADISON ST ', 13),
 ('324 N LEAVITT ST ', 9),
 ('307 S KEDZIE AVE ', 9),
 ('12 S MICHIGAN AVE ', 8)]
>>> by_year['2014'].most_common(5)
[('11601 W TOUHY AVE ', 32),
 ('500 W MADISON ST ', 17),
 ('324 N LEAVITT ST ', 15),
 ('113-125 N GREEN ST ', 12),
 ('131 N CLINTON ST ', 10)]
>>> by_year['2013'].most_common(5)
[('11601 W TOUHY AVE ', 37),
 ('2300 S THROOP ST ', 10),
 ('700 E GRAND AVE ', 10),
 ('301 E NORTH WATER ST ', 9),
 ('12760 S HALSTED ST ', 8)]
```

# Chicago Ohare Airport
```py
>>> bad.most_common(5)[0][0]
'11601 W TOUHY AVE '
```
![](./airport.png)

# All the fail restaurants in ohare airport
```py
>>> bad.most_common(5)[0]
('11601 W TOUHY AVE ', 346)
>>> ohare = [row for row in fail if row['Address'].startswith('11601 W TOUHY')]
>>> len(ohare)
347
>>> { row['Address'] for row in ohare }
{'11601 W TOUHY AVE T2 F12', '11601 W TOUHY AVE '}
```

# What are the businesses that are failing
```py
>>> { row['DBA Name'] for row in ohare }
{'7-ELEVEN #39913A',
 'AIR FRANCE',
 'AMERICAN AIRLINES',
 'AMERICAN AIRLINES ADMIRALS LOUNGE',
 'AMERICAS DOG',
 'ANDIAMOS OHARE, LLC',
 'ARAMARK AT UNITED AIRLINES',
 'ARGO TEA',
 'ARGO TEA CAFE-OHARE T2',
 'AUNTIE ANNES',
 'AUNTIE ANNES PRETZELS',
 'B JS  MARKET',
 'BERGHOFF CAFE',
 'BIG BOWL',
 'BRITISH AIRWAYS',
 'BURRITO BEACH',
 'CAFFE  MERCATO',
 'CHICAGO BLACKHAWKS STANLEYS T2 BAR',
 'CHICAGO NEWS & GIFTS',
 'CHILIS T - 3',
 'CHILIS T-I',
 'CHILIS- G CONCOURSE',
 'CNN',
 'DELI/STARBUCKS',
 'DELTA SKY CLUB',
 'DUNKIN DONUTS',
 'EFIES CANTEEN INC',
 'ELIS CHEESECAKE',
 'FARMERS FRIDGE',
 'FRESH ON THE FLY',
 'FRONTERA TORTAS  BY RICK BAYLESS GATE K4 T3',
 'FRONTERA TORTAS BY RICK  BAYLESS',
 'GALILEO BAR',
 'GARRETT POPCORN SHOPS',
 'GATEGOURMET',
 'GOLD COAST DOGS',
 'GOOSE ISLAND',
 'GREEN MARKET',
 'HILTON OHARE',
 'HOST INTERNATIONAL B05',
 'HOST INTERNATIONAL INC',
 'HOST INTERNATIONAL INC, CHILIS T-2',
 'HOST INTERNATIONAL INC-GOOSE ISLAND T3',
 'HOST INTERNATIONAL INC-PRAIRIE TAP',
 'HOST INTERNATIONAL INC.',
 'HOST INTERNATIONAL, INC',
 'HOT DOG EXPRESS',
 'HUB 51',
 'HUDSON',
 'HUDSON NEWS',
 'HUDSON NEWS OHARE JOINT VENTURE',
 'ICE BAR',
 'INTELLIGENTSIA',
 'JAMBA JUICE',
 'KOREAN AIR LOUNGE',
 'LA TAPENADE GATE H14',
 'LA TAPENADES GATE H14',
 'LOU MITCHELLS EXPRESS INC',
 'MACARONI GRILL',
 'MANCHU WOK',
 'MCDONALDS',
 'MCDONALDS # 12785',
 'MCDONALDS # 17274',
 'MCDONALDS # 17277',
 'MCDONALDS # 22821',
 'MCDONALDS CORPORATION',
 'MCDONALDS RESTAURANT',
 'NATURAL BREAK',
 'NUTS ON CLARK',
 'OBRIENS RESTAURANT & BAR',
 'OHARE BAR',
 'OHARE HILTON HOTEL',
 'PARADES A CHICAGO BAR',
 'PUBLICAN TAVERN K1',
 'REGGIOS PIZZA EXPRESS',
 'ROCKY MOUNTAIN CHOCOLATE FACTORY',
 'RUSH STREET',
 'SALAD WORKS',
 'SARAHS CANDIES',
 'SAS',
 'SKYBRIDGE RESTAURANT & BAR',
 'SODEXO AMERICA, LLC',
 'STARBUCKS',
 'STARBUCKS HK APEX',
 'STARBUCKS L03',
 'SUBWAY SANDWICH',
 'SWISS AIR',
 'SWISSPORT USA',
 'THE GODDESS & GROCER',
 'THE GREAT AMERICAN BAGEL',
 'TOCCO',
 'TORTAS FRONTERA',
 'TRAVEL TRADERS #3081 @ HILTON OHARE',
 'TUSCANY CAFE',
 'UNITED AIRLINES CLUB',
 'UNITED CLUB',
 'UNITED CLUB ,T-1  CONCOURSE C',
 'UNITED CLUB, TERMINAL 2 CONCOURSE F',
 'UNITED CLUB,TERMINAL 1 CONCOURSE B SOUTH',
 'UNITED FIRST INTERNATIONAL LOUNGE T1,CONCOURSE C',
 'UNITED POLARIS LOUNGE - ORD',
 'URBAN OLIVE',
 'WOLFGANG EXPRESS',
 'WOLFGANG PUCK, T-3',
 'WOW BAO',
 'ZOOTS'}
```

# AKA Name displays the locations of the restaurant
```py
>>> ohare[0]
{'AKA Name': "STANLEY'S CHICAGO BLACKHAWK (T2 E5)",
 'Address': '11601 W TOUHY AVE ',
 'City': 'CHICAGO',
 'DBA Name': 'CHICAGO BLACKHAWKS STANLEYS T2 BAR',
 'Facility Type': 'Restaurant',
 'Inspection Date': '03/20/2020',
 'Inspection ID': '2366117',
 'Inspection Type': 'Canvass',
 'Latitude': '42.008536400868735',
 'License #': '34139',
 'Location': '(-87.91442843927047, 42.008536400868735)',
 'Longitude': '-87.91442843927047',
 'Results': 'Fail',
 'Risk': 'Risk 1 (High)',
 'State': 'IL',
 'Violations': '52. SEWAGE & WASTE WATER PROPERLY DISPOSED - Comments: '
               'OBSERVED THREE COMPARTMENT SINK IN DISHWASHING AREA IN '
               'DISREPAIR NOT DRAINING PROPERLY (SLOW DRAINING), WATER '
               'RELEASED FROM ONE COMPARTMENT (BASIN) BACKUP INSIDE ANOTHER '
               'COMPARTMENT (BASIN) WHEN RELEASED INSIDE SINK. INFORMED PERSON '
               'IN CHARGE OF REQUIREMENTS AND MUST REPAIR SINK AND MAINTAIN. '
               'PRIORITY VIOLATION 7-38-030(C) NO CITATION ISSUED',
 'Zip': '60666'}
>>> ohare[0]['AKA Name']
"STANLEY'S CHICAGO BLACKHAWK (T2 E5)"
>>> 
```

# Worst location in ohare to eat
```py
>>> c = Counter(row['AKA Name'] for row in ohare)
>>> c.most_common(10)
[('MACARONI GRILL (T3-K2)', 12),
 ('ARGO TEA  (T3 ROTUNDA)', 9),
 ("CHILI'S TOO (T2  F4)", 8),
 ("CHILI'S  TOO (T3-H2)", 7),
 ("HILTON O'HARE & ANDIAMO", 7),
 ('ARGO TEA (T2/E5)', 7),
 ('TOCCO (T5 M-07)', 7),
 ('United Employee Cafeteria (T1 C LL)', 6),
 ("REGGIO'S PIZZA EXPRESS (T3 G8)", 5),
 ('GARRETT POPCORN SHOPS (T3 H2)', 5)]
```

# Collect all the inspections in ohare airport based on License Key
```py
>>> ohare[0]
{'AKA Name': "STANLEY'S CHICAGO BLACKHAWK (T2 E5)",
 'Address': '11601 W TOUHY AVE ',
 'City': 'CHICAGO',
 'DBA Name': 'CHICAGO BLACKHAWKS STANLEYS T2 BAR',
 'Facility Type': 'Restaurant',
 'Inspection Date': '03/20/2020',
 'Inspection ID': '2366117',
 'Inspection Type': 'Canvass',
 'Latitude': '42.008536400868735',
 'License #': '34139',
 'Location': '(-87.91442843927047, 42.008536400868735)',
 'Longitude': '-87.91442843927047',
 'Results': 'Fail',
 'Risk': 'Risk 1 (High)',
 'State': 'IL',
 'Violations': '52. SEWAGE & WASTE WATER PROPERLY DISPOSED - Comments: '
               'OBSERVED THREE COMPARTMENT SINK IN DISHWASHING AREA IN '
               'DISREPAIR NOT DRAINING PROPERLY (SLOW DRAINING), WATER '
               'RELEASED FROM ONE COMPARTMENT (BASIN) BACKUP INSIDE ANOTHER '
               'COMPARTMENT (BASIN) WHEN RELEASED INSIDE SINK. INFORMED PERSON '
               'IN CHARGE OF REQUIREMENTS AND MUST REPAIR SINK AND MAINTAIN. '
               'PRIORITY VIOLATION 7-38-030(C) NO CITATION ISSUED',
 'Zip': '60666'}
>>>
>>> inspections = defaultdict(list)
>>> for row in ohare:
...     inspections[row['License #']].append(row)
... 
>>>
>>> inspections.keys()
dict_keys(['34139', '34192', '2232034', '2192977', '2488186', '34190', '2535614', '2535610', '34173', '1888807', '2487932', '2463991', '1333235', '2109577', '34169', '34205', '2289511', '2192969', '2204037', '1141505', '51206', '34220', '34224', '2017724', '2308566', '2708730', '2363771', '2192968', '2428079', '2487938', '1947515', '2464515', '2647047', '2192971', '2583234', '34222', '2192963', '34159', '1942304', '2487933', '1898075', '1898214', '2289515', '1140128', '34154', '2560546', '2069938', '1909532', '2363763', '34199', '2308553', '1042895', '1356711', '2535609', '2464518', '2304183', '2516647', '1884292', '2464526', '64032', '1879164', '2487937', '34236', '2487943', '1884293', '1140745', '1879167', '1909539', '2299087', '1909522', '1909523', '34142', '64540', '2487934', '2535613', '34215', '34217', '1381615', '2535615', '15531', '1954648', '1916161', '34146', '1141457', '2517809', '2517808', '2363760', '2284294', '2492747', '1974743', '2141979', '2487849', '34219', '2146327', '2492753', '2363766', '2487848', '1878675', '34235', '2492748', '2492754', '1621425', '2428080', '34210', '2009092', '2013208', '2013206', '2016729', '1885160', '0', '2447055', '2451545', '1916219', '56366', '2289084', '1333098', '2363762', '2016727', '56367', '1333242', '34234', '1142116', '2184012', '34167', '1120626', '1879166', '34212', '34183', '1675026', '2284027', '1927556', '2289520', '34203', '2289527', '2289525', '2289531', '2289524', '2289495', '2277391', '2277363', '2261728', '2232035', '2261733', '1224624', '29570', '85188', '1926528', '2125489', '2016732', '2124567', '2124574', '1333092', '2125246', '2103989', '2114331', '37170', '34211', '34229', '34201', '1069382', '1069379', '2009095', '23894', '1718776', '2021757'])
>>>
>>> inspections['34139']
[{'AKA Name': "STANLEY'S CHICAGO BLACKHAWK (T2 E5)",
  'Address': '11601 W TOUHY AVE ',
  'City': 'CHICAGO',
  'DBA Name': 'CHICAGO BLACKHAWKS STANLEYS T2 BAR',
  'Facility Type': 'Restaurant',
  'Inspection Date': '03/20/2020',
  'Inspection ID': '2366117',
  'Inspection Type': 'Canvass',
  'Latitude': '42.008536400868735',
  'License #': '34139',
  'Location': '(-87.91442843927047, 42.008536400868735)',
  'Longitude': '-87.91442843927047',
  'Results': 'Fail',
  'Risk': 'Risk 1 (High)',
  'State': 'IL',
  'Violations': '52. SEWAGE & WASTE WATER PROPERLY DISPOSED - Comments: '
                'OBSERVED THREE COMPARTMENT SINK IN DISHWASHING AREA IN '
                'DISREPAIR NOT DRAINING PROPERLY (SLOW DRAINING), WATER '
                'RELEASED FROM ONE COMPARTMENT (BASIN) BACKUP INSIDE ANOTHER '
                'COMPARTMENT (BASIN) WHEN RELEASED INSIDE SINK. INFORMED '
                'PERSON IN CHARGE OF REQUIREMENTS AND MUST REPAIR SINK AND '
                'MAINTAIN. PRIORITY VIOLATION 7-38-030(C) NO CITATION ISSUED',
  'Zip': '60666'},
 {'AKA Name': "STANLEY'S CHICAGO BLACKHAWK (T2 E5)",
  'Address': '11601 W TOUHY AVE ',
  'City': 'CHICAGO',
  'DBA Name': 'CHICAGO BLACKHAWKS STANLEYS T2 BAR',
  'Facility Type': 'Restaurant',
  'Inspection Date': '09/20/2011',
  'Inspection ID': '539433',
  'Inspection Type': 'Canvass',
  'Latitude': '42.008536400868735',
  'License #': '34139',
  'Location': '(-87.91442843927047, 42.008536400868735)',
  'Longitude': '-87.91442843927047',
  'Results': 'Fail',
  'Risk': 'Risk 1 (High)',
  'State': 'IL',
  'Violations': '2. FACILITIES TO MAINTAIN PROPER TEMPERATURE - Comments: All '
                'food establishments that display, prepare, or store '
                'potentially hazardous food shall have adequate refrigerated '
                'food storage facilities.  DISPLAY COOLER AT IMPROPER '
                'TEMPERATURE,CRITICAL VIOLATION CITATION ISSUED,DISPLAY COOLER '
                'AT 48.5F,INSTRUCTED COOLER MUST BE 40F OR LESS,TAG COOLER '
                'MUST CALL TECHNICIAN TO FIX | 3. POTENTIALLY HAZARDOUS FOOD '
                'MEETS TEMPERATURE REQUIREMENT DURING STORAGE, PREPARATION '
                'DISPLAY AND SERVICE - Comments: All cold food shall be stored '
                'at a temperature of 40F or less.  POTENTIALLY HAZARDOUS FOODS '
                'AT IMPROPER TEMPERATURE,CRITICAL VIOLATION,CITATION '
                'ISSUED,FOUND CHICKEN ,TURKEY,ROAST BEEF SANDWICHES AT 48.5F '
                'OF 44 PCS,MILK AND CHOCO MILK AT 47.5F,1 PINT OF 16 PCS,SALAD '
                'WITH SHREDDED CHEESE AND SHREDDED CHICKEN AT 48.5 OF 10 PKGS, '
                '6 PCS YOGURT AT 47.5F;MANAGER DISCARDED FOODS APPROXIMATELY '
                '$150,INSTRUCTED ALL COLD FOODS MUST BE 40F OR BELOW | 8. '
                'SANITIZING RINSE FOR EQUIPMENT AND UTENSILS:  CLEAN, PROPER '
                'TEMPERATURE, CONCENTRATION, EXPOSURE TIME - Comments: '
                'Equipment and utensils should get proper exposure to the '
                'sanitizing solution during the rinse cycle.  Bactericidal '
                'treatment shall consist of exposure of all dish and utensil '
                'surfaces to a rinse of clean water at a temperature of not '
                'less than 180F.  IMPROPER SANITIZING OF EQUIPMENT AND '
                'UTENSILS,CRITICAL VIOLATION,CITATION ISSUED,FOUND SANITIZING '
                'RINSE OF DISHMACHINE AT 170F,TECHNICIAN CAME AND FIXED THE '
                'MACHINE ,REACHED TO 180F;INSTRUCTED SANITIZING RINSE MUST BE '
                '180F AT ALL TIMES OR USE CHEMICAL SANITIZER CHLORINE WITH '
                '100ppm OR QUATS AT 200 ppm | 18. NO EVIDENCE OF RODENT OR '
                'INSECT OUTER OPENINGS PROTECTED/RODENT PROOFED, A WRITTEN LOG '
                'SHALL BE MAINTAINED AVAILABLE TO THE INSPECTORS - Comments: '
                'All necessary control measures shall be used to effectively '
                'minimize or eliminate the presence of rodents, roaches, and '
                'other vermin and insects on the premises of all food '
                'establishments, in food-transporting vehicles, and in vending '
                'machines.  FOUND 15 LIVE FRUIT FLIES IN THE BAR(12) AND '
                'CASHIER AREA(3),SERIOUS VIOLATION,CITATION ISSUED,INSTRUCTED '
                'RESTAURANT MUST BE FREE FROM INSECTS/PESTS,MUST COVER CUT UP '
                'LEMON,ORANGES IN THE BAR AREA AND DETAIL CLEAN '
                'COUNTERS,CABINETS ; GIVEN 5 DAYS 09-27-11 TO CORRECT '
                'VIOLATION,MUST CONTACT PEST CONTROL COMPANY FOR SERVICE | 32. '
                'FOOD AND NON-FOOD CONTACT SURFACES PROPERLY DESIGNED, '
                'CONSTRUCTED AND MAINTAINED - Comments: All food and non-food '
                'contact equipment and utensils shall be smooth, easily '
                'cleanable, and durable, and shall be in good repair.  MISING '
                'ICE BIN LID IN BAR AREA MUST PROVIDE;MISSING SALAD BAR COVER '
                'ABOVE 2 DOOR PREP COOLER MUST BE PROVIDED;  HAND SINK SOAP '
                'DISPENSER IN BAR AREA MUST BE FIXED ON THE WALL  | 33. FOOD '
                'AND NON-FOOD CONTACT EQUIPMENT UTENSILS CLEAN, FREE OF '
                'ABRASIVE DETERGENTS - Comments: All food and non-food contact '
                'surfaces of equipment and all food storage utensils shall be '
                'thoroughly cleaned and sanitized daily.  MUST CLEAN AND '
                'MAINTAIN INTERIOR AND EXTERIOR PANEL OF THE ICE MACHINE;   '
                'SHELVES OF 2 DOOR COOLER AND DISPLAY COOLER UNCLEAN MUST '
                'CLEAN AND MAINTAIN;  CABINETS FOR WINE AND SUPPLIES IN BAR '
                'AREA UNCLEAN MUST CLEAN AND MAINTAIN | 35. WALLS, CEILINGS, '
                'ATTACHED EQUIPMENT CONSTRUCTED PER CODE: GOOD REPAIR, '
                'SURFACES CLEAN AND DUST-LESS CLEANING METHODS - Comments: The '
                'walls and ceilings shall be in good repair and easily '
                'cleaned.  CEILING IN PREP AREA ABOVE COOLER UNCLEAN MUST '
                'CLEAN AND MAINTAIN | 36. LIGHTING: REQUIRED MINIMUM '
                'FOOT-CANDLES OF LIGHT PROVIDED, FIXTURES SHIELDED - Comments: '
                'Shielding to protect against broken glass falling into food '
                'shall be provided for all artificial lighting sources in '
                'preparation, service, and display facilities.  LIGHT FIXTURES '
                'IN PREP AREA WITH DUST ACCUMULATION MUST CLEAN AND MAINTAIN;  '
                'MUST SHOW PROOF THAT LIGHT BULBS IN THE HOT HOLDING AREA ARE '
                'SHATTER RESISTANT',
  'Zip': '60666'},
 {'AKA Name': "STANLEY'S CHICAGO BLACKHAWK (T2 E5)",
  'Address': '11601 W TOUHY AVE ',
  'City': 'CHICAGO',
  'DBA Name': 'CHICAGO BLACKHAWKS STANLEYS T2 BAR',
  'Facility Type': 'Restaurant',
  'Inspection Date': '04/20/2017',
  'Inspection ID': '2028622',
  'Inspection Type': 'Complaint',
  'Latitude': '42.008536400868735',
  'License #': '34139',
  'Location': '(-87.91442843927047, 42.008536400868735)',
  'Longitude': '-87.91442843927047',
  'Results': 'Fail',
  'Risk': 'Risk 1 (High)',
  'State': 'IL',
  'Violations': '29. PREVIOUS MINOR VIOLATION(S) CORRECTED 7-42-090 - '
                'Comments: Previous minor violations not corrected from report '
                "# 1978434, dated 12-20-16: Violation 33- 'Observed the back "
                'of the cooking equipment to have grease and food debris on '
                "it. Instructed facility to clean and maintain.' Violation 34- "
                "'Observed dirt and debris on the floors around the dish area. "
                "Instructed facility to clean and maintain.' and Violation 35- "
                "'Observed the ceiling vent above the 2 door produce cooler to "
                'have dust accumulation. Instructed facility to clean and '
                "maintain.' Instructed facility to correct all and maintain. "
                'Serious violation 7-42-090. | 32. FOOD AND NON-FOOD CONTACT '
                'SURFACES PROPERLY DESIGNED, CONSTRUCTED AND MAINTAINED - '
                'Comments: Instructed facility to install and maintain a '
                'splashguard at the right of the rear exposed handsink near '
                'the 1 compartment sink/prep table. | 33. FOOD AND NON-FOOD '
                'CONTACT EQUIPMENT UTENSILS CLEAN, FREE OF ABRASIVE DETERGENTS '
                '- Comments: Observed slight dirt accumulation in the upper '
                'interior portion of the ice machine. Instructed facility to '
                'clean, sanitize, and maintain. | 34. FLOORS: CONSTRUCTED PER '
                'CODE, CLEANED, GOOD REPAIR, COVING INSTALLED, DUST-LESS '
                'CLEANING METHODS USED - Comments: Observed the floors and '
                'floor drains in the bar and throughout the kitchen to have '
                'dirt and food debris accumulated, especially along walls and '
                'under and around equipment. Instructed facility to clean and '
                'maintain. | 35. WALLS, CEILINGS, ATTACHED EQUIPMENT '
                'CONSTRUCTED PER CODE: GOOD REPAIR, SURFACES CLEAN AND '
                'DUST-LESS CLEANING METHODS - Comments: Observed the drop '
                'ceiling tracks in the dish area to be rusty and dirty. '
                'Instructed facility to repair/replace and maintain.  Observed '
                'the walls in the dish area to be dirty. Instructed facility '
                'to clean and maintain. | 38. VENTILATION: ROOMS AND EQUIPMENT '
                'VENTED AS REQUIRED: PLUMBING: INSTALLED AND MAINTAINED - '
                'Comments: Observed the hot water handle at the dish machine '
                'sprayer to have a small leak. Instructed facility to repair '
                'and maintain.',
  'Zip': '60666'}]
```

# Get inspections data
```py
>>> [row['Inspection Date'] for row in inspections['34139']]
['03/20/2020', '09/20/2011', '04/20/2017']
```

# Most common violations
violotions are separated by (|)
```py
>>> ohare[2]['Violations']
('3. MANAGEMENT, FOOD EMPLOYEE AND CONDITIONAL EMPLOYEE; KNOWLEDGE, '
 'RESPONSIBILITIES AND REPORTING - Comments: FOUND NO EMPLOYEE HEALTH '
 'POLICY/TRAINING ON SITE. INSTRUCTED TO PROVIDE. PRIORITY FOUNDATION '
 'VIOLATION 7-38-010     NO CITATION ISSUED | 5. PROCEDURES FOR RESPONDING TO '
 'VOMITING AND DIARRHEAL EVENTS - Comments: FOUND NO PROCEDURE/PLAN FOR '
 'RESPONDING TO VOMITING AND DIARRHEAL EVENTS. INSTRUCTED TO PROVIDE AND '
 'MAINTAIN APPROPRIATE SUPPLIES OR KIT. (NECESSARY ITEMS AT A MINIMUM: '
 'GLOVES,  FACE MASKS,  DISPOSABLE MOPS AND APPROPRIATE SANITIZER THAT KILLS '
 'NOROVIRUS)   PRIORITY FOUNDATION VIOLATION 7-38-005   NO CITATION ISSUED | '
 '10. ADEQUATE HANDWASHING SINKS PROPERLY SUPPLIED AND ACCESSIBLE - Comments: '
 'INSTRUCTED TO PROVIDE HANDWASHING SIGNAGE FOR HANDSINK IN PREP AREA. | 22. '
 'PROPER COLD HOLDING TEMPERATURES - Comments: FOUND TCS FOOD AT IMPROPER '
 'TEMPERATURE REQUIREMENT DURING STORAGE INSIDE REACH-IN COOLER (AIR '
 'TEMPERATURE OF 50.2F) AND DISPLAY COOLER (AIR TEMPERATURE OF 52.3F, 42.5F) '
 'INTERNAL TEMPERATURE OF THE FOLLLOWING TCS FOODS: MILK AT 48.3, 47.9F, '
 '47.4F, CREAM AT 48.7, 49.1F, YOGURT AT 45.8F, 48.6F, PRE-PACKAGED GREEN '
 'SALAD WITH DELI MEAT AT 57.5F, 58.9F. INSTRUCTED MANAGEMENT TCS FOODS MUST '
 'MAINTAIN COLD HOLDING TEMPERATURE OF 41.0F OR BELOW. MANAGER DISCARDED THE '
 'SAID FOOD PRODUCTS. TOTAL VALUE $ 100.00, TOTAL WEIGHT  30 LBS. PRIORITY '
 'VIOLATION 7-38-005    CITATION ISSUED | 23. PROPER DATE MARKING AND '
 'DISPOSITION - Comments: INSTRUCTED TO PROPERLY LABEL AND DATE READY TO EAT '
 'TCS FOODS HELD OVER 24 HOURS INSIDE COOLERS. MUST IDENTIFY PRODUCT SHELF '
 "LIFE OR 'CONSUME BY' DATING (7 DAYS FROM PREPARATION DATE). PRIORITY "
 'FOUNDATION VIOLATION 7-38-005  NO CITATION  ISSUED | 33. PROPER COOLING '
 'METHODS USED; ADEQUATE EQUIPMENT FOR TEMPERATURE CONTROL - Comments: FOUND '
 'COLD HOLDING UNITS WITH TCS FOODS NOT MAINTAINING PROPER TEMPERATURE. NOTED '
 'REACH-IN COOLER WITH AN AIR TEMPERATURE OF 50.2F AND DISPLAY COOLER WITH AN '
 'AIR TEMPERATURE OF 52.3F, 46.3F. (BUSINESS HAS ONLY REACH-IN COOLER AND '
 'DISPLAY COOLER AVAILABLE) INSTRUCTED MANAGER, COOLING EQUIPMENT WITH TCS '
 'FOODS MUST MAINTAIN COLD HOLDING TEMPERATURE OF 41.0F OR BELOW. COLD HOLDING '
 "UNIT IS TAGGED 'HELD FOR INSPECTION' INSTRUCTED NOT TO USE UNTIL REPAIRED "
 '(SEE COMMENTS BELOW). PRIORITY VIOLATION 7-38-005   CITATION ISSUED | 36. '
 'THERMOMETERS PROVIDED & ACCURATE - Comments: INSTRUCTED TO PROVIDE '
 'THERMOMETER VISIBLE AND ACCURATE INSIDE ALL COOLERS. | 40. PERSONAL '
 'CLEANLINESS - Comments: EMPLOYEE BEHIND FOOD COUNTER MUST WEAR EFFECTIVE '
 'HAIR RESTRAINTS (HAIRNETS/CAPS)  | 47. FOOD & NON-FOOD CONTACT SURFACES '
 'CLEANABLE, PROPERLY DESIGNED, CONSTRUCTED & USED - Comments: INSTRUCTED TO '
 'DETAIL CLEAN AND MAINTAIN INTERIOR SURFACES OF STORAGE CABINETS  IN PREP '
 'AREA. | 47. FOOD & NON-FOOD CONTACT SURFACES CLEANABLE, PROPERLY DESIGNED, '
 'CONSTRUCTED & USED - Comments: INSTRUCTED TO DETAIL CLEAN AND MAINTAIN RACK '
 'INSIDE REACH-IN COOLER. | 49. NON-FOOD/FOOD CONTACT SURFACES CLEAN - '
 'Comments: INSTRUCTED TO DETAIL CLEAN AND MAINTAIN COUNTERTOPS WITH DUST AND '
 'FOOD DEBRIS UNDERNEATH COFFEE MACHINES BEHIND FRONT SERVICE COUNTER. | 51. '
 'PLUMBING INSTALLED; PROPER BACKFLOW DEVICES - Comments: BACKFLOW PREVENTER '
 'DEVICE NOT LOCATED BEHIND/UNDERNEATH ESPRESSO MACHINE.            INSTRUCTED '
 'TO INSTALL SO THAT IT CAN BE LOCATED TO BE SERVICED AND MAINTAINED. | 55. '
 'PHYSICAL FACILITIES INSTALLED, MAINTAINED & CLEAN - Comments: INSTRUCTED TO '
 'DETAIL CLEAN AND MAINTAIN FLOORS WITH DUST AND FOOD DEBRIS ALONG THE WALLS '
 'AND IN ALL CORNERS IN PREP/SERVICE AREA ESPECIALLY UNDER AND AROUND 3 '
 'COMPARTMENT SINK. | 55. PHYSICAL FACILITIES INSTALLED, MAINTAINED & CLEAN - '
 'Comments: INSTRUCTED TO CLEAN AND MAINTAIN GARBAGE CONTAINER AREA. USABLE '
 'ITEMS (FOOD AND NON FOOD) MUST BE STORED OFF THE FLOOR FOR EASY ACCESS ON '
 'CLEANING.')
>>>
>>> violations = ohare[2]['Violations'].split('|')
>>> violoations
['3. MANAGEMENT, FOOD EMPLOYEE AND CONDITIONAL EMPLOYEE; KNOWLEDGE, '
 'RESPONSIBILITIES AND REPORTING - Comments: FOUND NO EMPLOYEE HEALTH '
 'POLICY/TRAINING ON SITE. INSTRUCTED TO PROVIDE. PRIORITY FOUNDATION '
 'VIOLATION 7-38-010     NO CITATION ISSUED ',
 ' 5. PROCEDURES FOR RESPONDING TO VOMITING AND DIARRHEAL EVENTS - Comments: '
 'FOUND NO PROCEDURE/PLAN FOR RESPONDING TO VOMITING AND DIARRHEAL EVENTS. '
 'INSTRUCTED TO PROVIDE AND MAINTAIN APPROPRIATE SUPPLIES OR KIT. (NECESSARY '
 'ITEMS AT A MINIMUM: GLOVES,  FACE MASKS,  DISPOSABLE MOPS AND APPROPRIATE '
 'SANITIZER THAT KILLS NOROVIRUS)   PRIORITY FOUNDATION VIOLATION 7-38-005   '
 'NO CITATION ISSUED ',
 ' 10. ADEQUATE HANDWASHING SINKS PROPERLY SUPPLIED AND ACCESSIBLE - Comments: '
 'INSTRUCTED TO PROVIDE HANDWASHING SIGNAGE FOR HANDSINK IN PREP AREA. ',
 ' 22. PROPER COLD HOLDING TEMPERATURES - Comments: FOUND TCS FOOD AT IMPROPER '
 'TEMPERATURE REQUIREMENT DURING STORAGE INSIDE REACH-IN COOLER (AIR '
 'TEMPERATURE OF 50.2F) AND DISPLAY COOLER (AIR TEMPERATURE OF 52.3F, 42.5F) '
 'INTERNAL TEMPERATURE OF THE FOLLLOWING TCS FOODS: MILK AT 48.3, 47.9F, '
 '47.4F, CREAM AT 48.7, 49.1F, YOGURT AT 45.8F, 48.6F, PRE-PACKAGED GREEN '
 'SALAD WITH DELI MEAT AT 57.5F, 58.9F. INSTRUCTED MANAGEMENT TCS FOODS MUST '
 'MAINTAIN COLD HOLDING TEMPERATURE OF 41.0F OR BELOW. MANAGER DISCARDED THE '
 'SAID FOOD PRODUCTS. TOTAL VALUE $ 100.00, TOTAL WEIGHT  30 LBS. PRIORITY '
 'VIOLATION 7-38-005    CITATION ISSUED ',
 ' 23. PROPER DATE MARKING AND DISPOSITION - Comments: INSTRUCTED TO PROPERLY '
 'LABEL AND DATE READY TO EAT TCS FOODS HELD OVER 24 HOURS INSIDE COOLERS. '
 "MUST IDENTIFY PRODUCT SHELF LIFE OR 'CONSUME BY' DATING (7 DAYS FROM "
 'PREPARATION DATE). PRIORITY FOUNDATION VIOLATION 7-38-005  NO CITATION  '
 'ISSUED ',
 ' 33. PROPER COOLING METHODS USED; ADEQUATE EQUIPMENT FOR TEMPERATURE CONTROL '
 '- Comments: FOUND COLD HOLDING UNITS WITH TCS FOODS NOT MAINTAINING PROPER '
 'TEMPERATURE. NOTED REACH-IN COOLER WITH AN AIR TEMPERATURE OF 50.2F AND '
 'DISPLAY COOLER WITH AN AIR TEMPERATURE OF 52.3F, 46.3F. (BUSINESS HAS ONLY '
 'REACH-IN COOLER AND DISPLAY COOLER AVAILABLE) INSTRUCTED MANAGER, COOLING '
 'EQUIPMENT WITH TCS FOODS MUST MAINTAIN COLD HOLDING TEMPERATURE OF 41.0F OR '
 "BELOW. COLD HOLDING UNIT IS TAGGED 'HELD FOR INSPECTION' INSTRUCTED NOT TO "
 'USE UNTIL REPAIRED (SEE COMMENTS BELOW). PRIORITY VIOLATION 7-38-005   '
 'CITATION ISSUED ',
 ' 36. THERMOMETERS PROVIDED & ACCURATE - Comments: INSTRUCTED TO PROVIDE '
 'THERMOMETER VISIBLE AND ACCURATE INSIDE ALL COOLERS. ',
 ' 40. PERSONAL CLEANLINESS - Comments: EMPLOYEE BEHIND FOOD COUNTER MUST WEAR '
 'EFFECTIVE HAIR RESTRAINTS (HAIRNETS/CAPS)  ',
 ' 47. FOOD & NON-FOOD CONTACT SURFACES CLEANABLE, PROPERLY DESIGNED, '
 'CONSTRUCTED & USED - Comments: INSTRUCTED TO DETAIL CLEAN AND MAINTAIN '
 'INTERIOR SURFACES OF STORAGE CABINETS  IN PREP AREA. ',
 ' 47. FOOD & NON-FOOD CONTACT SURFACES CLEANABLE, PROPERLY DESIGNED, '
 'CONSTRUCTED & USED - Comments: INSTRUCTED TO DETAIL CLEAN AND MAINTAIN RACK '
 'INSIDE REACH-IN COOLER. ',
 ' 49. NON-FOOD/FOOD CONTACT SURFACES CLEAN - Comments: INSTRUCTED TO DETAIL '
 'CLEAN AND MAINTAIN COUNTERTOPS WITH DUST AND FOOD DEBRIS UNDERNEATH COFFEE '
 'MACHINES BEHIND FRONT SERVICE COUNTER. ',
 ' 51. PLUMBING INSTALLED; PROPER BACKFLOW DEVICES - Comments: BACKFLOW '
 'PREVENTER DEVICE NOT LOCATED BEHIND/UNDERNEATH ESPRESSO MACHINE.            '
 'INSTRUCTED TO INSTALL SO THAT IT CAN BE LOCATED TO BE SERVICED AND '
 'MAINTAINED. ',
 ' 55. PHYSICAL FACILITIES INSTALLED, MAINTAINED & CLEAN - Comments: '
 'INSTRUCTED TO DETAIL CLEAN AND MAINTAIN FLOORS WITH DUST AND FOOD DEBRIS '
 'ALONG THE WALLS AND IN ALL CORNERS IN PREP/SERVICE AREA ESPECIALLY UNDER AND '
 'AROUND 3 COMPARTMENT SINK. ',
 ' 55. PHYSICAL FACILITIES INSTALLED, MAINTAINED & CLEAN - Comments: '
 'INSTRUCTED TO CLEAN AND MAINTAIN GARBAGE CONTAINER AREA. USABLE ITEMS (FOOD '
 'AND NON FOOD) MUST BE STORED OFF THE FLOOR FOR EASY ACCESS ON CLEANING.']
```

# Strip out the comments in violations
```py
>>> v = 'WANTED WORDS - Comments: boo hoo'
>>> v[:v.find('- Comments:')]
'WANTED WORDS '
>>> v[:v.find('- Comments:')].strip()
'WANTED WORDS'
>>>
>>> [v[:v.find('- Comments:')].strip() for v in violations]
['3. MANAGEMENT, FOOD EMPLOYEE AND CONDITIONAL EMPLOYEE; KNOWLEDGE, '
 'RESPONSIBILITIES AND REPORTING',
 '5. PROCEDURES FOR RESPONDING TO VOMITING AND DIARRHEAL EVENTS',
 '10. ADEQUATE HANDWASHING SINKS PROPERLY SUPPLIED AND ACCESSIBLE',
 '22. PROPER COLD HOLDING TEMPERATURES',
 '23. PROPER DATE MARKING AND DISPOSITION',
 '33. PROPER COOLING METHODS USED; ADEQUATE EQUIPMENT FOR TEMPERATURE CONTROL',
 '36. THERMOMETERS PROVIDED & ACCURATE',
 '40. PERSONAL CLEANLINESS',
 '47. FOOD & NON-FOOD CONTACT SURFACES CLEANABLE, PROPERLY DESIGNED, '
 'CONSTRUCTED & USED',
 '47. FOOD & NON-FOOD CONTACT SURFACES CLEANABLE, PROPERLY DESIGNED, '
 'CONSTRUCTED & USED',
 '49. NON-FOOD/FOOD CONTACT SURFACES CLEAN',
 '51. PLUMBING INSTALLED; PROPER BACKFLOW DEVICES',
 '55. PHYSICAL FACILITIES INSTALLED, MAINTAINED & CLEAN',
 '55. PHYSICAL FACILITIES INSTALLED, MAINTAINED & CLEAN']
```

# Whats the most common violations in ohare airport
```py
>>> all_violations = [row['Violations'].split('|') for row in ohare]
>>> len(all_violations)
347
>>>
>>> c = Counter()
>>> 
>>> for violations in all_violations:
...     for v in violations:
...             c[v[:v.find('- Comments:')].strip()] += 1
... 
>>> c.most_common(5)
[('34. FLOORS: CONSTRUCTED PER CODE, CLEANED, GOOD REPAIR, COVING INSTALLED, '
  'DUST-LESS CLEANING METHODS USED',
  166),
 ('33. FOOD AND NON-FOOD CONTACT EQUIPMENT UTENSILS CLEAN, FREE OF ABRASIVE '
  'DETERGENTS',
  158),
 ('35. WALLS, CEILINGS, ATTACHED EQUIPMENT CONSTRUCTED PER CODE: GOOD REPAIR, '
  'SURFACES CLEAN AND DUST-LESS CLEANING METHODS',
  139),
 ('18. NO EVIDENCE OF RODENT OR INSECT OUTER OPENINGS PROTECTED/RODENT '
  'PROOFED, A WRITTEN LOG SHALL BE MAINTAINED AVAILABLE TO THE INSPECTORS',
  118),
 ('32. FOOD AND NON-FOOD CONTACT SURFACES PROPERLY DESIGNED, CONSTRUCTED AND '
  'MAINTAINED',
  114)]
```
