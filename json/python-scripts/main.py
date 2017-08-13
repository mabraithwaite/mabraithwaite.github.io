import requests # $ pip install requests
from bs4 import BeautifulSoup # $ pip install beautifulsoup4
from dog import Dog

base_url = "http://www.cachehumane.org"
dogs_page = "/animals/adoptable-dogs"
page_number_query = "/?page="
current_page = 1
url = base_url + dogs_page + page_number_query + str(current_page)

def get_dog_json():
    global base_url
    global dogs_page
    global page_number_query
    global current_page
    global url
    
    dogs = []
    soup_text = requests.get(url).text
    soup = BeautifulSoup(soup_text, 'html.parser')

    page_links = soup.find('div', {'class' : 'page_links'})
    number_of_pages = int(page_links.contents[-2].get_text().strip())

    while current_page <= number_of_pages:
        dog_divs = soup.findAll('div', {'class': 'a_box'})
        for dog_div in dog_divs:
            dog = populate_dog_info(dog_div)
        
            if dog is not None:
                dogs.append(dog)
        current_page += 1
        if current_page <= number_of_pages:
            url = base_url + dogs_page + page_number_query + str(current_page)
            soup_text = requests.get(url).text
            soup = BeautifulSoup(soup_text, 'html.parser')

    return make_json(dogs)

def populate_dog_info(dog_div):
    global base_url
    
    dog = Dog()
    dog.shCode = dog_div.find('div', {'class' : 'sh_code'}).get_text().strip()
    dog.image = base_url + dog_div.find('img')['src']
    dog.name = dog_div.h3.get_text().strip()

    element = dog_div.find('td')
    dog.goodWithDogs = element.get_text().strip()
    element = element.find_next()
    dog.goodWithCats = element.get_text().strip()
    element = element.find_next()
    dog.goodWithChildren = element.get_text().strip()

    element = dog_div.find('b').next_element
    dog.breed = element.next_element.strip()
    element = element.find_next().find_next().next_element
    dog.gender = element.next_element.strip()
    element = element.find_next().find_next().next_element
    dog.ageStr = element.next_element.strip()
    dog.year, dog.month = get_age(element.next_element.strip())
    element = element.find_next().find_next().next_element
    dog.housetrained = element.next_element.strip()

    dog.bio = dog_div.find('p', {'class' : 'an_comments'}).get_text().strip()

    return dog

def get_age(age):
    year = 0
    month = 0
    temp = age.split(' ')
    if len(temp) > 1:
        if 'year' in temp[1]:
            try:
                year = int(float(temp[0].strip()))
            except ValueError:
                year = 0
        elif 'month' in temp[1]:
            try:
                month = int(float(temp[0].strip()))
            except ValueError:
                month = 0
        else:
            year = 0
            month = 0
            return year, month
        if len(temp) > 3:
            if 'year' in temp[3]:
                try:
                    year = int(float(temp[2].strip()))
                except ValueError:
                    year = 0
            elif 'month' in temp[3]:
                try:
                    month = int(float(temp[2].strip()))
                except ValueError:
                    month = 0
            else:
                year = 0
                month = 0
                return year, month

    return year, month
    

def make_json(dogs):
    jsonObject = "{\n"
    jsonObject += "  \"dogs\": [\n"

    number_of_dogs = len(dogs)
    for i in range(number_of_dogs):
        jsonObject += dogs[i].to_json("    ")
        if i < number_of_dogs - 1:
            jsonObject += ",\n"
        else: jsonObject += "\n"

    jsonObject += "  ]\n"
    jsonObject += "}"

    return jsonObject

dog_json_file = open('../dogs.json', 'w')
dog_json = get_dog_json()
dog_json_file.write(dog_json)
dog_json_file.close()
