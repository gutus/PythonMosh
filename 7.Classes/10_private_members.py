# PRIVATE MEMBERS

class TagCloud:
    def __init__(self):
        # dengan menambahkan double underscore sebagai prefix merubah attribute menjadi private
        self.__tags = {}
# dan tidak dapat diakses dari user luar

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PytHon")
print(cloud.__dict__)
