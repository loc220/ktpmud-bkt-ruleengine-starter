"""Rule Engine WAO/EAACI - khung bai tap BKT-1 (Track A), mon KTPMUD.

Sinh vien hien thuc ham classify() theo dac ta trong docs/decision-table.md.
KHONG tu dat nguong/quy tac moi chua co trong dac ta.
"""
import time
import uuid

def _ghi_audit(status):
    """Hàm phụ trợ ghi log audit đáp ứng tiêu chí A-06 (Zero PII)."""
    log_entry = {
        "Timestamp": time.time(),
        "User_UUID": str(uuid.uuid4()),
        "Action_Type": "CLASSIFY_ANAPHYLAXIS",
        "Status": status
    }
    print(f"AUDIT LOG: {log_entry}")

def safe_bool(val):
    if isinstance(val, str) and val.lower() == "false": return False
    return bool(val)

def classify(patient_data: dict) -> dict:
    if not isinstance(patient_data, dict): return {"muc_do": "THEO_DOI", "ly_do": "ERR-INPUT"}
    
    tuoi = patient_data.get("tuoi")
    # Kiểm tra tuổi nghiêm ngặt (A-04)
    if isinstance(tuoi, bool) or not isinstance(tuoi, (int, float)) or tuoi < 0:
        _ghi_audit("FAILED_INVALID_AGE")
        return {"muc_do": "THEO_DOI", "ly_do": "ERR-AGE"}

    # Lấy HATT nghiêm ngặt: Bắt buộc là số int hoặc float, cấm dùng chuỗi "80"
    hatt_raw = patient_data.get("huyet_ap_tam_thu", 999)
    if isinstance(hatt_raw, bool) or not isinstance(hatt_raw, (int, float)):
        hatt = 999  # Nếu sai kiểu, vô hiệu hóa việc xét tụt huyết áp
        _ghi_audit("WARNING_INVALID_HATT")
    else:
        hatt = hatt_raw

    co_di_nguyen = safe_bool(patient_data.get("co_di_nguyen_nghi_ngo", False))
    ton_thuong_da = safe_bool(patient_data.get("co_ton_thuong_da_niem_mac", False))
    trieu_chung_ho_hap = safe_bool(patient_data.get("co_trieu_chung_ho_hap", False))
    trieu_chung_tuan_hoan = safe_bool(patient_data.get("co_trieu_chung_tuan_hoan", False))
    trieu_chung_tieu_hoa = safe_bool(patient_data.get("co_trieu_chung_tieu_hoa_nang", False))
    
    # Xét Tầng 1: R-SOC
    if tuoi >= 11: nguong_huyet_ap = 90
    else: nguong_huyet_ap = 70 + (2 * tuoi)
    
    if hatt < nguong_huyet_ap:
        _ghi_audit("SUCCESS_CLASSIFIED_RSOC")
        return {"muc_do": "SOC_PHAN_VE", "ly_do": "R-SOC"}
    
    # Xét Tầng 2: R01-PV
    if ton_thuong_da and trieu_chung_ho_hap and not co_di_nguyen:
         _ghi_audit("SUCCESS_CLASSIFIED_R01")
         return {"muc_do": "PHAN_VE", "ly_do": "R01-PV"}
         
    # Xét Tầng 2: R02-PV
    trieu_chung_dem = sum([ton_thuong_da, trieu_chung_ho_hap, trieu_chung_tuan_hoan, trieu_chung_tieu_hoa])
    if co_di_nguyen and trieu_chung_dem >= 2:
        _ghi_audit("SUCCESS_CLASSIFIED_R02")
        return {"muc_do": "PHAN_VE", "ly_do": "R02-PV"}

    _ghi_audit("SUCCESS_CLASSIFIED_NO_MATCH")
    return {"muc_do": "THEO_DOI", "ly_do": "NO-MATCH"}