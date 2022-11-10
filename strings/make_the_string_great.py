from typing import Tuple


class Solution:
    def makeGood(self, s: str) -> str:
        result = []

        for current in s:
            if not result:
                result.append(current)
                continue

            previous = result.pop()

            if not (
                    (current.lower() == previous.lower()) and
                    (
                            ( current.islower() and previous.isupper()) or
                            ( current.isupper() and previous.islower())
                    )
            ):
                result.append(previous)
                result.append(current)

        return "".join(result)


