# EXTENDING BUILT IN TYPES
class Text(str):
    def duplicate(self):
        return self+self


test = Text(" This is only TEST")
print(f"1. Change to lowercase:\t {test.lower()}")
print(
    f"2. This is how we duplicate using builtin types duplicate \n{test.duplicate()}")
print(f"3.  This is how UPPER CASE the string >>> \t {test.upper()}.")
