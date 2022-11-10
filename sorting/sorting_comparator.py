from functools import cmp_to_key


class Player:
    name: str
    score: int

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"""Player [name={self.name}][score={self.score}]"""

    @staticmethod
    def comparator(a: "Player", b: "Player"):
        """returns -1 if a < b , 0 if  a == b, and 1 if a > b."""
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1

        sorted_names = list(sorted([a.name, b.name]))

        if a.name == sorted_names[0]:
            return -1

        return 1


if __name__ == '__main__':

    n = int(input())
    data = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)