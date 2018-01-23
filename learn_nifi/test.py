from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import (
    InputStreamCallback, OutputStreamCallback
)


class SplitFlowCallback(OutputStreamCallback):

    def __init__(self, content=None):
        self.content = content

    def process(self, outputStream):
        outputStream.write(bytearray(self.content.encode("utf-8")))


class PyStreamCallback(InputStreamCallback):

    def __init__(self, parentsFlowFile):
        self.parentsFlowFile = parentsFlowFile

    def process(self, inputStream):
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        filenames = text.strip().split("\n")
        str_filenames = ",".join(filenames)
        log.info(str_filenames)
        for filename in filenames:
            splitFlowFile = session.create(self.parentsFlowFile)
            splitFlowCallback = SplitFlowCallback(content=filename)
            splitFlowFile = session.write(splitFlowFile, splitFlowCallback)
            splitFlowFile = session.putAllAttributes(
                splitFlowFile, {"filename": "{}_splited".format(filename)})
            session.transfer(splitFlowFile, REL_SUCCESS)


flowFile = session.get()
if(flowFile != None):
    session.read(flowFile, PyStreamCallback(flowFile))
    session.remove(flowFile)
