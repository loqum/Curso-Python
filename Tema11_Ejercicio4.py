def sorting(collection):
    print("\nMayor a menor: ")
    print(sorted(collection, reverse=True))
    print("\nMayor a menor segun resto de 4: ")
    print(sorted(collection, reverse=True, key=lambda x: x % 4))


sorting(list(range(10)))
