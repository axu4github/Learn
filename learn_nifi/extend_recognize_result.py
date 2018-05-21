from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json

ROLE_A = "坐席"
ROLE_B = "客户"


class PyStreamCallback(StreamCallback):

    def __init__(self, flowFile):
        self.flowFile = flowFile

    def _format(self, result):
        return ";".join(result)

    def parse_voice_result(self, filepath):
        plaintexta, plaintextb, emotiona, emotionb = [], [], [], []
        emotionvaluea, emotionvalueb, tonea, toneb = [], [], [], []
        speeda, speedb = [], []
        rolea, roleb = ROLE_A, ROLE_B

        with open(filepath, "r") as f:
            while True:
                line = f.readline()
                if line:
                    line = line.strip()
                    try:
                        (start, end, plaintext, role, emotion, emotion_value,
                         tone_avg, tone_start, tone_end,
                         speed) = line.split("\t")
                        if role == rolea:
                            emotiona.append(emotion)
                            emotionvaluea.append(emotion_value)
                            tonea.append("{0} {1} {2}".format(
                                tone_avg, tone_start, tone_end))
                            speeda.append(
                                "{0} {1} {2}".format(start, end, speed))
                            plaintexta.append(plaintext)
                        elif role == roleb:
                            emotionb.append(emotion)
                            emotionvalueb.append(emotion_value)
                            toneb.append("{0} {1} {2}".format(
                                tone_avg, tone_start, tone_end))
                            speedb.append(
                                "{0} {1} {2}".format(start, end, speed))
                            plaintextb.append(plaintext)
                        else:
                            raise Exception("Unknow Role: [{0}]".format(role))
                    except Exception as e:
                        raise e
                else:
                    break

        plaintexta = self._format(plaintexta)
        plaintextb = self._format(plaintextb)
        emotiona = self._format(emotiona)
        emotionb = self._format(emotionb)
        emotionvaluea = self._format(emotionvaluea)
        emotionvalueb = self._format(emotionvalueb)
        tonea = self._format(tonea)
        toneb = self._format(toneb)
        speeda = self._format(speeda)
        speedb = self._format(speedb)

        return (plaintexta, plaintextb, emotiona, emotionb, emotionvaluea, emotionvalueb, tonea, toneb, speeda, speedb)

    def parse_voice_interruption(self, filepath):
        robspeeda, robspeedb = [], []
        rolea, roleb = ROLE_A, ROLE_B
        with open(filepath, "r") as f:
            while True:
                line = f.readline()
                if line:
                    line = line.strip()
                    try:
                        (start, end, role, value) = line.split("\t")
                        if role == rolea:
                            robspeeda.append(
                                "{0} - {1} - {2}".format(start, end, value))
                        elif role == roleb:
                            robspeedb.append(
                                "{0} - {1} - {2}".format(start, end, value))
                        else:
                            raise Exception("Unknow Role: [{0}]".format(role))
                    except Exception as e:
                        raise e
                else:
                    break

        robspeeda = self._format(robspeeda)
        robspeedb = self._format(robspeedb)
        return (robspeeda, robspeedb)

    def parse_voice_blankinfo(self, filepath):
        with open(filepath, "r") as f:
            blankinfo = f.read().strip()

        blankinfo_obj = json.loads(blankinfo)
        blank_len_arr = [item["blankLen"] for item in blankinfo_obj]
        max_pos = blank_len_arr.index(max(blank_len_arr))
        max_blank_len = blankinfo_obj[max_pos]["blankLen"]
        max_start_blankpos = blankinfo_obj[max_pos]["startBlankPos"]
        return (blankinfo, max_start_blankpos, max_blank_len)

    def extend(self, vocie):
        if "filename" in vocie:
            # filename = os.path.basename(vocie["filename"])
            voice_result_path = "/Users/axu/Tmp/voiceresult/text_role_result.txt"
            voice_interruption_path = "/Users/axu/Tmp/voiceresult/result_interruption.txt"
            voice_blankinfo_path = "/Users/axu/Tmp/voiceresult/blankinfo.txt"
            (plaintexta, plaintextb, emotiona, emotionb, emotionvaluea, emotionvalueb,
             tonea, toneb, speeda, speedb) = self.parse_voice_result(voice_result_path)
            (robspeeda, robspeedb) = self.parse_voice_interruption(
                voice_interruption_path)
            (blankinfo, max_start_blankpos, max_blank_len) = self.parse_voice_blankinfo(
                voice_blankinfo_path)

            vocie["plaintexta"] = plaintexta
            vocie["plaintextb"] = plaintextb
            vocie["emotiona"] = emotiona
            vocie["emotionb"] = emotionb
            vocie["emotionvaluea"] = emotionvaluea
            vocie["emotionvalueb"] = emotionvalueb
            vocie["tonea"] = tonea
            vocie["toneb"] = toneb
            vocie["speeda"] = speeda
            vocie["speedb"] = speedb
            vocie["robspeeda"] = robspeeda
            vocie["robspeedb"] = robspeedb
            vocie["blankinfo"] = blankinfo
            vocie["max_start_blankpos"] = max_start_blankpos
            vocie["max_blank_len"] = max_blank_len

    def process(self, inputStream, outputStream):
        content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        if content == "{}":
            raise Exception("CONTENT IS NULL!")

        content_obj = json.loads(content)
        map(self.extend, content_obj)
        outputStream.write(bytearray(json.dumps(content_obj).encode("utf-8")))


flowFile = session.get()
try:
    if(flowFile != None):
        session.write(flowFile, PyStreamCallback(flowFile))
        session.transfer(flowFile, REL_SUCCESS)
except Exception as e:
    log.error(str(e))
    session.transfer(flowFile, REL_FAILURE)
