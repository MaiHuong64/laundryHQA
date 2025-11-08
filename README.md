# HQA Project - Ứng dụng Web Flask tích hợp Tailwind CSS v4

##  Giới Thiệu

Dự án này là một Boilerplate (khuôn mẫu) cho ứng dụng web được xây dựng bằng **Flask** (Python) cho Backend và **Tailwind CSS v4** cho giao diện Frontend.

## Yêu Cầu Hệ Thống (Prerequisites)

Để thiết lập và chạy dự án, máy tính của bạn cần có:

1.  **Python 3.8+** và **pip** (để quản lý Backend).
2.  **Node.js** và **npm** (để quản lý Tailwind CSS).


##  Hướng Dẫn Cài Đặt & Khởi Chạy

Thực hiện các bước sau theo thứ tự để thiết lập môi trường và khởi chạy ứng dụng.

### Bước 1: Thiết lập Môi trường Python (Backend)

Đảm bảo bạn đang ở thư mục gốc của dự án.

1.  **Tạo và Kích hoạt Môi trường Ảo (`venv`):**
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt (Windows Command Prompt/PowerShell)
venv\Scripts\activate.bat
 
2.  **Cài đặt các Gói Python:**
# Cài đặt Flask (và các dependencies khác nếu có)
pip install Flask 
### Bước 2: Thiết lập Frontend (Tailwind CSS)

1.  **Cài đặt Dependencies của Node.js:**
# Cài đặt tailwindcss và công cụ CLI
npm install tailwindcss @tailwindcss/cli

2.  **Khởi chạy Bộ Biên dịch Tailwind (Bắt buộc):**
Bạn cần giữ lệnh này chạy trong một Terminal riêng biệt suốt quá trình phát triển. Lệnh này sẽ biên dịch CSS từ `src/input.css` ra `app/public/output.css`.
npm run tailwind

### Bước 3: Khởi chạy Ứng dụng Flask

Sau khi môi trường Python được kích hoạt (bước 1) và Tailwind Compiler đang chạy (bước 2):

3.  **Truy cập:**
Ứng dụng sẽ khả dụng tại: `http://127.0.0.1:5000/`


Nếu cần thoát khỏi môi trường ảo
deactivate
