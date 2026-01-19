# Deployment Guide

## Prerequisites
- Ubuntu server (AWS EC2 or similar)



## 1. Server Setup

### Update system packages
```bash
sudo apt update
sudo apt upgrade -y
```

### Install required packages
```bash
sudo apt install python3-pip python3-venv nginx -y
```

## 2. Project Setup

### Clone your repository
```bash
cd ~
git clone <your-repo-url>
cd ShopClubProject4
```

### Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configure Django settings
```bash
nano config/settings.py
```

Update the following:
- `DEBUG = False`
- `ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address']`
- Configure your database settings
- Set a strong `SECRET_KEY`

### Run migrations
```bash
python manage.py migrate
python manage.py collectstatic
```

## 3. Gunicorn Setup

### Create systemd service file
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

### Add the following content:
```ini
[Unit]
Description=gunicorn daemon for ShopClub
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/ShopClubProject4
Environment="PATH=/home/ubuntu/ShopClubProject4/venv/bin"
ExecStart=/home/ubuntu/ShopClubProject4/venv/bin/gunicorn \
          --workers 3 \
          --umask 0007 \
          --bind unix:/home/ubuntu/ShopClubProject4/shopclub.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Enable and start Gunicorn
```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

## 4. Nginx Setup

### Create Nginx configuration
```bash
sudo nano /etc/nginx/sites-available/shopclub
```

### Add the following content:
```nginx
server {
    listen 80;
    server_name your-domain.com your-ip-address;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/ubuntu/ShopClubProject4;
    }

    location /media/ {
        root /home/ubuntu/ShopClubProject4;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/ShopClubProject4/shopclub.sock;
    }
}
```

### Enable the site
```bash
sudo ln -s /etc/nginx/sites-available/shopclub /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 5. File Permissions

### Set correct permissions
```bash
sudo chmod 755 /home/ubuntu
sudo chmod 755 /home/ubuntu/ShopClubProject4
sudo usermod -aG ubuntu www-data
```


## 8. Verify Deployment

Check that all services are running:
```bash
sudo systemctl status gunicorn
sudo systemctl status nginx
```

Visit your site at `http://your-ip-address`

## Managing the Application

### Restart Gunicorn after code changes
```bash
sudo systemctl restart gunicorn
```

### View Gunicorn logs
```bash
sudo journalctl -u gunicorn -n 50 --no-pager
```

### View Nginx logs
```bash
sudo tail -n 50 /var/log/nginx/error.log
sudo tail -n 50 /var/log/nginx/access.log
```

### Restart Nginx
```bash
sudo systemctl restart nginx
```

## Troubleshooting

### 502 Bad Gateway Error
- Check Gunicorn status: `sudo systemctl status gunicorn`
- Check permissions on socket file: `ls -la /home/ubuntu/ShopClubProject4/shopclub.sock`
- Check Nginx error logs: `sudo tail -n 100 /var/log/nginx/error.log`

### Static files not loading
- Run `python manage.py collectstatic`
- Check Nginx configuration for correct static file path
- Verify file permissions

### Application changes not reflecting
```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart gunicorn
```

