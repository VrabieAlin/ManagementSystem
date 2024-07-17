'''
Method used by sqllite3 cursor so it can return dict not tuples
'''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
