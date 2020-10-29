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
For production release:
```sh
NORLIST_TOOL_RUN_TYPE='s' python app.py
```

For development:
```sh
NORLIST_TOOL_RUN_TYPE='r' python app.py
```

