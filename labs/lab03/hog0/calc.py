import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

