import tempfile
import csv
from src.utils import read_videos_from_csv

def test_read_videos_from_csv():
    content = """title,ctr,retention_rate,views
Video1,15.5,45,1000
Video2,20.0,30,2000
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        f.flush()
        videos = read_videos_from_csv(f.name)
    
    assert len(videos) == 2
    assert videos[0]['title'] == 'Video1'
    assert videos[0]['ctr'] == 15.5
    assert videos[1]['retention_rate'] == 30.0

def test_read_csv_with_missing_column():
    content = """title,views
Video1,1000
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        f.flush()
        videos = read_videos_from_csv(f.name)
    
    assert len(videos) == 0  # некорректная строка пропущена