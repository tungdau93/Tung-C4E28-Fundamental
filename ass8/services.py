from model import services

new_services = {
    "title": "c4e28",
    "author": "Tùng Đào",
    "content": "Anh không thể biến mùa hạ thành mùa đông nhưng em chỉ cần hích cái mông là anh sẽ đổi kiểu"
}
services.insert_one(new_services)
