## Threat Intelligence Platform (TIP)
Threat Intelligence Platform (TIP): “Radar” của an ninh mạng
Lại là mình đây, sau SIEM, IDS/IPS và Honeypot. Nay chúng ta nói đến TIP. Threat Intelligence Platform (TIP), hay Nền tảng Thông tin Tình báo Mối đe dọa, là một công cụ hoặc hệ thống giúp thu thập, phân tích và cung cấp thông tin về các mối đe dọa an ninh mạng. Nói đơn giản, nó giống như một “radar” quét khắp nơi – từ internet công khai, dark web, đến dữ liệu nội bộ – để phát hiện và hiểu rõ kẻ tấn công, cách chúng hoạt động, và làm sao để chặn đứng chúng. Trong một SOC (Security Operations Center), TIP đóng vai trò cung cấp “tin tức nóng” để đội ngũ bảo mật không chỉ phản ứng mà còn dự đoán trước nguy cơ.
TIP hoạt động thế nào?
TIP có ba nhiệm vụ chính:
- Thu thập dữ liệu: Lấy thông tin từ nhiều nguồn như diễn đàn hacker, báo cáo công khai, hoặc nhật ký hệ thống.
- Phân tích thông tin: Biến dữ liệu thô thành những gợi ý cụ thể, ví dụ: “IP này nguy hiểm vì thuộc mạng botnet tấn công tuần trước.”
- Hỗ trợ hành động: Đưa ra danh sách IP cần chặn, cảnh báo về lỗ hổng, hay hướng dẫn cách xử lý một cuộc tấn công.
Các thành phần quan trọng trong TIP
TIP thường xử lý các loại dữ liệu sau:
IoC (Indicators of Compromise - Chỉ số Thỏa hiệp):
- Định nghĩa: Dấu hiệu cho thấy hệ thống đã bị tấn công, như IP độc hại, tên miền giả mạo, hoặc mã băm của malware.
- Ý nghĩa: Giúp phát hiện nhanh kẻ xâm nhập.
- Ví dụ: Một file có mã băm “abc123” được xác định là ransomware WannaCry.
CVE (Common Vulnerabilities and Exposures - Lỗ hổng và Tiếp xúc Chung):
- Định nghĩa: Danh sách các lỗ hổng bảo mật đã được ghi nhận, mỗi cái có mã riêng (ví dụ: CVE-2023-1234).
- Ý nghĩa: Cảnh báo về điểm yếu trong phần mềm mà hacker có thể khai thác.
- Ví dụ: CVE-2021-34527 liên quan đến lỗ hổng PrintNightmare trong Windows.
TTP (Tactics, Techniques, and Procedures - Chiến thuật, Kỹ thuật, Thủ tục):
- Định nghĩa: Cách thức và phương pháp mà hacker sử dụng.
- Ý nghĩa: Hiểu hành vi để dự đoán bước đi tiếp theo của kẻ tấn công.
- Ví dụ: Nhóm APT29 dùng kỹ thuật “spear phishing” để lừa nhân viên nhấp vào email giả mạo.
Ví dụ cụ thể: Chặn một vụ tấn công nhờ TIP
Giả sử một công ty nhận được cảnh báo từ SIEM về lưu lượng lạ từ vài máy tính gửi email hàng loạt – dấu hiệu của phishing. Không có TIP, đội bảo mật sẽ mất nhiều thời gian mò mẫm. Nhưng với TIP, tình huống được giải quyết nhanh chóng:
TIP (chẳng hạn MISP – mã nguồn mở) được nhập IP đáng ngờ. Nó báo rằng IP này thuộc botnet đã tấn công ngành bán lẻ tuần trước, kèm danh sách 5 tên miền giả mạo và mẫu email lừa đảo.
Đội ngũ ngay lập tức:
Chặn các IP và tên miền trên firewall.
- Kiểm tra hệ thống xem có file nào khớp với IoC (mã băm của malware) không.
- Gửi cảnh báo cho nhân viên về email giả mạo.
- Kết quả: Vụ tấn công bị dập tắt trong 1 giờ, không gây thiệt hại.
Một số TIP mã nguồn mở và thương mại
Mã nguồn mở:
- MISP: Dùng để chia sẻ IoC giữa các tổ chức, dễ tích hợp với SIEM, phù hợp cho nhóm nhỏ.
- Ví dụ: Công ty A phát hiện ransomware, nhập IoC vào MISP để cảnh báo công ty B.
- OpenCTI: Tổng hợp dữ liệu từ CVE, IoC, TTP, hiển thị trực quan, miễn phí nhưng cần kỹ thuật để triển khai.
- Ví dụ: Theo dõi chiến dịch tấn công APT qua giao diện web.
Thương mại:
- Recorded Future: Cung cấp thông tin từ dark web, phân tích bằng AI, lý tưởng cho doanh nghiệp lớn.
- Ví dụ: Phát hiện sớm tên miền giả mạo thương hiệu công ty.
- ThreatConnect: Tích hợp IoC, CVE, và tự động hóa phản ứng, phù hợp với SOC chuyên nghiệp.
- Ví dụ: Tự động chặn IP độc hại dựa trên dữ liệu TIP.
Tại sao TIP quan trọng?
An ninh mạng không chỉ là chờ đợi và sửa chữa, mà là dự đoán và ngăn chặn. TIP giúp đội SOC:
- Biết trước kẻ tấn công nhắm vào đâu (dựa trên CVE, IoC).
- Hiểu cách chúng tấn công (qua TTP).
- Hành động nhanh chóng (chặn IP, vá lỗ hổng).
P/s: Hãy theo dõi tôi để cùng tìm hiểu nhiều hơn về SOC

![alt text](image-3.png)