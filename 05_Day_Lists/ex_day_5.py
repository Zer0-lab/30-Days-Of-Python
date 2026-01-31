list = []

list2 = ['star wars', 'arc raiders', 'monster hunter', 'avengers', 'apple', 'dragon']
print(list2)  # ['star wars', 'arc raiders', 'monster hunter', 'avengers', 'apple', 'dragon']

print(len(list2))  # 6

print(list2[0])  # 'star wars'
print(list2[2])  # 'monster hunter'
print(list2[5])  # 'dragon'
print(list2[-6])  # 'star wars'
print(list2[-4]) # 'monster hunter'
print(list2[-1]) # 'dragon'


mixed_data_types = ['Kevin', 78, True, 'BE']
print(mixed_data_types)  # ['Kevin', 78, True, 'BE']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)  # ['Facebook', 'Google', 'Microsoft', 'Apple',

print(len(it_companies))  # 7

print(it_companies[0])  # 'Facebook'
print(it_companies[3])  # 'Apple'
print(it_companies[-1])  # 'Amazon'

it_companies[0] = 'Meta'
it_companies[3] = 'AMD'
it_companies[-1] = 'Tesla'
print(it_companies)  # ['Meta', 'Google', 'Microsoft', 'AMD', 'IBM', 'Oracle', 'Tesla']


it_companies.append('Samsung')
print(it_companies)  # ['Meta', 'Google', 'Microsoft', 'AMD', 'IBM', 'Oracle', 'Tesla', 'Samsung']

it_companies.insert(3, 'Netflix')
print(it_companies)  # ['Meta', 'Google', 'Microsoft', 'Netflix', 'AMD', 'IBM', 'Oracle', 'Tesla']

it_companies[1] = it_companies[1].upper()
print(it_companies)  # ['Meta', 'GOOGLE', 'Microsoft', 'Netflix', 'AMD', 'IBM', 'Oracle', 'Tesla']

it_companies_string = '#; '.join(it_companies)
print(it_companies_string)  # 'Meta#; GOOGLE#; Microsoft#; Netflix#; AMD#; IBM#; Oracle#; Tesla'

print('Xiaomi' in it_companies)  # True

it_companies.sort()
print(it_companies)  # ['AMD', 'GOOGLE', 'IBM', 'Meta', 'Microsoft', 'Netflix', 'Oracle', 'Tesla']

it_companies.reverse()
print(it_companies)  # ['Tesla', 'Oracle', 'Netflix', 'Microsoft', 'Meta', 'IBM', 'GOOGLE', 'AMD']

print(it_companies[0:3])  # ['Tesla', 'Oracle', 'Netflix']

print(it_companies[4:])  # ['Meta', 'IBM', 'GOOGLE', 'AMD']

it_companies.remove('Tesla')
print(it_companies)  # ['Oracle', 'Netflix', 'Microsoft', 'Meta', 'IBM', 'GOOGLE', 'AMD']

it_companies.pop(2)
print(it_companies)  # ['Oracle', 'Netflix', 'Meta', 'IBM', 'GOOGLE', 'AMD']

del it_companies[-1]

print(it_companies)  # ['Oracle', 'Netflix', 'Meta', 'IBM', 'GOOGLE']

it_companies.clear()
print(it_companies)  # []

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

front_end.copy()
print(front_end)  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(max(ages))  # 26
print(min(ages))  # 19

ages.append(min(ages))
ages.append(max(ages))

ages.sort()
print(ages)  # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
median_index = len(ages) // 2
median = ages[median_index] if len(ages) % 2 != 0 else (ages[median_index - 1] + ages[median_index]) / 2
print("Median age is:", median)  # Median age is: 24

print(sum(ages) / len(ages))  # 22.75

print(abs(min(ages) - (sum(ages) / len(ages))))  # 3.75

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

middle_index = len(countries) // 2
print("Middle country:", countries[middle_index])  # Middle country: Mongolia

list_countries_split = countries[:len(countries)//2]
print("First half countries:", list_countries_split) # First half countries: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "
list_countries_split2 = countries[len(countries)//2:]
print("Second half countries:", list_countries_split2)  # Second half countries: ['Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan'

countries2 =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, scandican_countries= countries2[:3], countries2[3:]
print("First countries:", first_country)  # First countries: ['China', 'Russia', 'USA']
print("Scandinavian countries:", scandican_countries)  # Scandinavian countries: ['Finland', 'Sweden', 'Norway', 'Denmark']

