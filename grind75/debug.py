image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 0
sc = 0
color = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]


def floodFill(image, sr, sc, color):
    startingpx = image[sr][sc]
    if startingpx == color:
        return

    try:
        if image[sr-1][sc] == startingpx:
            image[sr-1][sc] = color
    except IndexError:
        pass
    try:
        if image[sr+1][sc] == startingpx:
            image[sr+1][sc] = color
    except IndexError:
        pass

    image[sr][sc] = color
    return image


print(floodFill(image, sr, sc, color))
