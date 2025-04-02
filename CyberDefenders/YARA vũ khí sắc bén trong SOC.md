## YARA vũ khí sắc bén trong SOC

YARA vũ khí sắc bén trong SOC
---
Vẫn là Virus, vẫn là Ransomware, vẫn là các mối đe dọa đến từ các anh chàng tinh nghịch đang khám phá "thế giới hacker", hay các nhóm APT được chính phủ tài trợ... Công nghệ thay đổi, nhưng mối đe dọa thì không: chúng lén lút, tham lam... nhưng luôn để lại dấu vết – nếu biết cách tìm. 
YARA không chỉ là công cụ. Nó là một người đồng đội bền bỉ, như con dao Thụy Sĩ trong túi – không hào nhoáng, nhưng sắc bén khi cần thiết.
1. Vai trò của YARA trong SOC
Qua hàng ngàn ca trực đêm và vài lần suýt mất "mạng" hệ thống, có thể đúc kết vài điều về YARA:
--Săn mã độc: Quét đống file hỗn loạn như lục thùng rác tìm đĩa 3.5 inch nhiễm virus thời xưa. Rule được viết, nó tìm – đơn giản, hiệu quả.
--Phân loại rác rưởi: Giữa biển dữ liệu, nó tách backdoor khỏi file log vô hại. Có lần, một SOC tưởng “readme.txt” là virus vì nằm cạnh Stuxnet – buồn cười mà không cười nổi.
--Tiết kiệm thời gian: Tự động hóa việc so khớp IoC, để còn lúc ngẫm đời qua ly cà phê nguội thay vì cắm mặt vào màn hình.
--Đánh gục kẻ thù: Rule tốt là đòn knock-out. Hacker có thể khóc trong lòng khi YARA tóm được backdoor chúng giấu kỹ nhất.
YARA không phải siêu anh hùng. Nó không tự nghĩ ra gì cả. Nhưng trong tay một đội SOC hiểu việc, nó biến dữ liệu thành bản đồ dẫn tới kẻ phá hoại.
2. Viết rule: Khoa học và kiên nhẫn
Kinh nghiệm dạy rằng vội vàng là chết. Viết YARA rule không phải trò may rủi, mà là khoa học pha chút nghệ thuật. Đây là cách làm, đúc kết từ những lần “tủi hổ và nước mắt (do sếp chửi)”:
--Moi ruột mã độc: Dùng IDA, Ghidra, hoặc chỉ cần strings để tìm dấu hiệu. Chuỗi “cmd.exe”, mã hex “DE AD BE EF”, hay regex cho C2 lắt léo – đó là vàng trong đống rác.
--Xây dựng khung: Rule gồm meta để ghi chú, strings để định vị, condition để ra đòn. Đừng làm phức tạp – đơn giản mà hiệu quả là triết lý sống sót trong nghề.
--Tinh chỉnh: Thêm filesize < 1MB hay kiểm tra PE header (uint16(0) == 0x5A4D) để tránh báo động nhầm. Một lần, rule báo động cả đống file Word vì quên giới hạn – sếp nhìn như muốn đuổi cả đội.
--Thử lửa: Chạy trên dữ liệu sạch và bẩn trước khi tung vào hệ thống. Drama không ai muốn: SOC nháo nhào vì rule khớp script backup của IT.
👉Rule ngon giống pha cà phê – đúng liều, đúng nhiệt, và chút kiên nhẫn.
4. Ứng dụng thực chiến: Phát hiện Lazarus trên IIS 🌶️ Đây là case thực tế hiện ghi nhận tấn công vào 14/3.
Nhóm Lazarus – đám Triều Tiên lì lợm – là kiểu đối thủ vừa đáng ghét vừa đáng nể. Chúng tấn công ngân hàng, nhúng backdoor vào IIS, và để lại dấu vết như trêu ngươi: “Tìm đi, nếu đủ giỏi”.
Bối cảnh ví dụ
Tháng trước, một ngân hàng nhỏ – gọi là Ngân hàng X – thấy server IIS “ho khan”: latency tăng, log đầy request POST từ IP Đông Á. Đội junior nháo nhào, nhưng ly cà phê nguội trên bàn vẫn nhắc rằng: “Bình tĩnh, YARA sẽ xử lý.”
IoC của Lazarus
Lazarus thích nhúng DLL hoặc ASPX vào IIS. Báo cáo từ MITRE và Kaspersky chỉ ra:
--Lệnh shell: cmd.exe /c, đôi khi powershell.exe.
--Web shell: Hàm eval() hoặc Server.Execute() trong ASPX.
--C2: Chuỗi “http://” hoặc Base64 dẫn tới domain ngẫu nhiên.
Rule YARA cho IIS
Dựa trên kinh nghiệm qua vài trận chiến với Lazarus, rule này được viết:
###
rule Lazarus_IIS_Hunter {
    meta:
        description = "Tracks Lazarus APT backdoors in IIS - seen too many of these"
        author = "Ke Chem Gio"
        date = "2025-03-14"
        wisdom = ###"
    strings:
        $shell_cmd = "cmd.exe /c" ascii fullword
        $shell_ps = "powershell.exe" ascii fullword
        $web_eval = "eval(" ascii
        $web_exec = "Server.Execute(" ascii
        $http_hex = { 68 74 74 70 3A 2F 2F } // "http://"
    condition:
        filesize < 500KB // Small fries, like most web shells
        and (uint16(0) == 0x4D5A or uint32(0) == 0xEFBBBF) // PE or ASPX
        and (
            any of ($shell*) // Shell execution
            or any of ($web*) // Web shell tricks
            or $http_hex     // C2 beacon
        )
}
###
Thực thi và kết quả
Lệnh được chạy: yara -r lazarus_iis_hunter.yar C:\inetpub\wwwroot. 
Mười phút sau, YARA báo động file patch.aspx. Nội dung bên trong:
###
<%@ Page Language="C#" %>
<% System.Diagnostics.Process.Start("cmd.exe", "/c whoami > C:\\temp\\out.txt"); %>
###
Đúng phong cách Lazarus – đơn giản, hiệu quả, và hơi “lầy”. Log IIS xác nhận: request POST từ 203.176.x.x, kèm dữ liệu Base64 gọi về C2.
Nụ cười khô khan thoáng qua: “Nó vẫn thế – tinh vi nhưng không đủ kín.” File bị xóa, server được cô lập, báo cáo ghi: “Lazarus 0 – YARA 1.
Sếp khen: Được đấy! Nhưng chắc chắn là lương sẽ không tăng 😞
P/s: Bài viết đủ để cho anh em hình dung được YARA và ứng dụng thực tế của nó. Với văn của một kỹ thuật khô khan như mình, chắc chắn là phải có AI trợ viết rồi. Đọc cho vui và bổ sung kiến thức nhé!

![alt text](image-5.png)