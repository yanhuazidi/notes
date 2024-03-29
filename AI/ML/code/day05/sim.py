# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import numpy as np
with open('../../data/ratings.json') as f:
    ratings = json.loads(f.read())
users, scmat = list(ratings.keys()), []
for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()
        for movie in ratings[user1]:
            if movie in ratings[user2]:
                movies.add(movie)
        if len(movies) == 0:
            score = 0
        else:
            x, y = [], []
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
            score = np.corrcoef(x, y)[0, 1]
        scrow.append(score)
    scmat.append(scrow)
users = np.array(users)
scmat = np.array(scmat)
for i, user in enumerate(users):
    sorted_indices = scmat[i].argsort()[::-1]
    similar_indices = sorted_indices[sorted_indices != i]
    similar_users = users[similar_indices]
    similar_scores = scmat[i, similar_indices]
    print(user)
    for similar_user, similar_score in zip(
            similar_users, similar_scores):
        print('%9.2f %s' % (
            similar_score, similar_user))
