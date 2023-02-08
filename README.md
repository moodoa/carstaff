# carstaff
在 partslink24 蒐集車子相關零件資訊

![alt text](https://media.gq.com.tw/photos/5dbc3c0002d4200008d87173/master/w_1600%2Cc_limit/2018092059043513.jpg)

## main.py
* 輸入指定車子品牌，程式自動蒐集該品牌所有車型以及其相對應的引擎和變速箱型號。
* 目前只支援 Jaguar/Land rover。

## Requirements
python 3

## Usage

`python main.py`

```
if __name__ == "__main__":
    services = {0:"jaguar_parts", 1:"landrover_parts", }
    select = input("你想找哪款車？0: JAGUAR, 1:LAND ROVER")
    staff = CARSTAFF(services[int(select)])
    staff.main()

```
## Installation
`pip install -r requriements.txt`。
