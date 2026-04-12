def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    H = len(image)
    W = len(image[0])
    cy = (H-1)/2
    cx = (W-1)/2
    radians = math.radians(angle_degrees)
    output = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            dy = i - cy
            dx = j - cx
            src_y = round(cy+dy*math.cos(radians)+dx*math.sin(radians))
            src_x = round(cx-dy*math.sin(radians)+dx*math.cos(radians))

            if 0 <= src_y <= H and 0 <= src_x <= W:
                output[i][j] = image[src_y][src_x]
            else:
                output[i][j] = 0

    return output