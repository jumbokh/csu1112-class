### python3 downgrade from 3.10 to 3.9
```
sudo apt-get update

sudo add-apt-repository ppa:deadsnakes/ppa

apt list | grep python3.9

sudo apt install python3.9

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

sudo update-alternatives --config python3
```
