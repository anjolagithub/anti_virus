import vt
import time

"""
["DATE_ATTRIBUTES", "context_attribut
es", "date", "error", "from_dict", "get", "id", "relationships", "results", "set_data", "stats", "status", "to_dict", "type"]
"""
client = vt.Client("67f88bc1ae450344880102e9ce31ab0dfaef97a7997d1f7e8eac1cbadcf457d2")

with open("index.html", "rb") as f:
  #analysis = client.scan_file(f)
  analysis = client.scan_file(f, wait_for_completion=True)

print(analysis.results)


#analysis = client.scan_url("", wait_for_completion=True)
# while True:
#    analysis = client.get_object("/analyses/{}", analysis.id)
#    print(analysis.status)
#    if analysis.status == "completed":
#      break
#    time.sleep(30)
