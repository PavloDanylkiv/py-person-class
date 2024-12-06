class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for i in people:
        result.append(Person(i["name"], i["age"]))
    for i in people:
        person = Person.people.get(i["name"])
        if "wife" in i and i["wife"]:
            wife_person = Person.people.get(i["wife"])
            person.wife = wife_person
            wife_person.husband = person
        elif "husband" in i and i["husband"]:
            husband_person = Person.people.get(i["husband"])
            person.husband = husband_person
            husband_person.wife = person
    return result
