# weibo-ncov
get most recent data from weibo; The submodule is a reference for my project and the main function located at `userspider`

## configuration

*Note*: If you need to creat your own data cluster on your data storage note or just single machine. You need to establish momgodb or mysql database in the beginning. Two docker-version database compose file create by me could used as a example. Or if you don't need, just modify the `userspider/config.json`. The describtion file for configuration shows on that `userspider` folder. 

*Note*: 

## Usage
```
cd userspider
pip install -r requirements.txt
python spider.py
```