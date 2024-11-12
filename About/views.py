from django.shortcuts import render
from django.views import View


# Create your views here.

class TeacherContactsView(View):
    def get(self, req):

        context = {
            "teachers": [
                "Phụ trách khoa: Cô Phạm Thị Thu Hiếu 0988902652 - - hieup3@gmail.com ",
                "Phó trưởng khoa: Thầy Vũ Hùng Cường 0989158258 - vhcuongvh@gmail.com",
                "Trưởng tổ môn CNTT:  Cô Ngô Thị Lan 0982010510 - onebit.lannt@gmail.com",
                "Trưởng tổ môn Thiết kế đồ họa: Cô Nguyễn Thị Hải Yến 0989091183 - yenmtcn@gmail.com",
                "Giảng viên: Thầy Nguyễn Hồng Quân 0357444000 - nhquanst@gmail.com",
                "Giảng viên: Thầy Nguyễn Đình Quyết 0983750717 - dinhquyet@gmail.com",
                "Giảng viên: Cô Đặng Thị Huệ 0982128025 - dangthihue.2006@gmail.com",
                "Giảng viên: Cô Chu Thị Thanh Xuân 0989183975 - chuthanhxuan2009@gmail.com",
                "Giảng viên: Cô Nguyễn Thị Thu Thủy 0984083308 - nttthuy2103@gmail.com",
                "Giảng viên: Cô Phan Thị Việt Hà 0988977187 - phanviethavic@gmail.com",
                "Giảng viên: Phan Mạnh Chung 0988456586 - toi.ck@gmail.com",
                "Giảng viên: Thầy Nguyễn Đức Nguyện 0983756867 - ndnguyen312@gmail.com",
                "Giảng viên: Cô Nguyễn Thị Hiền 0393991524 - hiennguyen79@gmail.com",
                "Giảng viên: Cô Nguyễn Thị Vân Anh 0982936648 - nguyenvananhvp88@gmail.com",
                "Giảng viên: Cô Nguyễn Hoàng Hà 0398490703 - hoangha90st@gmail.com",
                "Giảng viên: Thầy Phạm Hồng Long 0374704871 - long.cntt252@gmail.com",
                "Giảng viên: Thầy Nguyễn Thành Trung 0972395713 - trungnt312@gmail.com",
            ]
        }
        return render(req, "user/contact.html", context)
