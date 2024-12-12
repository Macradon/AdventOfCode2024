result = 0
location_id_list_1 = []
location_id_list_2 = []

with open("input", "r") as file:
    print('Reading file')
    for line in file:
        location_id_1, location_id_2 = map(int, line.split())
        location_id_list_1.append(location_id_1)
        location_id_list_2.append(location_id_2)

for location_id in location_id_list_1:
    id_occurance = location_id_list_2.count(location_id)
    result = result + (id_occurance * location_id)

print(result)