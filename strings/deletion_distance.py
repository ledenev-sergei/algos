def deletion_distance(str1, str2):
    if not str1:
        return len(str2)

    if not str2:
        return len(str1)

    if str1[-1] != str2[-1]:
        result = 1 + min(deletion_distance(str1[:-1], str2), deletion_distance(str1, str2[:-1]))
    else:
        result = deletion_distance(str1[:-1], str2[:-1])

    return result
