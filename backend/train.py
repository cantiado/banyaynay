import json
import os
import matplotlib.pyplot as plt
import numpy as np

import src.config as config
import src.model as model

# Training
train_imgs_path = os.path.join(config.DIR_TRAIN, config.DIR_IMG)
train_labs_path = os.path.join(config.DIR_TRAIN, config.DIR_LAB)

train_imgs = model.load_images(train_imgs_path)
train_labs = model.load_images(train_labs_path)

print("=== Training ===")
mean, cov = model.train(train_imgs, train_labs, True)
print()

# Validation (Find best threshold which yeilds equal error rate, i.e., FP==FN)
val_imgs_path = os.path.join(config.DIR_VAL, config.DIR_IMG)
val_labs_path = os.path.join(config.DIR_VAL, config.DIR_LAB)

val_imgs = model.load_images(val_imgs_path)
val_labs = model.load_images(val_labs_path)

thresholds = np.linspace(0, 1, 101)
performance = {}

print("=== Validation ===")
for threshold in thresholds:
    print("Threshold:", threshold)
    conf_matrix = model.evaluate(
        val_imgs, val_labs, mean, cov, threshold, True)
    acc = (conf_matrix[0] + conf_matrix[3])/sum(conf_matrix)
    far = conf_matrix[1]/sum(conf_matrix)
    frr = conf_matrix[2]/sum(conf_matrix)
    performance[threshold] = {"acc": acc, "far": far, "frr": frr}
    print()

t_star = min(thresholds, key=lambda t: abs(
    performance[t]["far"] - performance[t]["frr"]))

plt.plot(thresholds, [performance[t]["far"]
         for t in thresholds], label="FAR", c="r")
plt.plot(thresholds, [performance[t]["frr"]
         for t in thresholds], label="FRR", c="b")
plt.vlines(t_star, 0, 1, "k", "dashed", "ERR")
plt.title("Error rate vs. Threshold")
plt.xlabel("Threshold")
plt.ylabel("Error rate")
plt.legend()
plt.savefig(os.path.join(config.DIR_BIN, "error_rate.png"))
plt.show()

plt.plot(thresholds, [performance[t]["acc"] for t in thresholds], c="k")
plt.title("Accuracy vs. Threshold")
plt.xlabel("Threshold")
plt.ylabel("Accuracy")
plt.savefig(os.path.join(config.DIR_BIN, "accuracy.png"))
plt.show()

with open(os.path.join(config.DIR_BIN, "parameters.json"), "w") as fout:
    json.dump({"mean": mean.tolist(), "cov": cov.tolist(), "threshold": t_star}, fout)
