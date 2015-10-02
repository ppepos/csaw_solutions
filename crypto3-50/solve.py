import base64

with open('eps1.9_zer0-day_b7604a922c8feef666a957933751a074.avi', 'r') as fd:
    data = fd.read().strip()
    data = data.replace('\\n', '')
    print base64.b64decode(data)

