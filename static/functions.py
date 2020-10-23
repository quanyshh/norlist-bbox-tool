from browser import document, ajax, bind
import json

def display_increment(response):
  document["name"].value = response.text
  print('display_increment print statement here')

def send_to_server(ev):
  """Get the predicted probability."""

  print('send_to_server print statement here')

  req = ajax.ajax()
  req.bind('complete', display_increment)
  req.open('POST', '/increment_on_server', True)
  req.set_header('content-type','application/json')

  data = json.dumps(
    {'package_to_server': document['message'].value}
    )
  req.send(data)


document["asd"].bind("click", send_to_server)

@bind("#test", "click")
def get_text(ev):
  
  ajax.get(document["message"].value,
            timeout=7,
            oncomplete=display_increment)