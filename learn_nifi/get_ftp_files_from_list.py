from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json
import os
from ftplib import FTP

SRC_FTP_HOST = src_ftp_host.getValue()
SRC_FTP_PORT = src_ftp_port.getValue()
SRC_FTP_USER = src_ftp_user.getValue()
SRC_FTP_PASSWORD = src_ftp_password.getValue()
DEST_ROOT_DIR = dest_root_dir.getValue()


class PyStreamCallback(StreamCallback):

    def __init__(self):
        self.ftp = FTP(SRC_FTP_HOST)
        self.ftp.login(SRC_FTP_USER, SRC_FTP_PASSWORD)

    def download_files(self, files):
        for file in files:
            src_file_path = file["filepath"]
            dest_file_path = "{0}{1}{2}".format(
                DEST_ROOT_DIR,
                os.path.sep,
                os.path.basename(src_file_path))
            log.info("{0} => {1}".format(src_file_path, dest_file_path))
            f = open(dest_file_path, "wb").write
            self.ftp.retrbinary("RETR %s" % src_file_path, f)

        return files

    def process(self, inputStream, outputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        if content == "{}":
            raise Exception("CONTENT IS NULL!")

        content_obj = json.loads(content)
        result = self.download_files(content_obj)
        outputStream.write(bytearray(json.dumps(result).encode("utf-8")))


flow_file = session.get()
try:
    if flow_file is not None:
        session.write(flow_file, PyStreamCallback())
        session.transfer(flow_file, REL_SUCCESS)
        session.commit()
except Exception as e:
    log.error(str(e))
    session.transfer(flow_file, REL_FAILURE)
