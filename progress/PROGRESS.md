# PROGRESS — nhom49 — Track A
Starter: ktpmud-bkt-ruleengine-starter · tag bkt-2026-v1.1
Fork: https://github.com/loc220/ktpmud-bkt-ruleengine-starter

## PC-1 — 11/11/2026
### 1.1. Tiến độ theo acceptance criteria
| Mã | Trạng thái (Chưa / Đang / Xong) | Bằng chứng (commit / CI / file) | Ghi chú |
|---|---|---|---|
| A-01 | Xong | docs/decision-table.md | Đã nộp CP1 |
| A-02 | Xong | rule_engine/classifier.py | Đã nộp CP1 |
| A-03 | Xong | rule_engine/classifier.py | Đã nộp CP1 |
| A-04 | Xong | rule_engine/classifier.py | Đã nộp CP1 |
| A-05 | Xong | rule_engine/classifier.py | Đã nộp CP1 |
| A-06 | Xong | rule_engine/classifier.py | Đã có Audit Zero PII |
| A-07 | Xong | tests/test_classifier.py | Đã nộp CP1 |
| A-08 | Xong | pytest -q | 4 passed |
| A-09 | Xong | GitHub Actions (CI) pass | CI tự động chạy |
| A-10 | Xong | run_benchmark.py | p95 < 100ms |
| A-11 | Xong | README.md | Đã thêm miễn trừ y khoa |

### 1.2. Sửa đổi bắt buộc từ Checkpoint 1
| Mục | Trạng thái | Bằng chứng |
|---|---|---|
| Không có | | |

### 1.3. Timeline dự kiến đến khi hoàn thành
| Việc | Vai trò phụ trách | Mốc (CP2 15/11 · M3 · Freeze 19/11 · M4 20/11) | Ngày dự kiến |
|---|---|---|---|
| Chuẩn bị script demo nội bộ | BE-1 | CP2 15/11 | 14/11/2026 |
| Bổ sung tài liệu bảo mật | QA-1 | M3 | 16/11/2026 |
| Draft PR check validate xanh | Lead | PC-2 18/11 | 17/11/2026 |
| Nộp PR chính thức | Lead | M4 20/11 | 20/11/2026 |

### 1.4. Rủi ro / đang vướng
Không có.

### 1.5. Câu hỏi cho GV
Q1: Nhóm đã làm xong toàn bộ A-01 đến A-11, em có thể nộp Draft PR sớm để lấy check validate xanh luôn được không ạ?

### 1.6. Phân công (alias hoặc vai trò, KHÔNG ghi họ tên/MSSV)
| Alias / vai trò | Đầu việc chính | Commit/PR tiêu biểu |
|---|---|---|
| Lead | Quản lý dự án, nộp bài | Các commit merge |
| BE-1 | Code logic, benchmark | classifier.py |
| QA-1 | Unit test, tài liệu | test_classifier.py |
