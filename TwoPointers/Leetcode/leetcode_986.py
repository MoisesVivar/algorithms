
def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    intersecs = []
    first_index, second_index = 0, 0
    while first_index < len(firstList) and second_index < len(secondList):

        first_start, first_end = firstList[first_index][0], firstList[first_index][1]
        second_start, second_end = secondList[second_index][0], secondList[second_index][1]

        # no intersection 1
        if first_start > second_end:
            second_index += 1
            continue
        # no intersection 2
        if first_end < second_start:
            first_index += 1
            continue
        # intersections
        intersecs.append([max(first_start, second_start), min(first_end, second_end)])
        if first_end < second_end:
            first_index += 1
        elif first_end > second_end:
            second_index += 1
        else:
            first_index += 1
            second_index += 1
    return intersecs


print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

