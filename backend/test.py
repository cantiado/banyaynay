import config
import model
import cv2
import os
import numpy as np

train_imgs_path = os.path.join(config.DIR_TRAIN, config.DIR_IMG)
train_labs_path = os.path.join(config.DIR_TRAIN, config.DIR_LAB)

train_imgs = model.load_images(train_imgs_path)
train_labs = model.load_images(train_labs_path)

test_imgs_path = os.path.join(config.DIR_TEST, config.DIR_IMG)
test_labs_path = os.path.join(config.DIR_TEST, config.DIR_LAB)

test_imgs = model.load_images(test_imgs_path)
test_labs = model.load_images(test_labs_path)

# cv2.imshow("image", train_imgs[0])
# cv2.imshow("ref", train_labs[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

mean, cov = model.train(train_imgs, train_labs, True)
conf_matrix = model.test(test_imgs, test_labs, mean, cov, 0.75, True)
results = model.classify(test_imgs, mean, cov, 0.75)

for i, res in enumerate(results):
    cv2.imwrite(f"res-{i}.jpg", res)
    cv2.imshow(f"res-{i}", res)
cv2.waitKey(0)
cv2.destroyAllWindows()