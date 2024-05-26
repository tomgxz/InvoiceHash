import zlib

EXISTING = [00,36,66,67]

name = b"NAME"
gen = zlib.crc32(name)

i=0
short = int(str(gen)[i:i+2])

while short in EXISTING:
  i+=1
  short = int(str(gen)[i:i+2])

print(short)
