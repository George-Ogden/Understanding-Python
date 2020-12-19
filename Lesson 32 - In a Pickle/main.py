import pickle, json
from datetime import date

class Person:
    def __init__(self,**data):
        self.data = data
        self.name = data["name"]
        self.DOB = date(*data["DOB"])
        self.job = data["job"]
        self.skills = data["skills"]
    
    @property
    def age(self):
        today = date.today()
        return (today.year - self.DOB.year) - ((today.month,today.day) < (self.DOB.month,self.DOB.day))
    
    def __str__(self):
        return "Hello, my name is {name} and I am {age} years old.\nI am a {job} and my main skill is {skills[0]}".format(**self.data,age=self.age)
    
    def save(self,filename):
        with open("{}.json".format(filename),"w") as json_file:
            json.dump(self.data,json_file)

        with open("{}.pickle".format(filename),"wb") as pickle_file:
            pickle.dump(self,pickle_file)
    
    @staticmethod
    def from_JSON(JSON):
        return Person(**JSON)

    @property
    def json(self):
        return json.dumps(self.data)
    
    @property
    def pickle(self):
        return pickle.dumps(self)

person = Person(name="Fictional Person",DOB=(2001,1,1),job="coder",skills=["coding","maths","Python"])
print(person)

person.save("person")

with open("person.json") as json_file:
    person = Person.from_JSON(json.load(json_file))

with open("person.pickle","rb") as pickle_file:
    person = pickle.load(pickle_file)

print(person.json)
print(person.pickle)