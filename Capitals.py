print("Welcome to State and World Capitals")


states = {
"Alabama": "Montgomery",
"Alaska": "Juneau",
"Arizona": "Phoenix",
"Arkansas": "Little Rock",
"California": "Sacramento",
"Colorado": "Denver",
"Connecticut": "Hartford",
"Delaware": "Dover",
"Florida": "Tallahassee",
"Georgia": "Atlanta",
"Hawaii": "Honolulu",
"Idaho": 'Boise',
"Illinois": "Springfield",
"Indiana": "Indianapolis",
"Iowa": "Des Moines",
"Kansas": "Topeka",
"Kentucky": "Frankfort",
"Louisiana": "Baton Rouge",
"Maine": "Augusta",
"Maryland": "Annapolis",
"Massachusetts": "Boston",
"Michigan": "Lansing",
"Minnesota": "Saint Paul",
"Mississippi": "Jackson",
"Missouri": "Jefferson City",
"Montana": "Helena",
"Nebraska": "Lincoln",
"Nevada": "Carson City",
"New Hampshire": "Concord",
"New Jersey": "Trenton",
"New Mexico": "Santa Fe",
"New York": "Albany",
"North Carolina": "Raleigh",
"North Dakota": "Bismarck",
"Ohio": "Columbus",
"Oklahoma": "Oklahoma City",
"Oregon": "Salem",
"Pennsylvania": "Harrisburg",
"Rhode Island": "Providence",
"South Carolina": "Columbia",
"South Dakota": "Pierre",
"Tennessee": "Nashville",
"Texas": "Austin",
"Utah": "Salt Lake City",
"Vermont": "Montpelier",
"Virginia": "Richmond",
"Washington": "Olympia",
"West Virginia": "Charleston",
"Wisconsin": "Madison",
"Wyoming": "Cheyenne",
}

countries = {
"Afghanistan":
"Kabul",
"Albania":
"Tirana",
"Algeria":
"Algiers",
"Andorra":
"Andorra la Vella",
"Angola":
"Luanda",
"Antigua and Barbuda":
"Saint John's",
"Argentina":
"Buenos Aires",
"Armenia":
"Yerevan",
"Australia":
"Canberra",
"Austria":
"Vienna",
"Azerbaijan":
"Baku",
"Bahamas":
"Nassau",
"Bahrain":
"Manama",
"Bangladesh":
"Dhaka",
"Barbados":
"Bridgetown",
"Belarus":
"Minsk",
"Belgium":
"Brussels",
"Belize":
"Belmopan",
"Benin":
"Porto Novo",
"Bhutan":
"Thimphu",
"Bolivia":
"La Paz",
"Bosnia and Herzegovina":
"Sarajevo",
"Botswana":
"Gaborone",
"Brazil":
"Brasilia",
"Brunei":
"Bandar Seri Begawan",
"Bulgaria":
"Sofia",
"Burkina Faso":
"Ouagadougou",
"Burundi":
"Gitega",
"Cambodia":
"Phnom Penh",
"Cameroon":
"Yaounde",
"Canada":
"Ottawa",
"Cape Verde":
"Praia",
"Central African Republic":
"Bangui",
"Chad":
"N'Djamena",
"Chile":
"Santiago",
"China":
"Beijing",
"Colombia":
"Bogota",
"Comoros":
"Moroni",
"Democratic Republic of the Congo":
"Kinshasa",
"Republic of the Congo":
"Brazzaville",
"Costa Rica":
"San Jose",
"Cote d'Ivoire":
"Yamoussoukro",
"Croatia":
"Zagreb",
"Cuba":
"Havana",
"Cyprus":
"Nicosia",
"Czech Republic":
"Prague",
"Denmark":
"Copenhagen",
"Djibouti":
"Djibouti",
"Dominica":
"Roseau",
"Dominican Republic":
"Santo Domingo",
"East Timor":
"Dili",
"Ecuador":
"Quito",
"Egypt":
"Cairo",
"El Salvador":
"San Salvador",
"England":
"London",
"Equatorial Guinea":
"Malabo",
"Eritrea":
"Asmara",
"Estonia":
"Tallinn",
"Ethiopia":
"Addis Ababa",
"Federated States of Micronesia":
"Palikir",
"Fiji":
"Suva",
"Finland":
"Helsinki",
"France":
"Paris",
"French Guiana":
"Cayenne",
"Gabon":
"Libreville",
"Gambia":
"Banjul",
"Georgia":
"Tbilisi",
"Germany":
"Berlin",
"Ghana":
"Accra",
"Greece":
"Athens",
"Grenada":
"Saint George's",
"Guatemala":
"Guatemala City",
"Guinea":
"Conakry",
"Guinea-Bissau":
"Bissau",
"Guyana":
"Georgetown",
"Haiti":
"Port au Prince",
"Honduras":
"Tegucigalpa",
"Hungary":
"Budapest",
"Iceland":
"Reykjavik",
"India":
"New Delhi",
"Indonesia":
"Jakarta",
"Iran":
"Tehran",
"Iraq":
"Baghdad",
"Ireland":
"Dublin",
"Israel":
"Tel Aviv (Jerusalem has limited recognition)",
"Italy":
"Rome",
"Jamaica":
"Kingston",
"Japan":
"Tokyo",
"Jordan":
"Amman",
"Kazakhstan":
"Astana",
"Kenya":
"Nairobi",
"Kiribati":
"Tarawa Atoll",
"Kosovo":
"Pristina",
"Kuwait":
"Kuwait City",
"Kyrgyzstan":
"Bishkek",
"Laos":
"Vientiane",
"Latvia":
"Riga",
"Lebanon":
"Beirut",
"Lesotho":
"Maseru",
"Liberia":
"Monrovia",
"Libya":
"Tripoli",
"Liechtenstein":
"Vaduz",
"Lithuania":
"Vilnius",
"Luxembourg":
"Luxembourg",
"Macedonia":
"Skopje",
"Madagascar":
"Antananarivo",
"Malawi":
"Lilongwe",
"Malaysia":
"Kuala Lumpur",
"Maldives":
"Male",
"Mali":
"Bamako",
"Malta":
"Valletta",
"Marshall Islands":
"Majuro",
"Mauritania":
"Nouakchott",
"Mauritius":
"Port Louis",
"Mexico":
"Mexico City",
"Moldova":
"Chisinau",
"Monaco":
"Monaco",
"Mongolia":
"Ulaanbaatar",
"Montenegro":
"Podgorica",
"Morocco":
"Rabat",
"Mozambique":
"Maputo",
"Myanmar (Burma)":
"Nay Pyi Taw",
"Namibia":
"Windhoek",
"Nauru":
"No official capital",
"Nepal":
"Kathmandu",
"Netherlands":
"Amsterdam",
"New Zealand":
"Wellington",
"Nicaragua":
"Managua",
"Niger":
"Niamey",
"Nigeria":
"Abuja",
"North Korea":
"Pyongyang",
"Northern Ireland":
"Belfast",
"Norway":
"Oslo",
"Oman":
"Muscat",
"Pakistan":
"Islamabad",
"Palau":
"Melekeok",
"Panama":
"Panama City",
"Papua New Guinea":
"Port Moresby",
"Paraguay":
"Asuncion",
"Peru":
"Lima",
"Philippines":
"Manila",
"Poland":
"Warsaw",
"Portugal":
"Lisbon",
"Qatar":
"Doha",
"Romania":
"Bucharest",
"Russia":
"Moscow",
"Rwanda":
"Kigali",
"Saint Kitts and Nevis":
"Basseterre",
"Saint Lucia":
"Castries",
"Saint Vincent and the Grenadines":
"Kingstown",
"Samoa":
"Apia",
"San Marino":
"San Marino",
"Sao Tome and Principe":
"Sao Tome",
"Saudi Arabia":
"Riyadh",
"Scotland":
"Edinburgh",
"Senegal":
"Dakar",
"Serbia":
"Belgrade",
"Seychelles":
"Victoria",
"Sierra Leone":
"Freetown",
"Singapore":
"Singapore",
"Slovakia":
"Bratislava",
"Slovenia":
"Ljubljana",
"Solomon Islands":
"Honiara",
"Somalia":
"Mogadishu",
"South Africa":
"Pretoria, Bloemfontein, Cape Town",
"South Korea":
"Seoul",
"South Sudan":
"Juba",
"Spain":
"Madrid",
"Sri Lanka":
"Colombo",
"Sudan":
"Khartoum",
"Suriname":
"Paramaribo",
"Swaziland (Eswatini)":
"Mbabana",
"Sweden":
"Stockholm",
"Switzerland":
"Bern",
"Syria":
"Damascus",
"Taiwan":
"Taipei",
"Tajikistan":
"Dushanbe",
"Tanzania":
"Dodoma",
"Thailand":
"Bangkok",
"Togo":
"Lome",
"Tonga":
"Nuku'alofa",
"Trinidad and Tobago":
"Port of Spain",
"Tunisia":
"Tunis",
"Turkey":
"Ankara",
"Turkmenistan":
"Ashgabat",
"Tuvalu":
"Funafuti",
"Uganda":
"Kampala",
"Ukraine":
"Kiev",
"United Arab Emirates":
"Abu Dhabi",
"United Kingdom":
"London",
"United States":
"Washington D.C.",
"Uruguay":
"Montevideo",
"Uzbekistan":
"Tashkent",
"Vanuatu":
"Port Vila",
"Vatican City":
"Vatican City",
"Venezuela":
"Caracas",
"Vietnam":
"Hanoi",
"Wales":
"Cardiff",
"Yemen":
"Sana'a",
"Zambia":
"Lusaka",
"Zimbabwe":
"Harare",

}
starting = input("Would you like to start? Y or N ")
starting = starting.upper()
while starting == "Y":
  operation = input("Enter 1 for States or 2 for Countries and 3 to Exit ")
  if operation == "1":
    state = input("Enter a state ")
    state = state.title()
    if state in states:
        print(" The capital of {} is {}".format(state, states[state]))
    else:
        print("Invalid Input")
  elif operation == "2":
    country = input("Enter a country ")
    country = country.title()
    if country in countries:
        print(" The capital of {} is {}".format(country, countries[country]))
    else:
        print("Invalid Input")
  elif operation == "3":
      exit(0)
  else:
    print("Invalid Input")
else:
    exit(0)
