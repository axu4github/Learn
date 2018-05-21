from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json


class JsonEmptyError(RuntimeError):

    def __init__(self, msg):
        self.msg = msg


class PyStreamCallback(StreamCallback):

    def __init__(self):
        pass

    def transfer(self, recoed):
        pass

    def process(self, inputStream, outputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        if content == "{}":
            raise JsonEmptyError("CONTENT IS EMPTY.")

            
        outputStream.write(content.encode("utf-8"))


flowFile = session.get()
try:
    if(flowFile != None):
        session.write(flowFile, PyStreamCallback())
        session.transfer(flowFile, REL_SUCCESS)
except JsonEmptyError as e:
    log.warn(str(e.msg))
    session.transfer(flowFile, REL_FAILURE)
except Exception as e:
    log.error(str(e))
    session.transfer(flowFile, REL_FAILURE)

session.commit()
