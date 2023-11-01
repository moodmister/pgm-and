def read_pgm(filename):
  with open(filename, 'r') as file:
    header = []
    width = 0
    height = 0
    max_val = 0
    data = []
    data_started = False
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0 and line != 'P2':
            raise ValueError("Invalid PGM format (P2 expected).")
        elif i == 0 and line == 'P2':
            continue

        if line.startswith('#'):
            continue

        if not header:
            header = line.split()
            width, height = int(header[0]), int(header[1])
        elif not max_val:
            max_val = int(line)
        else:
            if not data_started:
                data_started = True
            data.extend([int(value) for value in line.split()])

    return width, height, max_val, data

def write_pgm(filename, width, height, max_val, data):
    with open(filename, 'w') as file:
        file.write(f'P2\n')
        file.write(f'{width} {height}\n')
        file.write(f'{max_val}\n')
        for i, value in enumerate(data):
            file.write(str(value))
            if (i + 1) % width == 0:
                file.write('\n')
            else:
                file.write('  ')

def perform_logical_and(image1_path, image2_path, x1, y1, x2, y2):
    # Read the PGM images
    width1, height1, max_val1, data1 = read_pgm(image1_path)
    width2, height2, max_val2, data2 = read_pgm(image2_path)

    # Ensure the images have the same dimensions
    if width1 != width2 or height1 != height2:
        raise ValueError("The images must have the same dimensions.")

    if not 0 <= y1 < height1 or not 0 < y2 < height2:
        raise Exception("Out of bounds")
    
    if not 0 <= x1 < width1 or not 0 <= x1 < width2:
        raise Exception("Out of bounds")

    # Crop the images to the specified coordinates and perform the logical AND operation
    for y in range(y1, y2):
        for x in range(x1, x2):
            idx = y * width1 + x
            data1[idx] = data1[idx] & data2[idx]

    # Save the result image
    result_image_path = "result.pgm"
    write_pgm(result_image_path, width1, height1, max_val1, data1)

    print("Logical AND operation completed and saved as 'result.pgm'.")

if __name__ == "__main__":
    image1_path = "image1.pgm"  # Replace with the path to your first P2 PGM image
    image2_path = "image2.pgm"  # Replace with the path to your second P2 PGM image
    # Define the coordinates (0 <= x1,x2 < 27), (0 <= y1,y2 < 7)
    x1, y1 = 2, 2
    x2, y2 = 6, 6

    perform_logical_and(image1_path, image2_path, x1, y1, x2, y2)
