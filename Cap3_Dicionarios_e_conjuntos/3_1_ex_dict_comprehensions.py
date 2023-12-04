DIAL_CODES = [                                                  
(880, 'Bangladesh'),
(55,  'Brazil'),
(86,  'China'),
(91,  'India'),
(62,  'Indonesia'),
(81,  'Japan'),
(234, 'Nigeria'),
(92,  'Pakistan'),
(7,   'Russia'),
(1,   'United States'),
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
# {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62, 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}

dict2 = {code: country.upper() for country, code in country_code.items() if code < 66}
print(dict2)
# {55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}
