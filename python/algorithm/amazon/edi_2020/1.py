def k_with_max_v(d):
    if not d:
        return []
    rst = []
    max_v = max(d.values())
    for k, v in d.items():
        if v == max_v:
            rst.append(k)
    return rst

def favoriteVideoGenre(numUsers, userBooksListenedTo, numGenres, bookGenres):
    # WRITE YOUR CODE HERE
    book_to_genre = {}
    for g, books in bookGenres.items():
        for b in books:
            book_to_genre[b] = g
    rst = {}
    for u, books in userBooksListenedTo.items():
        tmp = {}
        for b in books:
            if b not in book_to_genre:
                continue
            g = book_to_genre[b]
            if g in tmp:
                tmp[g] += 1
            else:
                tmp[g] = 1
        rst[u] = k_with_max_v(tmp)
    return rst

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                1,
                {'john':['latin', 'tomb','nation']},
                1,
                {'history':['latin','nation'],
                'horror':['tomb']}
            ),
            {'john':['history']}
        ),
        (
            (
                1,
                {'john':['notfound', 'tomb','nation']},
                1,
                {'history':['latin','nation'],
                'horror':['tomb']}
            ),
            {'john':['horror','history']}
        ),
        (
            (
                1,
                {'john':[]},
                1,
                {'history':['latin','nation'],
                'horror':['tomb']}
            ),
            {'john':[]}
        ),

    ]
    test(favoriteVideoGenre, test_data)
