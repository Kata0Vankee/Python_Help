'''
t = "dwd\n"
print(t[0].islower())
print(t.find('d'))
def find(str, ch):
    list = []
    for i, ltr in enumerate(str):
        if ltr == ch:
            list.append(i)
    return list
list = find("Neeus. DWDWD www.google.com", '.')
print(list)

str = "nen. com.goole.dwd"
list = find(str, '.')
for index in list:
    print(index, str[index], str[index-1], str[index+1])
    if str[index+1] != ' ' and str[index + 1].islower() and str[index-1].islower():
        str = str[:index] + '#' + str[index + 1:]

print(str)

def de_format(sentence):
    sentence = sentence.replace("#", ".")
    return sentence

str = de_format(str)
print(str)



def en_format(para):
    while para.find(".."):
        para = para.replace("..", ".")
    return para

print(en_format("ndww.. dwdw ..dwd"))

print("dwdwd".replace("wd", "d"))
'''
def find(str, ch):
    list = []
    for i, ltr in enumerate(str):
        if ltr == ch:
            list.append(i)
    return list


def en_format(para):
    where_point = find(para, '.')
    for index in where_point:
        if index < len(para) - 1:
            if para[index+1] != ' ' and para[index + 1].islower() and para[index-1].islower():
                para = para[:index] + '#' + para[index+1:]
    where_point = find(para, '.')
    for index in where_point:
        if index < len(para) - 1:
            if para[index + 1] == '"':
                para = para[:index] + '"' + para[index + 1:]
                para = para[:index] + '.' + para[index + 2:]
    while ".. " in para:
        para = para.replace(".. ", ".")

    return para

str = 'new para:  Home Fixit để thêm. Nhãn dán môi trường. Bởi Bruce Hartiga. Home Fixit, nhà bán lẻ lớn thứ hai của quốc gia, tuyên bố sẽ theo dõi, Four Mart, nhà bán lẻ lớn nhất của quốc gia, bằng cách tham gia phong trào xanh.. Home Fixit cho biết, bắt đầu từ tuần tới, họ sẽ dán nhãn dán cho tất cả các sản phẩm thúc đẩy bảo tồn năng lượng, được làm từ chất thải có thể tái chế hoặc được coi là có tác động tối thiểu đến môi trường, đặc biệt là trong khu vực không khí sạch và nước. Hệ thống này để xác định các sản phẩm như vậy có thể thấy có tới 7.000 sản phẩm thân thiện với môi trường được dán nhãn theo cách này trong ba năm tới. Những sản phẩm này sẽ được nhận dạng bằng nhãn dán Home Fixit Eco Friend. "Mặc dù hầu hết các sản phẩm này đắt hơn các sản phẩm thông thường", Vivian Lacey, chủ tịch đổi mới môi trường tại nhà bán lẻ nói, "Khách hàng đã kêu gọi cho các sản phẩm này." Khi lo ngại về ô nhiễm và biến đổi khí hậu được nêu ra, người tiêu dùng lo lắng về thói quen mua sắm của họ tác động đến môi trường như thế nào. Home Fixit có kế hoạch dành nhiều không gian hơn cho các sản phẩm thân thiện với môi trường trong tương lai. Các nhà cung cấp hỗ trợ dòng Eco Friend cũng sẽ được ưu đãi tại các cửa hàng của Home Fixit miễn là họ sản xuất hàng hóa Eco Friend với giá tương đương với hàng hóa thông thường. "Mọi người muốn đóng góp cho một môi trường trong sạch, nhưng họ không biết làm thế nào", bà Lacey nói. "Chúng tôi đang cho họ một cơ hội để làm điều này khi họ mua sắm." Từ: Tobias Foucan <tfoucan@valusave.com. Tới: Ivana Dench <idench @ valusave.com>. Chủ đề: Sản phẩm xanh cho ValuSave. Ngày: 9 tháng 5. Tài liệu đính kèm: Productfile.doc. Trước đây, tôi biết rằng chúng tôi đã miễn cưỡng phân loại một số sản phẩm là "xanh" hoặc "thân thiện với môi trường", vì doanh số mờ nhạt, nhưng tôi nghĩ đã đến lúc chúng ta có thể tiếp thị thành công các sản phẩm đó tại ValuSave. Các nhà bán lẻ lớn hơn như Home Fixit và Four Mart đã giới thiệu toàn bộ các dòng hàng hóa thân thiện với môi trường mà người tiêu dùng mong muốn mua. Tôi nhận ra rằng sức mua của chúng tôi không lớn bằng các nhà bán lẻ lớn hơn, nhưng có nhiều cách chúng tôi cũng có thể giới thiệu các dòng như vậy mà không ảnh hưởng đến lợi nhuận của chúng tôi.. Chúng ta nên bắt đầu bằng cách xem xét những sản phẩm chúng tôi đã cung cấp thân thiện với môi trường. Ví dụ, thuốc diệt côn trùng tự nhiên và bóng đèn huỳnh quang. Doanh số của các sản phẩm này vượt xa các sản phẩm không được phân loại là thân thiện với môi trường. Thúc đẩy tác động thấp của họ đến môi trường sẽ chỉ thu hút nhiều khách hàng hơn.. Tôi đã lập ra một danh sách các sản phẩm hiện có có thể đủ điều kiện cho một nhãn thân thiện với môi trường. Mặc dù một số trong số chúng có giá cao hơn các sản phẩm tương tự khác, chúng tôi có thể làm nhiều hơn để quảng bá chúng bằng cách sử dụng màn hình trong cửa hàng hoặc bằng cách giảm giá phiếu giảm giá cho một số mặt hàng nhất định. Một cuộc khảo sát được thực hiện về khách hàng tại chi nhánh ở Tucson của chúng tôi cho thấy họ quan tâm đến việc thử các sản phẩm thân thiện với môi trường. Nếu chúng ta có thể khiến họ mua những sản phẩm này chỉ một lần, tôi chắc chắn rằng chúng ta sẽ gắn kết họ suốt đời.. Trân trọng,. Tobias Foucan. Quản lý kinh doanh'
print(str)
str = en_format(str)
print(str)