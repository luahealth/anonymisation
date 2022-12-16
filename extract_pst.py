from pathlib import Path

from libratom.lib.core import load_spacy_model
from libratom.lib.pff import PffArchive

PST_FILE = Path("/Users/fionn/Documents/anonymisation/TaskUs_test_data.pst")

with PffArchive(PST_FILE) as archive:
    print(archive.tree)

MESSAGE_ID = 2097188

archive = PffArchive(PST_FILE)
message = archive.get_message_by_id(MESSAGE_ID)

headers = message.transport_headers
print(headers.strip())

body = message.plain_text_body or message.html_body or message.rtf_body

if isinstance(body, bytes):
    body = str(body, encoding="utf-8", errors="replace")

print(body.strip())
