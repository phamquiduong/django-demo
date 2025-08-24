## Cài đặt môi trường ảo cho Python (không bắt buộc)
#### Tạo môi trường ảo
```powershell
python -m venv .venv
```

#### Kích hoạt môi trường ảo
```powershell
.\.venv\Scripts\Activate.ps1
```

> [!CAUTION]
> Nếu bị lỗi thì mở **PowerShell** với quyền admin, chạy lệnh sau và thử lại
> ```powershell
> Set-ExecutionPolicy Unrestricted -Force
> ```

<br>

## Chuẩn bị cho dự án
#### Bước 1: Cài đặt gói thư viện cho Python
```powershell
.\run_pip_install.bat
```

#### Bước 2: Cập nhật cấu trúc Database
```powershell
.\run_migrate.bat
```

<br>

## Chạy server
```powershell
.\run_server.bat
```

> [!NOTE]
> Khi bắt đầu chạy script sẽ hỏi bạn về `cổng mạng (port)` của server. Nếu để trống mặc định là **80**.<br>
> Bạn truy cập `http://localhost:<cổng mạng>` để vào được website.

<br>

## Chạy test
```powershell
.\run_tests.bat
```
