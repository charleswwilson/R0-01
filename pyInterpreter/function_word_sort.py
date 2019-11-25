from PyDictionary import PyDictionary

dictionary = PyDictionary()
# features="html.parser" added to env/lib/pythonx/site-packages/PyDictionary/utils.py

house_def = dictionary.meaning("house")


def word_type(item):
    word = dictionary.meaning(item)
    word_key = []
    word_def = []
    if word == None:
        word = {"none": ["none"]}
    for key in word:
        word_key.append(key)
    word_key_counter = 0
    for i in range(len(word_key)):
        word_def.append(word[word_key[i]][0])
    return word_key, word_def

    # print(word_key)
    # print(word_def)


def test_func():
    print(f"sun:{word_type('sun')}")
    print(f"holiday:{word_type('holiday')}")
    print(f"open:{word_type('open')}")
    print(f"if:{word_type('if')}")
    print(f"what:{word_type('what')}")