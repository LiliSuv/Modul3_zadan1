calls_ = 0
k = 0
m = 0
x = 0
def count_calls(calls_):
    calls_ = k + x
    print (calls_)
def string_info(string):
    n = len (string), string.upper (), string.lower ()
    print (n)
    global x
    x = x + 1
def is_contains(string, list_to_search):
    print (string in list_to_search)
    global k
    k = k + 1
string_ = 'Сегодня отличная погода', 'Теплое лето', "вся земля"
for i in range (3):
    string = string_[i]
    string_info (string)

list_to_search_ = (('Теплое лето', "вся земля", 'город мой'), ('Теплое лето', 'земля вся'))
string = "ВСЯ земля"
string = string.upper ()
for i in range (2):
    list_to_search = str (list_to_search_[i])
    list_to_search = list_to_search.upper ()
    is_contains (string, list_to_search)

count_calls(calls_)
