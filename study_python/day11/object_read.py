import pickle

with open('mark.p', 'rb') as f:
    name = pickle.load(f)
    age = pickle.load(f)
    address = pickle.load(f)
    score = pickle.load(f)

    print(name)
    print(age)
    print(address)
    print(score)


