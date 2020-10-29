# norlist-bbox-tool

![Main page](images/main_page.jpg)

### Installation
```sh
git clone https://github.com/quanyshh/norlist-bbox-tool.git
cd norlist-bbox-tool
python -m venv venv
pip install -r requirements.txt
```

### Requirements
- python >= 3.6

### Run
Linux: 
- On server:
```sh
NORLIST_TOOL_RUN_TYPE='s' python app.py
```

- On local pc:
```sh
NORLIST_TOOL_RUN_TYPE='r' python app.py
```
Windows:
- Powershell:
```sh
Set-Variable -Name "NORLIST_TOOL_RUN_TYPE" -Value "r" 
python app.py
```
-cmd:
```sh
SET NORLIST_TOOL_RUN_TYPE='r'
python app.py
```
