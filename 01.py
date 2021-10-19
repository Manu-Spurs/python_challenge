inString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def shift_string(inString, inOffset):
    return "".join([chr((ord(x) + inOffset)%123 if ord(x) + inOffset <=122  else 96+(ord(x) + inOffset)%123) for x in inString])
