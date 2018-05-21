from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json
import os
import time

DEST_BASE_DIR = dest_base_dir.getValue()
TIME_FORMAT = "%Y%m%d%H"
RECOGNIZE_COMMAND = "xxx.sh {0}"


class PyStreamCallback(StreamCallback):

    def __init__(self, flowFile):
        self.flowFile = flowFile
        self.dest_dir = self.get_dest_dir()

    def get_dest_dir(self):
        current_dir = "{0}/{1}/{2}".format(
            DEST_BASE_DIR, time.strftime(TIME_FORMAT, time.localtime()),
            self.flowFile.getAttribute("uuid"))
        os.makedirs(current_dir)
        return current_dir

    def move_to_dest(self, file):
        if "download_path" in file:
            src = file["download_path"]
            dest = "{0}/{1}".format(self.dest_dir, os.path.basename(src))
            log.info("move file {0} => {1}.".format(src, dest))
            os.rename(src, dest)

    def recognize(self):
        log.info(RECOGNIZE_COMMAND.format(self.dest_dir))
        time.sleep(60)

    def process(self, inputStream, outputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        if content == "{}":
            raise Exception("CONTENT IS NULL!")

        content_obj = json.loads(content)
        map(self.move_to_dest, content_obj)
        self.recognize()
        outputStream.write(bytearray(json.dumps(content_obj).encode("utf-8")))


flowFile = session.get()
try:
    if(flowFile != None):
        session.write(flowFile, PyStreamCallback(flowFile))
        session.transfer(flowFile, REL_SUCCESS)
except Exception as e:
    log.error(str(e))
    session.transfer(flowFile, REL_FAILURE)
