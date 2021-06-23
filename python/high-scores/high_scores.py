def latest(scores):
    return scores.pop()


def personal_best(scores):
    scores.sort()
    return scores.pop()


def personal_top_three(scores):
    scores.sort(reverse=True)
    return [x for x in scores[0:3]]
