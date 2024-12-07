class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for item in people:
        some_var = Person(item["name"], item["age"])
        result.append(some_var)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if wife_name := person_data.get("wife"):
            person.wife = Person.people[wife_name]
        if husband_name := person_data.get("husband"):
            person.husband = Person.people[husband_name]

    return result
