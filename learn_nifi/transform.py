from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json

""" 转换列内容 """


class PyStreamCallback(StreamCallback):

    def __init__(self):
        pass

    def transfer(self, products):
        if "product_names" in products:
            products["product_names"] = products["product_names"].split(" && ")

    def process(self, inputStream, outputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        content_obj = json.loads(content)
        map(self.transfer, content_obj)
        outputStream.write(bytearray(json.dumps(content_obj).encode("utf-8")))


flowFile = session.get()
if(flowFile != None):
    session.write(flowFile, PyStreamCallback())

session.transfer(flowFile, REL_SUCCESS)