singers = {input(f"Enter the name of singer {i+1}: ") for i in range(int(input("Enter the number of singers: ")))}
dancers = {input(f"Enter the name of dancer {i+1}: ") for i in range(int(input("Enter the number of dancers: ")))}
all_artists = singers.union(dancers)
all_rounders = singers.intersection(dancers)
dancers_not_singers = dancers.difference(singers)
singers_not_dancers = singers.difference(dancers)
dancers_singers_exclusive = dancers.symmetric_difference(singers)
print("\nAll artists (either singers or dancers or both):", all_artists)
print("All-rounders (both singers and dancers):", all_rounders)
print("Dancers but not singers:", dancers_not_singers)
print("Singers but not dancers:", singers_not_dancers)
print("Dancers but not singers or singers but not dancers:", dancers_singers_exclusive)

