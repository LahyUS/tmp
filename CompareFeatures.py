import cv2 as cv
import cv2
import matplotlib.pyplot as plt

def compareSIFT(img1, img2):
    # Detect the keypoints using SIFT Detector, compute the descriptors
    detector = cv.SIFT_create()
    keypoint_1, desc_1 = detector.detectAndCompute(img1, None)
    keypoint_2, desc_2 = detector.detectAndCompute(img2, None)

    # Show number of each keypoint
    print("Keypoints 1ST image: " + str(len(keypoint_1)))
    print("Keypoints 2NS image: " + str(len(keypoint_2)))

    # Match the keypoints using KNN algorithm
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(desc_1, desc_2, k=2)

    # Keep crucial features which have small distance
    good_points = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:
            good_points.append(m)
    number_keypoint = 0
    if len(keypoint_1) <= len(keypoint_2):
        number_keypoint = len(keypoint_1)
    else:
        number_keypoint = len(keypoint_2)

    # Get result matching image
    result = cv.drawMatches(img1, keypoint_1, img2, keypoint_2, good_points, None)
    cv.imshow("Result", cv.resize(result, None, fx=0.4, fy=0.8))
    print("Good Matches: ", len(good_points))
    print("How good it's the match: ", len(good_points) / number_keypoint * 100, "%")

def Match(img1, img2):
    # Detect the keypoints using SIFT Detector, compute the descriptors
    detector = cv.SIFT_create()
    keypoint_1, desc_1 = detector.detectAndCompute(img1, None)
    keypoint_2, desc_2 = detector.detectAndCompute(img2, None)

    # feature matching
    bf = cv2.BFMatcher(cv.NORM_L1, crossCheck=True)

    matches = bf.match(desc_1, desc_2)
    matches = sorted(matches, key=lambda x: x.distance)

    img3 = cv.drawMatches(img1, keypoint_1, img2, keypoint_2, matches[:50], img2, flags=2)
    plt.imshow(img3), plt.show()