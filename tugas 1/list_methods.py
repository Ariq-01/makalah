fruits = ["apel", "jeruk", "mangga"]

def append_element(lst):
    lst.append("pisang")
    print(lst)

def copy_list(lst):
    new = lst.copy()
    print(new)

def count_element(lst):
    print(lst.count("apel"))

def extend_list(lst):
    lst.extend(["melon", "anggur"])
    print(lst)

def find_index(lst):
    print(lst.index("mangga"))

def insert_element(lst):
    lst.insert(1, "lemon")
    print(lst)

def pop_last(lst):
    lst.pop()
    print(lst)

def remove_value(lst):
    lst.remove("jeruk")
    print(lst)

def reverse_list(lst):
    lst.reverse()
    print(lst)

def clear_list(lst):
    lst.clear()
    print(lst)


append_element(fruits)
copy_list(fruits)
count_element(fruits)
extend_list(fruits)
find_index(fruits)
insert_element(fruits)
pop_last(fruits)
remove_value(fruits)
reverse_list(fruits)
clear_list(fruits)
