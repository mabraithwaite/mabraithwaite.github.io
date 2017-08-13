import json

class Dog:
    """Hold details on the dog"""

    def __init__(self):
        """Initialize variables"""
        self.shCode = ""
        self.image = ""
        self.name = ""
        self.breed = ""
        self.gender = ""
        self.year = 0
        self.month = 0
        self.ageStr = ""
        self.housetrained = ""
        self.goodWithDogs = ""
        self.goodWithCats = ""
        self.goodWithChildren = ""
        self.bio = ""

    def to_json(self, indent = ""):
        """Return a string representation of the object."""
        jsonObject = indent + "{\n"
        jsonObject += indent + "  \"shCode\": " + json.dumps(self.shCode) + ",\n"
        jsonObject += indent + "  \"image\": " + json.dumps(self.image) + ",\n"
        jsonObject += indent + "  \"name\": " + json.dumps(self.name) + ",\n"
        jsonObject += indent + "  \"breed\": " + json.dumps(self.breed) + ",\n"
        jsonObject += indent + "  \"gender\": " + json.dumps(self.gender) + ",\n"
        jsonObject += indent + "  \"age\": {\n"
        jsonObject += indent + "    \"year\": " + str(self.year) + ",\n"
        jsonObject += indent + "    \"month\": " + str(self.month) + ",\n"
        jsonObject += indent + "    \"ageStr\": " + json.dumps(self.ageStr) + "\n"
        jsonObject += indent + "  },\n"
        jsonObject += indent + "  \"housetrained\": " + json.dumps(self.housetrained) + ",\n"
        jsonObject += indent + "  \"goodWithDogs\": " + json.dumps(self.goodWithDogs) + ",\n"
        jsonObject += indent + "  \"goodWithCats\": " + json.dumps(self.goodWithCats) + ",\n"
        jsonObject += indent + "  \"goodWithChildren\": " + json.dumps(self.goodWithChildren) + ",\n"
        jsonObject += indent + "  \"bio\": " + json.dumps(self.bio) + "\n"
        jsonObject += indent + "}"
        
        return jsonObject
