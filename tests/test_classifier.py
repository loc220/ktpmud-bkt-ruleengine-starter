"""Vi du minh hoa dinh dang test - KHONG phai bo test an dung de cham diem.
Sinh vien tu viet them test cho du cac muc do theo dac ta (docs/decision-table.md).
"""
import pytest
from rule_engine.classifier import classify

def test_boundary_age_11():
    assert classify({"tuoi": 10.99, "huyet_ap_tam_thu": 91})["muc_do"] == "SOC_PHAN_VE"

    assert classify({"tuoi": 11.0, "huyet_ap_tam_thu": 91})["muc_do"] == "THEO_DOI"
def test_invalid_and_missing_input():
    assert classify({"tuoi": 20, "huyet_ap_tam_thu": "80"})["muc_do"] == "THEO_DOI" # Tạm trả THEO_DOI

    assert classify({"tuoi": 20, "co_trieu_chung_ho_hap": "false"})["muc_do"] == "THEO_DOI" 

def test_issue_15_missing_hatt_but_rule_2():

    ca_issue_15 = {
        "tuoi": 20,
        "co_di_nguyen_nghi_ngo": True,
        "co_ton_thuong_da_niem_mac": True,
        "co_trieu_chung_ho_hap": True
    }
  
    assert classify(ca_issue_15)["muc_do"] == "PHAN_VE"