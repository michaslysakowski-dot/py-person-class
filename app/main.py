class Person:
    people = {}

    def __init__(self, name: str, age: int) -> list:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_to_add = Person(person["name"], person["age"])
        if person.get("wife"):
            person_to_add.wife = person["wife"]
        elif person.get("husband"):
            person_to_add.husband = person["husband"]
        person_list.append(person_to_add)

    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.husband]
    return person_list
