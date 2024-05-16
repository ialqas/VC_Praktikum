import copy
import math

import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import sys
import math

from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns[0:1]:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
        print(ann['area'])
    ax.imshow(img)

    print(anns[0])



def sobel_edge_detector(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Sobel operator
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate gradient magnitude
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Apply a threshold to identify edges
    threshold = 450
    edges = magnitude > threshold

    return edges.astype(np.uint8)
def canny_edge_detector(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Defining all the parameters
    t_lower = 650  # Lower Threshold
    t_upper = 850  # Upper threshold
    aperture_size = 5  # Aperture size
    L2Gradient = False  # Boolean

    # Applying the Canny Edge filter
    # with Aperture Size and L2Gradient
    edge = cv2.Canny(image, t_lower, t_upper,
                     apertureSize=aperture_size,
                     L2gradient=L2Gradient)

    return edge


def ransac_vanishing_point(lines, num_ransac_iter=2000, threshold_inlier=5):
    """Estimate vanishing point using Ransac.

    Parameters
    ----------
    edgelets: tuple of ndarrays
        (locations, directions, strengths) as computed by `compute_edgelets`.
    num_ransac_iter: int
        Number of iterations to run ransac.
    threshold_inlier: float
        threshold to be used for computing inliers in degrees.

    Returns
    -------
    best_model: ndarry of shape (3,)
        Best model for vanishing point estimated.

    Reference
    ---------
    Chaudhury, Krishnendu, Stephen DiVerdi, and Sergey Ioffe.
    "Auto-rectification of user photos." 2014 IEEE International Conference on
    Image Processing (ICIP). IEEE, 2014.
    """
   # locations, directions, strengths = edgelets
   # lines = edgelet_lines(edgelets)

    num_pts = lines.shape[0]
    strength = [np.linalg.norm(line[0][0:2] - line[0][2::]) for line in lines]

    arg_sort = np.argsort(strength)
    first_index_space = arg_sort[:num_pts // 5]
    second_index_space = arg_sort[:num_pts // 2]

    best_model = None
    best_votes = np.zeros(num_pts)

    for ransac_iter in range(num_ransac_iter):
        ind1 = np.random.choice(first_index_space)
        ind2 = np.random.choice(second_index_space)

        l1 = lines[ind1][0]
        l2 = lines[ind2][0]

        current_model = np.cross(l1, l2)

        if np.sum(current_model**2) < 1 or current_model[2] == 0:
            # reject degenerate candidates
            continue

        current_votes = compute_votes(
            edgelets, current_model, threshold_inlier)

        if current_votes.sum() > best_votes.sum():
            best_model = current_model
            best_votes = current_votes
            logging.info("Current best model has {} votes at iteration {}".format(
                current_votes.sum(), ransac_iter))

    return best_model
def line_detection_lsd(edge_image, raw_image):
    edge_img = copy.deepcopy(edge_image)
    raw_img = copy.deepcopy(raw_image)
    # Create default parametrization LSD
    lsd = cv2.createLineSegmentDetector(0)
    # Detect lines in the image
    lines = lsd.detect(edge_img)[0]# Position 0 of the returned tuple are the detected lines
    #get horizontal and vertical lines
    horizon_lines_idx = []
    vertical_lines_idx = []
    for idx in range(lines.shape[0]):
        x1, y1, x2, y2 = lines[idx][0]
        slope = abs((y2 - y1) / (x2 - x1 + 0.0001))
        if slope < 0.5:
            horizon_lines_idx.append(idx)
        if slope > 5:
            vertical_lines_idx.append(idx)


    horizon_lines = lines[horizon_lines_idx]
    vertical_lines = lines[vertical_lines_idx]

  #  vp1 = ransac_vanishing_point(horizon_lines, num_ransac_iter=2000,
          #                       threshold_inlier=5)
   # print(vp1)
  #  vp1 = reestimate_model(vp1, edgelets1, threshold_reestimate=5)
  #  vis_model(image, vp1)  # Visualize the vanishing point model


    # Draw detected horizon lines in the image
    raw_img = copy.deepcopy(raw_image)
    drawn_img_h = lsd.drawSegments(raw_img, horizon_lines)
    plt.figure(figsize=(20, 20))
    plt.imshow(drawn_img_h)
    plt.axis('off')
    plt.show()

    # Draw detected vertical lines in the image
    raw_img = copy.deepcopy(raw_image)
    drawn_img_v = lsd.drawSegments(raw_img, vertical_lines)
    plt.figure(figsize=(20, 20))
    plt.imshow(drawn_img_v)
    plt.axis('off')
    plt.show()


    # get vanishing point

    return edge_img
def line_lsd(edge_image, raw_image):
    img = copy.deepcopy(raw_image)
    middlex = img.shape[1] / 2
    middley = img.shape[0] / 2

    def gaussianweights(image):
        newarr = [[0 for i in range(image.shape[1])] for j in range(image.shape[0])]
        for i in range(image.shape[1]):
            for j in range(image.shape[0]):
                x, y = i, j
                filtered = np.exp(
                    ((x - middlex) ** 2) / ((middlex ** 2) / 2) + ((y - middley) ** 2) / ((middley ** 2) / 2))
                newarr[j][i] = image[j][i] * filtered
        return newarr

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    weighted_img = gaussianweights(img_gray)
    filtered_img = cv2.filter2D(weighted_img, -1, np.array(
        [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, -24, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))

    dst = cv2.Canny(filtered_img, 600, 800, None, 3)

    lines = cv2.HoughLines(dst, 1, np.pi / 180, 100)
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

   # cv2.imshow("Hough Image", img)
    plt.figure(figsize=(20, 20))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
def line_detection(edge_image, raw_image):

    edge_img = copy.deepcopy(edge_image)
    lines = cv2.HoughLinesP(edge_img, rho = 1,theta = 1*np.pi/180,threshold = 60,minLineLength = 50,maxLineGap = 50)
    lines1 = cv2.HoughLines(edge_img, rho = 1,theta = 45*np.pi/180, threshold  = 180)#50, 100, 50
    for line in lines:

        cv2.line(edge_img, (line[0][0], line[0][1]), (line[0][2], line[0][3]), (255, 255, 255), 1)
    plt.figure(figsize=(20, 20))
    plt.imshow(edge_img)
    plt.axis('off')
    plt.show()


    #get the parallel line from the bottom and the top
    x_min_arg = np.where(lines[:,0,0]<=lines[:,0,0].min()+3)[0]
    x_min_y_min_arg = lines[x_min_arg,0,1].argmin()
    x_min_y_max_arg = lines[x_min_arg, 0, 1].argmax()
    x_max_line = lines[x_min_arg[x_min_y_min_arg]]
    x_min_line = lines[x_min_arg[x_min_y_max_arg]]

    #get the vertical line from the bottom and the top
    arg = []
    for idx in range(lines.shape[0]):
        if abs(lines[idx][0][0]-lines[idx][0][2]) < 20:
            arg.append(idx)
    ver_lines = lines[arg]
    y_min_arg = np.where(ver_lines[:,0,0]==ver_lines[:,0,0].min())[0]
    y_max_arg = np.where(ver_lines[:, 0, 0] == ver_lines[:, 0, 0].max() )[0]

    y_min_line = ver_lines[y_min_arg][0]
    y_max_line =ver_lines[y_max_arg][0]

    contour_img = copy.deepcopy(edge_image)
    cv2.line(contour_img, (x_min_line[0][0], x_min_line[0][1]), (x_min_line[0][2], x_min_line[0][3]), (255, 255, 255), 5)
    cv2.line(contour_img, (x_max_line[0][0], x_max_line[0][1]), (x_max_line[0][2], x_max_line[0][3]), (255, 255, 255),
             5)
    cv2.line(contour_img, (y_min_line[0][0], y_min_line[0][1]), (y_min_line[0][2], y_min_line[0][3]), (255, 255, 255),
             5)
    cv2.line(contour_img, (y_max_line[0][0], y_max_line[0][1]), (y_max_line[0][2], y_max_line[0][3]), (255, 255, 255),
             5)

    plt.figure(figsize=(20, 20))
    plt.imshow(contour_img)
    plt.axis('off')
    plt.show()

    rotate_img = rotate_image(contour_img, raw_image,  x_min_line, x_max_line, y_min_line, y_max_line)



    return edge_img, rotate_img
def get_joint_point(line1, line2):
    o1 = np.array((line1[0], line1[1]))
    p1 = np.array((line1[2], line1[3]))
    o2 = np.array((line2[0], line2[1]))
    p2 = np.array((line2[2], line2[3]))

 #   x = o2 - o2
 #   d1 = p1 - o1
 #   d2 = p2 - o2
 #   cross = d1[0]*d2[1] - d2[0]*d1[1]
 #   t1 = (x[0]*d2[1] - x[1]*d2[0])/cross
 #   r = o1+d1*t1
    a1 = p1[1] - o1[1]
    b1 = o1[0] - p1[0]
    c1 = a1 * o1[0] + b1 * o1[1]
    a2 = p2[1] - o2[1]
    b2 = o2[0] - p2[0]
    c2 = a2 * o2[0] + b2 * o2[1]
    det = a1*b2 - a2*b1
    x = (b2 * c1 - b1 * c2)/det
    y = (a1 * c2 - a2 * c1) / det

    return np.array((x, y))

def rotate_image(contour_image, image, x_max_line, x_min_line, y_min_line, y_max_line):

    # Read the image using OpenCV
 #   image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Extracting height and width from image shape
    height = image.shape[0]
    width = image.shape[1]

    jp_xmin_ymin = get_joint_point(x_min_line[0], y_min_line[0])
    jp_xmax_ymin = get_joint_point(x_min_line[0], y_max_line[0])
    jp_xmin_ymax = get_joint_point(x_max_line[0], y_min_line[0])
    jp_xmax_ymax = get_joint_point(x_max_line[0], y_max_line[0])

  #  pts1 = np.float32([jp_xmin_ymin, jp_xmax_ymax, jp_xmax_ymin])
  #  pts2 = np.float32([[3, 3], [width-3, height-3], [width-3, 3]])
    pts1 = np.float32([jp_xmin_ymin, jp_xmax_ymax, jp_xmax_ymin, jp_xmin_ymax])
    pts2 = np.float32([[3, 3], [width - 3, height - 3], [width - 3, 3],[ 3, height - 3]])

    # using cv2.getRotationMatrix2D() to get
    # the rotation matrix
    rotate_matrix = cv2.getPerspectiveTransform(pts1,pts2)
   # rotate_matrix = cv2.getAffineTransform(pts1, pts2)

    # rotate the image using cv2.warpAffine 180
    # degree anticlockwise
   # rotated_image = cv2.warpAffine(
   #     src=image, M=rotate_matrix, dsize=(width, height))
    rotated_image = cv2.warpPerspective(
        src=image, M=rotate_matrix, dsize=(width, height))
    plt.figure(figsize=(20, 20))
    plt.imshow(rotated_image)
    plt.axis('off')
    plt.show()
    return rotated_image


if __name__ == '__main__':
    img_path = './imgtest.jpg'
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20, 20))
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    #edge detection
  #  edge_image = sobel_edge_detector(img_path)
  #  plt.figure(figsize=(20, 20))
  #  plt.imshow(edge_image)
  #  plt.axis('off')
  #  plt.show()
    # canny edge detection works better
    edge_image = canny_edge_detector(img_path)
    plt.figure(figsize=(20, 20))
    plt.imshow(edge_image)
    plt.axis('off')
    plt.show()


   # line_image, rotate_image = line_detection(edge_image, image)
    line_image = line_detection_lsd(edge_image, image)

    # canny edge detection
 #   edge_image = canny_edge_detector(img_path)
 #   plt.figure(figsize=(20, 20))
 #   plt.imshow(edge_image)
 #   plt.axis('off')
 #   plt.show()
 #   line_image = line_detection(edge_image)



    sys.path.append("..")

    sam_checkpoint = "sam_vit_h_4b8939.pth"
    model_type = "vit_h"

  #  device = "cuda"

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
  #  sam.to(device=device)

    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(rotate_image)
    print(len(masks))
    print(masks[0].keys())

    plt.figure(figsize=(20, 20))
    plt.imshow(rotate_image)
    show_anns(masks)
    plt.axis('off')
    plt.show()
