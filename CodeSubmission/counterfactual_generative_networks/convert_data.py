import numpy as np

def main():
    #load our unformatted data 
    normalload = np.load('data.npy', allow_pickle=True).item()
    #grab each from the dictionary
    test_image_ourdata = normalload.get('test_image')
    train_image_ourdata = normalload.get('train_image')
    test_label_ourdata = normalload.get('test_label')
    train_label_ourdata = normalload.get('train_label')

    #Format test images
    test_images = []
    rows = []
    col = []
    #for each entry
    for i in range(0, len(test_image_ourdata)):
        #for each of the 4096 values for each pixel
        for j in range(0, len(test_image_ourdata[i])):
            #if we've populated a column append it to the row
            if len(col) == 64:
                rows.append(col)
                col = []
            #convert grayscale to color by having r=g=b
            val = np.uint8(test_image_ourdata[i][j])
            col.append([val, val, val])
        #append column
        rows.append(col)
        col = []
        ##if done with rows, add the completed image to test_images
        if len(rows) == 64:
            test_images.append(rows)
            rows = []
    #reformat to be uint8
    test_images = np.array(test_images, dtype=np.uint8)
    #feed back into
    normalload['test_image'] = test_images

    #Format train images, same structure as above
    train_images = []
    rows = []
    col = []
    for i in range(0, len(train_image_ourdata)):
        for j in range(0, len(train_image_ourdata[i])):
            if len(col) == 64:
                rows.append(col)
                col = []
            val = np.uint8(train_image_ourdata[i][j])
            col.append([val, val, val])
        rows.append(col)
        col = []
        if len(rows) == 64:
            train_images.append(rows)
            rows = []

    train_images = np.array(train_images, dtype=np.uint8)
    normalload['train_image'] = train_images

    #Format test gray images (same structure as above)
    test_gray_images = []
    rows = []
    col = []
    for i in range(0, len(test_image_ourdata)):
        for j in range(0, len(test_image_ourdata[i])):
            if len(col) == 64:
                rows.append(col)
                col = []
            val = np.uint8(test_image_ourdata[i][j])
            col.append(val)
        rows.append(col)
        col = []
        if len(rows) == 64:
            test_gray_images.append(rows)
            rows = []
    test_gray_images = np.array(test_gray_images, dtype=np.uint8)
    normalload['test_gray'] = test_gray_images

    #Format test labels
    test_labels = []
    #grab each value as an int8
    for i in range(0, len(test_label_ourdata)):
        test_labels.append(np.int8(test_label_ourdata[i]))
    test_labels = np.array(test_labels, dtype=np.int8)
    #squeeze to match our goal data
    test_labels = np.squeeze(test_labels)
    normalload['test_label'] = test_labels

    #Format train labels
    train_labels = []
    #grab each value as an int8
    for i in range(0, len(train_label_ourdata)):
        train_labels.append(np.int8(train_label_ourdata[i]))
    train_labels = np.array(train_labels, dtype=np.int8)
    #squeeze to match our goal data
    train_labels = np.squeeze(train_labels)
    normalload['train_label'] = train_labels
    np.save('chinese_MNIST_data', normalload)

main()
