| Trường dữ liệu | Thiếu khóa / Null | Sai kiểu (Type Error) | Ngoài miền (Vd: số âm) | Hành vi / Kết quả hệ thống |
|---|---|---|---|---|
| `tuoi` | Báo THEO_DOI (ERR-AGE) | Báo THEO_DOI (ERR-AGE) | Báo THEO_DOI (ERR-AGE) | Bỏ qua phân loại mức nặng vì thiếu tuổi tính ranh giới. |
| `huyet_ap_tam_thu` | Bỏ qua xét R-SOC | Crash (nếu ném string) -> Báo lỗi | Không áp dụng | Nếu HATT lỗi, không xét tụt HA nhưng **VẪN XÉT** các rule Tầng 2 (R01, R02). Nếu đủ 2 triệu chứng, vẫn trả `PHAN_VE`. |
| Các trường `bool` | Mặc định là `False` | Trả `True` (nếu string "false") | Không áp dụng | Lỗi ép kiểu `bool` sẽ được hệ thống Harden ở M3 sửa, hiện tại mặc định `False` nếu thiếu. |
| **Trùng Rule** | N/A | N/A | N/A | Ưu tiên cao nhất: R01 > R02 > R03 (theo Issue #15). |