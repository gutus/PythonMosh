# Making Custom Containers

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PytHon")
print(cloud.tags)
