result = 0
location_id_list_1 = []
location_id_list_2 = []

with open("input", "r") as file:
    print('Reading file')
    for line in file:
        location_id_1, location_id_2 = map(int, line.split())
        location_id_list_1.append(location_id_1)
        location_id_list_2.append(location_id_2)
location_id_list_1.sort()
location_id_list_2.sort()

length_1 = len(location_id_list_1)
length_2 = len(location_id_list_2)

if length_1 == length_2:
    print('Same length')
    i = 0
    while i < length_1:
        result = result + abs(location_id_list_1[i] - location_id_list_2[i])
        i +=1

print (result)