# -*- coding: utf-8 -*-

import json


def _format(result):
    return ";".join(result)


def parse_voice_result(result_filepath):
    plaintexta, plaintextb, emotiona, emotionb = [], [], [], []
    emotionvaluea, emotionvalueb, tonea, toneb = [], [], [], []
    speeda, speedb = [], []
    rolea, roleb = "客户", "坐席"

    with open(result_filepath, "r") as f:
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

    plaintexta = _format(plaintexta)
    plaintextb = _format(plaintextb)
    emotiona = _format(emotiona)
    emotionb = _format(emotionb)
    emotionvaluea = _format(emotionvaluea)
    emotionvalueb = _format(emotionvalueb)
    tonea = _format(tonea)
    toneb = _format(toneb)
    speeda = _format(speeda)
    speedb = _format(speedb)

    return (plaintexta, plaintextb, emotiona, emotionb, emotionvaluea, emotionvalueb, tonea, toneb, speeda, speedb)


def parse_voice_interruption(filepath):
    robspeeda, robspeedb = [], []
    rolea, roleb = "客户", "坐席"
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

    return (_format(robspeeda), _format(robspeedb))


def parse_blankinfo(filepath):
    with open(filepath, "r") as f:
        blankinfo = f.read().strip()

    blankinfo_obj = json.loads(blankinfo)
    blank_len_arr = [item["blankLen"] for item in blankinfo_obj]
    max_pos = blank_len_arr.index(max(blank_len_arr))
    max_blank_len = blankinfo_obj[max_pos]["blankLen"]
    max_start_blankpos = blankinfo_obj[max_pos]["startBlankPos"]
    return (blankinfo, max_start_blankpos, max_blank_len)

filepath = "/Users/axu/Tmp/voiceresult/text_role_result.txt"
interruption_filepath = "/Users/axu/Tmp/voiceresult/result_interruption.txt"
blank_filepath = "/Users/axu/Tmp/voiceresult/blankinfo.txt"

# r = parse_voice_result(filepath)
# r = parse_voice_interruption(interruption_filepath)
r = parse_blankinfo(blank_filepath)
for re in r:
    print(re)
    print("-" * 20)
