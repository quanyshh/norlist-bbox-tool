from browser import document, ajax, bind, console
import json

def on_complete(req):
  pass
  # console.log(req.responseText);

@bind("#get_user_info", "click")
def get_user_info(ev):
  req = ajax.Ajax()
  req.bind('complete', on_complete)
  req.open('GET', '172.16.3.86:8080/')
  sel = document['user_id'].options
  selected = [option.value for option in sel if option.selected]
  console.log(selected[0])
  req.send()