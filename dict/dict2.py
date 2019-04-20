phim = {
    "tên":"IT",
    "mô tả": "phim kinh dị ",
}
print(phim)
phim["diễn viên"] = "Micheal Abc"
print(phim)
phim["hãng sản xuất"] = input("hãng sản xuất:")
print(phim)
phim["mô tả"] = "sản xuất năm 2018"
print(phim)
phim["diễn viên"] = input("giới tính:")
print(phim)
del phim["diễn viên"]
del phim[input("nhập key muốn xóa:")]
print(phim)