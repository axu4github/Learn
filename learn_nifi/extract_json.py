from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import (
    InputStreamCallback, OutputStreamCallback
)
import json


class WriteStreamCallback(OutputStreamCallback):

    def __init__(self, content=None):
        self.content = content

    def process(self, outputStream):
        outputStream.write(self.content.encode("utf-8"))


class ReadStreamCallback(InputStreamCallback):

    def __init__(self, parentFlowFile):
        self.parentFlowFile = parentFlowFile

    def process(self, inputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        if content == "{}":
            raise Exception("CONTENT IS EMPTY!")

        content_obj = json.loads(content)

        if "filepath" in content_obj:
            childFlowFile = session.create(self.parentFlowFile)
            childFlowFile = session.write(
                childFlowFile, WriteStreamCallback(content=content))
            childFlowFile = session.putAllAttributes(
                childFlowFile, {"filepath": content_obj["filepath"]})
            session.transfer(childFlowFile, REL_SUCCESS)
        else:
            raise Exception("NOT HAS FILEPATH.")


flowFile = session.get()
try:
    if(flowFile != None):
        session.read(flowFile, ReadStreamCallback(flowFile))
        session.remove(flowFile)
except Exception as e:
    log.error(str(e))
    session.transfer(flowFile, REL_FAILURE)
