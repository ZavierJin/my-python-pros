# learn python -- 17th day


"""
收盘价数据仪表盘(dashboard)
多图整合
"""


with open('收盘价Dashboard.html', 'w', encoding='utf-8') as h_f:
    h_f.write('<html><head><title>收盘价Dashboard</title><meta\
charset="utf-8"></head><body>\n')
    for svg in [
            '收盘价折线图.svg', '收盘价对数变换折线图.svg',
            '收盘价月日均值.svg', '收盘价每周均值.svg'
    ]:
        h_f.write('    <object type="image/svg+xml" data="{0}"\
height=500></object>\n'.format(svg))
    h_f.write('</body></html>')
