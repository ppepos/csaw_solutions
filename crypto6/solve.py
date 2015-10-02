with open('bricks_of_gold_40d12e05cd6d67ed51d29a6da39d6878', 'r') as fd:
    data = fd.read()
    data = data[0 : data.find("THE_SECRET_IV")]

    key = ""
    for i in range(4):
        key += chr(ord(data[i]) ^ ord("CASH"[i]) ^ ord("%PDF"[i]))
        
    # print key

    plain = ""
    prev_block = "CASH"
    for block in range(0, len(data), 4):
        block = data[block: block+4] 
        for idx, b in enumerate(block):
            plain += chr(ord(b) ^ ord(key[idx]) ^ ord(prev_block[idx]))
        prev_block = block

    print plain

