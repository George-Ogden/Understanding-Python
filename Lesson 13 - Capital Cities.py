from random import sample
capital_cities = {"Canada":"Ottawa","United States of America":"Washington D.C.","Mexico":"Mexico City","Belize":"Belmopan","Guatemala":"Guatemala City","Honduras":"Tegucigalpa","El Salvador":"San Salvador","Nicaragua":"Managua","Costa Rica":"San Jose","Panama":"Panama City","Cuba":"Havana","Bahamas":"Nassau","Jamaica":"Kingston","Haiti":"Port au Prince","Dominican Republic":"Santo Domingo","Puerto Rico":"San Juan","Trinidad and Tobago":"Port of Spain","Dominica":"Roseau","St. Lucia":"Castries","Barbados":"Bridgetown","Antigua and Barbuda":"St. John's","Saint Kitts & Nevis":"Basseterre","St. Vincent & The Grenadines":"Kingstown","Grenada":"St. George's","Colombia":"Bogota","Venezuela":"Caracas","Guyana":"Georgetown","Suriname":"Paramaribo","French Guyana":"Cayenne","Ecuador":"Quito","Peru":"Lima","Brazil":"Brasilia","Bolivia":"La Paz","Paraguay":"Asuncion","Chile":"Santiago","Argentina":"Buenos Aires","Uruguay":"Montevideo","Morocco":"Rabat","Western Sahara":"El Aaiun","Algeria":"Algiers","Tunisia":"Tunis","Libya":"Tripoli","Egypt":"Cairo","Mali":"Bamako","Niger":"Niamey","Mauritania":"Nouakchott","Chad":"N'Djamena","Sudan":"Khartoum","Eritrea":"Asmara","Senegal":"Dakar","Gambia":"Banjul","Guinea Bissau":"Bissau","Guinea":"Conakry","Sierra Leone":"Freetown","Liberia":"Monrovia","Ivory Coast":"Yamoussoukro","Burkina Faso":"Ouagadougou","Ghana":"Accra","Togo":"Lome","Benin":"Porto Novo","Nigeria":"Abuja","Cameroon":"Yaounde","Central African Republic":"Bangui","Ethiopia":"Addis Ababa","Djibouti":"Djibouti","Somalia":"Mogadishu","Equatorial Guinea":"Malabo","Sao Tome and Principe":"Sao Tome","Gabon":"Libreville","Congo":"Brazzaville","Democratic Republic of Congo":"Kinshasa","Uganda":"Kampala","Rwanda":"Kigali","Burundi":"Bujumbura","Kenya":"Nairobi, Mombasa","Tanzania":"Dodoma","Angola":"Luanda","Zambia":"Lusaka","Malawi":"Lilongwe","Mozambique":"Maputo","Namibia":"Windhoek","Botswana":"Gaborone","Zimbabwe":"Harare","Swaziland":"Mbaban, Lobamba","South Africa":"Cape Town, Pretoria, and Bloemfontein","Lesotho":"Maseru","Madagascar":"Antananarivo","Comoros":"Moroni","Cape Verde":"Praia","Iceland":"Reykjavik","Norway":"Oslo","Sweden":"Stockholm","Finland":"Helsinki","Denmark":"Copenhagen","United Kingdom":"London","Ireland":"Dublin","Netherlands":"Amsterdam","Belgium":"Brussels","Luxembourg":"Luxembourg City","France":"Paris","Monaco":"Monaco","Germany":"Berlin","Austria":"Vienna","Switzerland":"Bern","Liechtenstein":"Vaduz","Spain":"Madrid","Andorra":"Andorra la Vella","Portugal":"Lisbon","Italy":"Rome","San Marino":"San Marino","Vatican City":"Vatican City","Malta":"Valetta","Estonia":"Talinn","Latvia":"Riga","Lithuania":"Vilnius","Belarus":"Minsk","Ukraine":"Kiev","Moldova":"Chisinau","Poland":"Warsaw","Czech Republic":"Prague","Slovakia":"Bratislava","Hungary":"Budapest","Slovenia":"Ljubljana","Croatia":"Zagreb","Romania":"Bucharest","Bosnia & Herzegovina":"Sarajevo","Serbia & Montenegro":"Belgrade","Bulgaria":"Sofia","Macedonia":"Skopje","Albania":"Tirana","Greece":"Athens","Cyprus":"Nicosia","Russia":"Moscow","Georgia":"Tbilisi","Azerbaijan":"Baku","Armenia":"Yerevan","Kazakhstan":"Astana","Uzbekistan":"Tashkent","Turkmenistan":"Ashgabat","Kyrgyzstan":"Bishkek","Tajikistan":"Dushanbe","Turkey":"Ankara","Iran":"Tehran","Lebanon":"Beirut","Syria":"Damascus","Israel":"Jerusalem","Jordan":"Amman","Iraq":"Baghdad","Kuwait":"Kuwait City","Saudi Arabia":"Riyadh","Bahrain":"Marama","Qatar":"Doha","United Arab Emirates":"Abu Dhabi","Oman":"Muscat","Yemen":"Sana'a","Afghanistan":"Kabul","Pakistan":"Islamabad","India":"New Dehli","Bangladesh":"Dhaka","Sri Lanka":"Colombo, Sri Jayawardenepura Kotte","Myanmar":"Naypyidaw","Laos":"Vientiane","Thailand":"Bangkok","Vietnam":"Hanoi","Cambodia":"Phnom Penh","Philippines":"Manila","Malaysia":"Kuala Lumpur","Singapore":"Singapore","Brunei":"Bandar Seri Begawan","Indonesia":"Jakarta","East Timor":"Dili","Papua New Guinea":"Port Moresby","Mongolia":"Ulaarbaatar","China":"Beijing","Nepal":"Kathmandu","Bhutan":"Thimpu","North Korea":"Pyongyang","South Korea":"Seoul","Taiwan":"Taipei","Japan":"Tokyo","Maldives":"Male","Mauritius":"Port Louis","Seychelles":"Victoria","Australia":"Canberra","New Zealand":"Wellington","Palau":"Ngerulmud","Micronesia":"Palikir","Marshall Islands":"Majuro","Nauru":"Nauru","Kiribati":"Tawara","Solomon Islands":"Honiara","Tuvalu":"Funafuti","Samoa":"Apia","Vanuatu":"Port Vila","Fiji":"Suva","Tonga":"Nuku'alofa","Palestine":"Palestine"}
score = 0
questions = sample(capital_cities.keys(),10)
for country in questions:
    answer = input("What is the capital of "+country+"?\n")
    city = capital_cities[country]
    if answer == city:
        print("Correct!")
        score += 1
    else:
        print("The capital of",country,"is",city)
print("You scored ",score,"/10",sep="")