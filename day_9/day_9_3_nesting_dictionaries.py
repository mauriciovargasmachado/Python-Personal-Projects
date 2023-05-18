#nested dictionary in dictionary

capitals={
    'France':'Paris',
    'Spain':'Madrid',
    'Colombia':'Bogota',
    'Canada':'Otawa',
    'United States':'Washinton',
}

travel_log={
    'France':{'cities_visited':['Paris','Waterloo','Dijon'],'total_visits':12},
    'Spain':{'cities_visited':['Madrid','Barcelona','Malaga'],'total_visits':24},
    'Colombia':{'cities_visited':['Bogota','Medellin','Cartagena'],'total_visits':32},
    'Canada':'Otawa',
    'United States':'Washinton',
}

#nested dictionary in list

travel_log[
    {'city':'France','cities_visited':['Paris','Waterloo','Dijon'],'total_visits':12},
    {'City':'Spain','cities_visited':['Madrid','Barcelona','Malaga'],'total_visits':24},
    
]