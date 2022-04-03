#!/usr/bin/env python
import cv2
import numpy as np

if __name__ == '__main__' :

    # Read source image.
    im_src = cv2.imread('images/modelSoccerField.jpg')

    # Four corners of the book in source image
    pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]], np.float32)

    # Read destination image.
    im_dst = cv2.imread('images/input1.png')

    # Four corners of the book in destination image.
    pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]], np.float32)

    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    #resmatrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
    # no difference between using `findHomography` and `getPerspectiveTransform` if you're using 4 points as input. 

    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
    #im_out2 = cv2.warpPerspective(im_src, resmatrix, (im_dst.shape[1],im_dst.shape[0]))

    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
    # cv2.imshow("Got perspective Source Image", im_out2)
    cv2.waitKey(0)