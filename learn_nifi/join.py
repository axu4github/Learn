
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import InputStreamCallback
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


contents = []


class ReaderCallback(InputStreamCallback):

    def __init__(self, flowFile):
        self.flowFile = flowFile
        self.tableName = self.flowFile.getAttribute("table.name")

    def process(self, inputStream):
        contents.append({
            "tableName": self.tableName,
            "uuid": self.flowFile.getAttribute("uuid"),
            "content": IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        })


flowFileList = session.get(10)
try:
    if not flowFileList.isEmpty():
        for flowFile in flowFileList:
            session.read(flowFile, ReaderCallback(flowFile))

        log.info("contents len => {}.".format(len(contents)))
        for content in contents:
            log.info("content.uuid => {}.".format(content["uuid"]))

        raise Exception("flowFileTypes.")
    else:
        raise Exception("FlowFiles is Empty.")
except Exception as e:
    log.error("ERROR => ({}).".format(e))
    session.rollback()
