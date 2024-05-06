def find_id_sequence(entries, search_id):
    try:
        first_index = entries.index(search_id)
    except ValueError:
        return ()

    try:
        second_index = entries.index(search_id, first_index + 1)
        return entries[first_index:second_index + 1]
    except ValueError:
        return entries[first_index:]


print(find_id_sequence((1, 2, 3), 8))
print(find_id_sequence((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_id_sequence((1, 2, 8, 5, 1, 2, 9), 8))