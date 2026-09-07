# Instagram Engagement Checker

Instagram 게시물 URL이 포함된 Excel 파일을 업로드하면
각 게시물의 좋아요 수와 댓글 수를 자동으로 수집해
결과 Excel 파일로 내려받을 수 있는 경량 웹 애플리케이션입니다.

## Features

- Excel 파일 업로드
- Instagram 게시물 URL 자동 탐색
- 좋아요 수 수집
- 댓글 수 수집
- 조회 상태 기록
- 조회 시각 기록
- 결과 Excel 다운로드

### 🔗 Live Demo

[Instagram Engagement Checker](https://instagramchecker.streamlit.app/)

## Tech Stack

- Python
- Streamlit
- Instaloader
- openpyxl

## Project Structure

```text
instagram-engagement-checker/

├── app.py
├── instagram_service.py
├── excel_service.py
├── requirements.txt
└── README.md
