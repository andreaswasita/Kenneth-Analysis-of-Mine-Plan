import fitz
doc = fitz.open('IGO_Announcement.pdf')
print(f'Pages: {len(doc)}')
# Read pages 1-30 (key data, not the JORC tables at the end)
for i in range(min(35, len(doc))):
    page = doc[i]
    text = page.get_text()
    print(f'--- PAGE {i+1} ---')
    print(text)
