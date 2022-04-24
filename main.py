# import the necessary packages
import argparse
import cv2 as cv
import CompareHistogram as ch
import CompareFeatures as cf
import Image_Diff as id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--first", required=True, help="first input image")
    ap.add_argument("-s", "--second", required=True, help="second")
    ap.add_argument("-m", "--mode", required=True, help="Mode")
    args = vars(ap.parse_args())

    # load the two input images
    imageA = cv.imread(args["first"])
    imageB = cv.imread(args["second"])

    # load mode of program
    mode = int(args["mode"])

    if mode == 0:
        ch.compareHistogram(imageA, imageB)
    elif mode == 1:
        cf.compareSIFT(imageA, imageB)
    elif mode == 2:
        id.image_differences(imageA, imageB)

    elif mode == 3:
        cf.Match(imageA, imageB)


    cv.waitKey(0)