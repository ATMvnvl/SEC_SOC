## SOC 2.0
Sau bài về SOC 1.0 “cày tay”, hôm nay chúng ta quay lại với SOC 2.0 - bước tiến lớn khi tự động hóa và công cụ hiện đại bắt đầu “gánh team”. Đây là lựa chọn phổ biến cho doanh nghiệp vừa và nhỏ muốn nâng cấp bảo mật mà không quá phức tạp như SOC 3.0. Cùng khám phá từng bước nhé!
Bước 1: Xác định phạm vi và tích hợp nguồn dữ liệu
• Việc cần làm: Quyết định tài sản cần bảo vệ và gom dữ liệu từ các nguồn về một chỗ.
• Thực hành:
1. Lập danh sách tài sản: Server, endpoint (máy nhân viên), firewall, ứng dụng web, v.v.
2. Chọn nguồn dữ liệu: Log từ firewall (pfSense), IDS (Snort), Windows Event Logs, ứng dụng (như Apache/Nginx logs).
3. Tích hợp: Dùng một công cụ SIEM để tập trung dữ liệu (gợi ý: thử Elastic Stack hoặc Splunk Free nếu ngân sách hạn chế).
• Ví dụ: Cấu hình pfSense gửi log qua Syslog đến SIEM bằng cách vào Status > System Logs > Settings, bật Syslog và trỏ về IP của SIEM server.
​
Bước 2: Cài đặt và cấu hình SIEM
SOC 2.0 phụ thuộc lớn vào SIEM để tự động phân tích log:
• Công cụ đề xuất: Elastic Stack (ELK - Elasticsearch, Logstash, Kibana) vì miễn phí và mạnh mẽ.
• Thực hành:
1. Cài đặt ELK:
• Trên Ubuntu: Tải Elasticsearch, Logstash, Kibana từ elastic.co, cài bằng lệnh sudo apt-get install elasticsearch logstash kibana.
• Khởi động: sudo systemctl start elasticsearch, tương tự với Logstash và Kibana.
2. Cấu hình Logstash: Tạo file logstash.conf để nhận log từ Syslog và đẩy vào Elasticsearch:
​
input { syslog { port => 514 } }
output { elasticsearch { hosts => ["localhost:9200"] } }
3. Kibana Dashboard: Truy cập <http://localhost:5601>, tạo dashboard để xem log theo thời gian thực.
• Mục tiêu: Có một nơi tập trung để nhìn toàn cảnh hệ thống.
​
Bước 3: Thiết lập quy trình tự động hóa
• Việc cần làm: Tạo rule để SIEM tự động phát hiện và cảnh báo.
• Thực hành:
1. Tạo rule cơ bản: Trong Kibana, vào Security > Alerts, thêm rule như “Nếu có hơn 10 lần đăng nhập thất bại trong 5 phút từ cùng IP thì báo”.
2. Cảnh báo: Cấu hình gửi email hoặc thông báo qua Slack khi rule bị kích hoạt (dùng plugin ElastAlert hoặc tính năng Alerting của Kibana).
3. Tối ưu: Thêm rule nâng cao, ví dụ: “Phát hiện quét port từ IDS” hoặc “Lưu lượng mạng bất thường tăng đột biến”.
• Ví dụ: Rule phát hiện brute force SSH: Kiểm tra log chứa “failed password” từ /var/log/auth.log, đếm số lần xuất hiện trong 5 phút.
​
Bước 4: Giám sát và phản ứng chủ động
• Giám sát: Không cần xem log thủ công như SOC 1.0 nữa, giờ chỉ cần theo dõi dashboard SIEM.
• Thực hành:
1. Kiểm tra dashboard: Xem biểu đồ số lượng alert, nguồn IP đáng ngờ, hay sự kiện bất thường (như spike lưu lượng).
2. Điều tra: Khi có cảnh báo (ví dụ: “Brute force từ IP 203.0.113.5”), dùng Kibana lọc log liên quan, kiểm tra thời gian và hành vi.
3. Phản ứng:
• Chặn IP thủ công trên firewall: pfctl -t blacklist -T add 203.0.113.5.
• Hoặc tự động: Viết script gọi API của firewall khi SIEM phát hiện tấn công (nâng cao hơn chút).
• Mẹo: Dành 30 phút mỗi ngày xem lại alert để tránh bị “ngập” trong báo động giả.
​
Bước 5: Báo cáo và cải tiến liên tục
• Việc cần làm: Tổng hợp dữ liệu từ SIEM để báo cáo và tối ưu hệ thống.
• Thực hành:
1. Tạo báo cáo: Trong Kibana, xuất report dạng PDF từ dashboard (ví dụ: “Tuần này có 50 alert, chặn 10 IP, 5 sự cố nghiêm trọng”).
2. Cải thiện rule: Nếu thấy nhiều false positive (như VPN bị nhầm thành tấn công), chỉnh lại ngưỡng hoặc thêm ngoại lệ trong rule.
3. Đánh giá hiệu quả: So sánh số sự cố phát hiện được với tuần trước để xem SOC có tiến bộ không.
• Ví dụ: Mình từng thấy rule “quét port” báo nhầm vì nhân viên test tool, phải thêm IP nội bộ vào whitelist.
Lưu ý khi thực hành SOC 2.0
• Ưu điểm: Tự động hóa giúp tiết kiệm thời gian, phát hiện nhanh hơn SOC 1.0, tích hợp được nhiều nguồn dữ liệu.
• Nhược điểm: Vẫn cần con người xử lý alert phức tạp, chi phí đầu tư ban đầu cao hơn (nếu dùng SIEM trả phí như Splunk).
• Kinh nghiệm thực tế: Đừng để SIEM thành “thùng rác log” – chỉ gom dữ liệu quan trọng, tránh quá tải.
​
Câu hỏi cho cả nhà:
• Ai từng thử ELK hay Splunk chưa? Cảm giác thế nào?
• Theo bạn, SOC 2.0 còn thiếu gì để “đánh bại” hacker hiện đại