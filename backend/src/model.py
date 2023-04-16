import cv2
import json
import numpy as np
import os
from pprint import pprint


def load_images(dir_name):
    images = []
    for fname in os.listdir(dir_name):
        fpath = os.path.join(dir_name, fname)
        if os.path.isfile(fpath):
            images.append(cv2.imread(fpath))
    return images


def load_params(fpath):
    with open(fpath, "r") as fin:
        params = json.load(fin)
    params["mean"] = np.array(params["mean"])
    params["cov"] = np.array(params["cov"])
    return params


def chromatic(bgr):
    total = np.sum(bgr)
    if total == 0:
        return np.array([0, 0])
    r = bgr[2]/total
    g = bgr[1]/total
    return np.array([r, g])


def sample_mean(n, prev_mean, new_X):
    if n == 0:
        return new_X
    return (1/(n + 1))*(n*prev_mean + new_X)


def sample_cov(n, prev_mean, prev_cov, new_X):
    if n == 0:
        return prev_cov
    phi = (prev_mean - new_X).reshape((len(new_X), 1))
    return (1/n)*((n - 1)*prev_cov + (n/(n + 1))*phi@phi.T)


def dnorm(x, mean, cov_det, cov_inv):
    phi = (x - mean).reshape((len(x), 1))
    return (2*np.pi)**(-len(x)/2) * (1/np.sqrt(cov_det)) * np.exp(-0.5*phi.T@cov_inv@phi)


def train(images, labels, verbose=False):
    n = 0
    mu_hat = np.zeros((2,))
    sigma_hat = np.zeros((2, 2))
    for file_i in range(len(images)):
        image = images[file_i]
        label = labels[file_i]
        print(f"{file_i + 1}/{len(images)} Images")
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                if np.any(label[row, col]):
                    pixel = chromatic(image[row, col])
                    sigma_hat = sample_cov(n, mu_hat, sigma_hat, pixel)
                    mu_hat = sample_mean(n, mu_hat, pixel)
                    n += 1
        if verbose:
            print(f"Sample mean:", mu_hat)
            print(f"Sample covariance:")
            pprint(sigma_hat)
    return mu_hat, sigma_hat


def evaluate(images, labels, mean, cov, threshold, verbose=False):
    tp, fp, fn, tn = 0, 0, 0, 0
    cov_det = np.linalg.det(cov)
    cov_inv = np.linalg.inv(cov)
    norm = 1/(2*np.pi*np.sqrt(cov_det))
    for file_i in range(len(images)):
        image = images[file_i]
        label = labels[file_i]
        print(f"{file_i + 1}/{len(images)} Images")
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                pixel = chromatic(image[row, col])
                likelihood = dnorm(pixel, mean, cov_det, cov_inv)[0, 0]
                if likelihood > threshold*norm:
                    if np.any(label[row, col]):
                        tp += 1
                    else:
                        fp += 1
                else:
                    if np.any(label[row, col]):
                        fn += 1
                    else:
                        tn += 1
        if verbose:
            print(f"(TP, FP, FN, TN): {(tp, fp, fn, tn)}", end="\t")
            print(f"Accuracy: {(tp + tn)/(tp + fp + fn + tn)}")
    return tp, fp, fn, tn


def classify(images, mean, cov, threshold, silhouette=False):
    results = []
    cov_det = np.linalg.det(cov)
    cov_inv = np.linalg.inv(cov)
    norm = 1/(2*np.pi*np.sqrt(cov_det))
    for image in images:
        result = np.zeros(image.shape, dtype=np.uint8)
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                pixel = chromatic(image[row, col])
                likelihood = dnorm(pixel, mean, cov_det, cov_inv)[0, 0]
                if likelihood > threshold*norm:
                    if silhouette:
                        result[row, col] = [255, 255, 255]
                    else:
                        result[row, col] = image[row, col]
                    # print(image[row, col], result[row, col])
                # else:
                #     result[row, col] = [0, 0, 0]
        results.append(result)
    return results
