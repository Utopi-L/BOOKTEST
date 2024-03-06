import torch_rbf as rbf
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.decomposition import PCA

# Defining an RBF network class

class MyDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x.size(0)

    def __getitem__(self, idx):
        x = self.x[idx]
        y = self.y[idx]
        return (x, y)


class Network(nn.Module):
    def __init__(self, layer_widths, layer_centres, basis_func):
        super(Network, self).__init__()
        self.rbf_layers = nn.ModuleList()
        self.linear_layers = nn.ModuleList()
        for i in range(len(layer_widths) - 1):
            self.rbf_layers.append(rbf.RBF(layer_widths[i], layer_centres[i], basis_func))
            self.linear_layers.append(nn.Linear(layer_centres[i], layer_widths[i + 1]))

    def forward(self, x):
        out = x
        for i in range(len(self.rbf_layers)):
            out = self.rbf_layers[i](out)
            out = self.linear_layers[i](out)
        return out

    def fit(self, x, y, epochs, batch_size, lr, loss_func):
        self.train()
        obs = x.size(0)
        trainset = MyDataset(x, y)
        trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True)
        optimiser = torch.optim.Adam(self.parameters(), lr=lr)
        epoch = 0
        while epoch < epochs:
            epoch += 1
            current_loss = 0
            batches = 0
            progress = 0
            for x_batch, y_batch in trainloader:
                batches += 1
                optimiser.zero_grad()
                y_hat = self.forward(x_batch)
                loss = loss_func(y_hat, y_batch)
                current_loss += (1 / batches) * (loss.item() - current_loss)
                loss.backward()
                optimiser.step()
                progress += y_batch.size(0)
                sys.stdout.write('\rEpoch: %d, Progress: %d/%d, Loss: %f      ' % \
                                 (epoch, progress, obs, current_loss))
                sys.stdout.flush()


# Generating a dataset for a given decision boundary

data = load_wine()
train = data.data
ex_test = data.target

ss = MinMaxScaler()
x = ss.fit_transform(train)
pca = PCA(n_components='mle')
train = pca.fit_transform(x)


ohe = OneHotEncoder()
test2D = np.expand_dims(ex_test, axis=1)
test = ohe.fit([[0], [1], [2]]).transform(test2D).toarray()

samples = len(train)
x = np.array(train)[:, [0, 1]]
y = np.array(test)

xmin = x.min(0)[0]
xmax = x.max(0)[0]
ymin = x.min(0)[1]
ymax = x.max(0)[1]

steps = 100
x_span = np.linspace(xmin, xmax, steps)
y_span = np.linspace(ymin, ymax, steps)

xx, yy = np.meshgrid(x_span, y_span)
values = np.append(xx.ravel().reshape(xx.ravel().shape[0], 1),
                   yy.ravel().reshape(yy.ravel().shape[0], 1),
                   axis=1)

tx = torch.from_numpy(x).float()
ty = torch.from_numpy(y).float()

# Instanciating and training an RBF network with the Gaussian basis function
# This network receives a 2-dimensional input, transforms it into a 40-dimensional
# hidden representation with an RBF layer and then transforms that into a
# 3-dimensional output/prediction with a linear layer

# To add more layers, change the layer_widths and layer_centres lists

layer_widths = [2, 3]
layer_centres = [40]
basis_func = rbf.gaussian

rbfnet = Network(layer_widths, layer_centres, basis_func)
rbfnet.fit(tx, ty, 10000, samples, 0.01, nn.BCEWithLogitsLoss())
rbfnet.eval()

# Plotting the ideal and learned decision boundaries
with torch.no_grad():
    preds_3D = (torch.sigmoid(rbfnet(torch.from_numpy(values).float()))).data.numpy()
    sampreds = (torch.sigmoid(rbfnet(torch.from_numpy(x).float()))).data.numpy()

# print(preds)
pred = np.expand_dims([pred.argmax() for pred in preds_3D], axis=1)
sampred = np.expand_dims([sampred.argmax() for sampred in sampreds], axis=1)

# print(test2D)
# print(sampred)
print('rbf 准确率为:', sum(sampred == np.expand_dims(ex_test, axis=1)) / len(y))

area_0 = values[np.where(pred[:, 0] == 0)[0]]
area_1 = values[np.where(pred[:, 0] == 1)[0]]
area_2 = values[np.where(pred[:, 0] == 2)[0]]

fig, ax = plt.subplots(figsize=(16, 8), nrows=1, ncols=2)
ax[0].scatter(x[ex_test == 0, 0], x[ex_test == 0, 1], c='dodgerblue')
ax[0].scatter(x[ex_test == 1, 0], x[ex_test == 1, 1], c='orange', marker='x')
ax[0].scatter(x[ex_test == 2, 0], x[ex_test == 2, 1], c='red', marker='*')
ax[0].set_title('real distribution')

ax[1].scatter(x[ex_test == 0, 0], x[ex_test == 0, 1], c='dodgerblue')
ax[1].scatter(x[ex_test == 1, 0], x[ex_test == 1, 1], c='orange', marker='x')
ax[1].scatter(x[ex_test == 2, 0], x[ex_test == 2, 1], c='red', marker='*')

ax[1].scatter(area_0[:, 0], area_0[:, 1], alpha=0.1, c='dodgerblue')
ax[1].scatter(area_1[:, 0], area_1[:, 1], alpha=0.1, c='orange')
ax[1].scatter(area_2[:, 0], area_2[:, 1], alpha=0.1, c='red')
ax[1].set_title('predict distribution')
plt.show()