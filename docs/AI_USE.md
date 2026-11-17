# Nhật ký sử dụng Trí tuệ Nhân tạo (AI-Use Log)
**Dự án:** Track A (Dr May Day Rule Engine Sprint.  
**Nhóm:** 49

Bảng dưới đây liệt kê những sự trợ giúp của AI đã được nhóm sử dụng để hỗ trợ trong quá trình phát triển dự án và quyết định của nhóm.

| Công cụ | Mục đích | Phạm vi | Kiểm chứng | Quyết định của nhóm | Người chịu trách nhiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **gemini/ chatgpt** | Giải thích cấu trúc chuẩn WAO/EAACI và tư duy thiết kế hệ thống Rule Engine. | File `ADR-001-rule-engine-design.md` và `REQUIREMENTS.md` (Checkpoint 1). | Đối chiếu tài liệu y khoa do AI cung cấp. | **Sửa:** Chỉ lấy ý tưởng về kiến trúc, tự viết lại báo cáo cho phù hợp với dự án. | Lộc (202414220)|
| **gemini/chatgpt** | Hỗ trợ debug lỗi môi trường ảo, lỗi Git và cấu hình chạy Pytest lúc đầu. | Môi trường phát triển cục bộ, không tác động trực tiếp vào file mã nguồn. | Gõ lại các lệnh terminal do AI gợi ý (như cách activate venv, xử lý xung đột git). | **Giữ:** Sử dụng các lệnh fix lỗi vì đã giải quyết được vấn đề chạy Pytest thành công. | Lộc (202414220) |
| **Gemini** | Gợi ý cách lên kịch bản test cho các ngưỡng tuổi và huyết áp. | File `TEST_PLAN.md` và các test case trong Pytest (PR #1). | Trực tiếp chạy `pytest` để đảm bảo các ca bệnh giả định pass qua Rule Engine. | **Sửa:** Nhóm điều chỉnh lại các con số test case sát ngưỡng huyết áp thực tế của hệ thống. | Lộc (202414220) |
| **chatgpt** | Tham khảo cấu trúc code logic cho tính năng Audit Log (A-06) và Medical Disclaimer (A-11). | Module mã nguồn chứa tính năng A-06, A-11 và PR #1. | Đọc hiểu logic theo tư duy khối rẽ nhánh (if/else), chạy kiểm thử cục bộ pass 100%. | **Sửa & Loại:** Giữ lại logic cốt lõi, nhưng loại bỏ các biến thừa do AI tựa bịa ra để đồng nhất với cấu trúc repo `loc220/ktpmud-bkt-ruleengine-starter`. | Lộc (202414220) |