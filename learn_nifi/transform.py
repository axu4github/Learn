from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json


class PyStreamCallback(StreamCallback):

    transfer_fields = ["product_names", "policy_codes",
                       "pay_modes", "way_names", "charge_descs",
                       "single_modes", "organ_areas"]

    def __init__(self, flowFile):
        self.flowFile = flowFile

    def transfer(self, products):
        for field in self.transfer_fields:
            if field in products and products[field] is not None:
                products[field] = list(set(products[field].split(" && ")))

        if "id" in products:
            products["id"] = products["filename"]

    def process(self, inputStream, outputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        if content == "{}":
            raise Exception("CONTENT IS NULL!")

        content_obj = json.loads(content)
        map(self.transfer, content_obj)
        outputStream.write(bytearray(json.dumps(content_obj).encode("utf-8")))


flowFile = session.get()
try:
    if(flowFile != None):
        session.write(flowFile, PyStreamCallback(flowFile))
        session.transfer(flowFile, REL_SUCCESS)
except Exception as e:
    log.error(str(e))
    session.transfer(flowFile, REL_FAILURE)
