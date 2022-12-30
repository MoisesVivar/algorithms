import numpy
import numpy as np
import cv2

#img = cv2.imread("images/2.png")
img = np.zeros((255, 255), dtype=np.uint8)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Please enter the starting pixel coordinates: ")
x, y = input().split()
print("Please enter a pixel color in RGB")
r, g, b = input().split()


def fill_connected_area(_img: np.ndarray, coordinates: tuple, color: np.ndarray):

    def get_neighbours(pixel: tuple):
        px, py = pixel
        possible_neighbours = [(px-1, py), (px+1, py), (px, py-1), (px, py+1)]
        neighbours = []
        for neighbour in possible_neighbours:
            nx, ny = neighbour
            if 0 <= nx < _img.shape[0] and 0 <= ny < _img.shape[1] and _img[nx][ny] == _img[px][py]:
                neighbours.append(neighbour)
        return neighbours

    queue = [coordinates]
    pixels_to_paint = []
    while queue:
        cur_pixel = queue.pop(0)
        pixels_to_paint.append(cur_pixel)
        for neighbour in get_neighbours(cur_pixel):
            if neighbour not in pixels_to_paint and neighbour not in queue:
                queue.append(neighbour)

    for p in pixels_to_paint:
        _img[p[0]][p[1]] = color


fill_connected_area(img, (int(x), int(y)), np.array([int(r), int(g), int(b)], dtype=np.uint8))

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
