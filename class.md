```
from google.colab import drive
drive.mount('/content/gdrive') # 此處需要登入google帳號
```
* %cd /content/gdrive/MyDrive/Colab\ Notebooks
### 互動
```
from ipywidgets import interact_manual
interact_manual(bmi_cal, h="請輸入你的身高(公分)",
                w="請輸入你的體重(公斤)");
```
