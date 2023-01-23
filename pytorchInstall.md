##
```
今天要教大家安裝敵方陣營的深度學習 PyTorch, 其實如果有 NVIDIA GPU 的 Windows/Linux 系統, 記得照著官網打那一行就好了。所以這裡特別討論對 M1/M2 系的 Mac, 要感受 GPU 做深度學習的快感, 請參考華聖頓大學 (在聖路易士的) Jeff Heaton 給的指引:
https://github.com/....../pytorch-install-aug-2022.ipynb
簡單說是要做幾件事:
1. 安裝 miniconda, M1/M2 系的 Mac 記得要選 ARM64 版本
2. 安裝 jupyter (Jupyter Notebook)
3. (重點) 把 Heaton 老師的 GitHub "install" 中的  torch-conda-nightly.yml 放到你準備下安裝指令的資料夾 (你可以用純文字編輯器看這個 .yml 內容, 會發現就是指示去那個 channel, 安裝哪些套件)
4. 下那一行安裝指令:
conda env create -f torch-conda-nightly.yml -n torch
5. 進入 (activate) 新建的 torch 虛擬環境, 讓 Jupyter Notebook 看得到這個環境:
python -m ipykernel install --user --name pytorch --display-name "Python 3.9 (pytorch)"
這個安裝文件用 Jupyter Notebook 打開的話, 還可順便幫忙檢查是否安裝成功。
by 蔡炎龍老師
```
* [T81-558: Applications of Deep Neural Networks](https://github.com/jumbokh/csu1112-class/blob/main/notebooks/manual_setup.ipynb)
