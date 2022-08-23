# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
from skimage.metrics import structural_similarity as ssim


def demo_on_sample1():
    file_name = 'Sample3.JPG'
    image_test = cv2.imread(file_name)
    grey_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
    histogram_test = cv2.calcHist([grey_test], [0],
                                  None, [256], [0, 256])

    target_width = image_test.shape[1]
    target_height = image_test.shape[0]
    target_size = (target_width, target_height)

    print("DEMO SAMPLE1")
    print("Image name: {}, shape: {}".format(file_name, image_test.shape))
    for i in range(1, 9):
        # data image
        file_name = 'Sample3_Neg{}.jpg'.format(i)
        image_data = cv2.imread(file_name)

        # resize image
        image_data_resized = cv2.resize(image_data, target_size)

        grey_data = cv2.cvtColor(image_data_resized, cv2.COLOR_BGR2GRAY)
        histogram_data = cv2.calcHist([grey_data], [0],
                                      None, [256], [0, 256])
        c = 0

        # Euclidean Distance between data and test
        i = 0
        while i < len(histogram_test) and i < len(histogram_data):
            c += (histogram_test[i] - histogram_data[i]) ** 2
            i += 1
        c = c ** (1 / 2)
        s = ssim(grey_test, grey_data)
        print("Image name: {}, shape: {}".format(file_name, image_test.shape))
        print("c = {}, s = {}".format(c, s))


# Images of colourful apple
def demo_on_sample2():
    file_name = 'test.jpg'
    image_test = cv2.imread(file_name)
    grey_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
    histogram_test = cv2.calcHist([grey_test], [0],
                                  None, [256], [0, 256])

    target_width = image_test.shape[1]
    target_height = image_test.shape[0]
    target_size = (target_width, target_height)
    print("DEMO SAMPLE2")
    print("Image name: {}, shape: {}".format(file_name, image_test.shape))

    for i in range(1, 4):
        # data image
        file_name = 'data{}.jpg'.format(i)
        image_data = cv2.imread(file_name)

        # resize image
        image_data_resized = cv2.resize(image_data, target_size)

        grey_data = cv2.cvtColor(image_data_resized, cv2.COLOR_BGR2GRAY)
        histogram_data = cv2.calcHist([grey_data], [0],
                                      None, [256], [0, 256])
        c = 0

        # Euclidean Distance between data and test
        i = 0
        while i < len(histogram_test) and i < len(histogram_data):
            c += (histogram_test[i] - histogram_data[i]) ** 2
            i += 1
        c = c ** (1 / 2)
        s = ssim(grey_test, grey_data)
        print("Image name: {}, shape: {}".format(file_name, image_test.shape))
        print("c = {}, s = {}".format(c, s))


def demo_resize():
    src = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)

    # percent by which the image is resized
    scale_percent = 50

    # calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(src, dsize)

    cv2.imwrite('conv.jpg', output)


def compare_image(expected_image_path, actual_image_path):
    similar = False

    image_test = cv2.imread(expected_image_path)
    grey_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
    histogram_test = cv2.calcHist([grey_test], [0],
                                  None, [256], [0, 256])

    target_width = image_test.shape[1]
    target_height = image_test.shape[0]
    target_size = (target_width, target_height)
    print("DEMO IMAGE COMPARISON")
    print("Image name: {}, shape: {}".format(expected_image_path, image_test.shape))

    image_data = cv2.imread(actual_image_path)

    # resize image
    image_data_resized = cv2.resize(image_data, target_size)

    grey_data = cv2.cvtColor(image_data_resized, cv2.COLOR_BGR2GRAY)
    histogram_data = cv2.calcHist([grey_data], [0],
                                  None, [256], [0, 256])
    c = 0

    # Euclidean Distance between data and test
    i = 0
    while i < len(histogram_test) and i < len(histogram_data):
        c += (histogram_test[i] - histogram_data[i]) ** 2
        i += 1
    c = c ** (1 / 2)
    s = ssim(grey_test, grey_data)
    print("Image name: {}, shape: {}".format(actual_image_path, image_test.shape))
    print("c = {}, s = {}".format(c, s))

    if c == 0 and s == 1:
        similar = True

    return similar


if __name__ == '__main__':
    demo_on_sample1()
    demo_on_sample2()
    demo_resize()
    image_path1 = 'Sample3.JPG'
    image_path2 = 'Sample3_Neg1.JPG'
    print("Comparing image {} and {}.".format(image_path1, image_path2))
    IsSimilar = compare_image(image_path1, image_path2)
    if IsSimilar:
        print("They are similar")
    else:
        print("They are different")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
