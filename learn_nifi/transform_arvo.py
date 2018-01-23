import avro.schema
import io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

"""
转换avro格式列内容（未执行成功）（参考：https://gist.github.com/lfidnl/100a3ef18a72eb0be35bad27e20dd8aa）
16:31:22 CSTERROR016110c3-354e-1ba9-db2d-3af0ad0a4b8f ExecuteScript[id=016110c3-354e-1ba9-db2d-3af0ad0a4b8f] Failed to process session due to org.apache.nifi.processor.exception.ProcessException: javax.script.ScriptException: ImportError: No module named avro in <script> at line number 1: javax.script.ScriptException: ImportError: No module named avro in <script> at line number 1
"""


class PyStreamCallback(StreamCallback):

    def __init__(self):
        pass

    def transfer(self, products):
        if "product_names" in products:
            products["product_names"] = products["product_names"].split(" && ")

    def process(self, inputStream, outputStream):
        bytes_arr = IOUtils.toByteArray(inputStream, StandardCharsets.UTF_8)
        bytes_io = io.BytesIO(bytes_arr)
        reader = DataFileReader(bytes_io, DatumReader())
        schema = reader.datum_reader.writers_schema
        writer = DataFileWriter(outputStream, DatumWriter(), schema)
        for product in reader:
            product = self.transfer(product)
            writer.append(product)

        writer.close()


flowFile = session.get()
if(flowFile != None):
    session.write(flowFile, PyStreamCallback())
    session.transfer(flowFile, REL_SUCCESS)
