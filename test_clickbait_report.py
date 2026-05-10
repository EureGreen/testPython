import pytest
from src.reports.clickbait_report import ClickbaitReport

@pytest.fixture
def sample_videos():
    return [
        {"title": "A", "ctr": 20.0, "retention_rate": 30.0},
        {"title": "B", "ctr": 18.0, "retention_rate": 50.0},  # не подходит (удержание)
        {"title": "C", "ctr": 10.0, "retention_rate": 25.0},  # не подходит (ctr)
        {"title": "D", "ctr": 25.0, "retention_rate": 35.0},
        {"title": "E", "ctr": 16.0, "retention_rate": 39.0},
    ]

def test_clickbait_filter(sample_videos):
    report = ClickbaitReport()
    result = report.filter_videos(sample_videos)
    
    titles = [v['title'] for v in result]
    assert titles == ["D", "A", "E"]  # сортировка по убыванию CTR (25, 20, 16)
    assert all(v['ctr'] > 15 and v['retention_rate'] < 40 for v in result)

def test_clickbait_columns():
    report = ClickbaitReport()
    assert report.columns() == ["title", "ctr", "retention_rate"]

def test_clickbait_name():
    report = ClickbaitReport()
    assert report.name == "clickbait"