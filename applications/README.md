Launchpad Tracker

A full-stack Job Application Tracker built with Django REST Framework (backend) and vanilla JavaScript (frontend), deployed on AWS EC2 with Nginx and Gunicorn.

⸻

Features
• Add job applications
• Delete applications
• Track application status
• Persistent database
• Fully deployed and accessible via public IP

⸻

Tech Stack
• Backend: Django + Django REST Framework
• Frontend: HTML, CSS, JavaScript (Fetch API)
• Server: AWS EC2 (Ubuntu)
• Web Server: Nginx
• App Server: Gunicorn

⸻

Project Setup (Local Development)

1. Clone Repository

git clone
cd launchpad

2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install django djangorestframework gunicorn

4. Run Migrations

python manage.py makemigrations
python manage.py migrate

5. Start Server

python manage.py runserver

⸻
Backend (Django API)

Model

class Application(models.Model):
company = models.CharField(max_length=100)
role = models.CharField(max_length=100)
status = models.CharField(max_length=50)

Serializer

class ApplicationSerializer(serializers.ModelSerializer):
class Meta:
model = Application
fields = ‘all’

View

class ApplicationViewSet(viewsets.ModelViewSet):
queryset = Application.objects.all()
serializer_class = ApplicationSerializer

URLs

router.register(r’application’, ApplicationViewSet)

⸻

Frontend

Create

fetch(“http:///application/”, {
method: “POST”,
headers: {
“Content-Type”: “application/json”
},
body: JSON.stringify({ company, role, status })
})

Delete

fetch(http://<server-ip>/application/${id}/, {
method: “DELETE”
})

Load Data

fetch(“http:///application/”)

⸻

Deployment (AWS EC2)

1. Launch EC2
   • Ubuntu
   • Open ports: 22, 80

2. SSH

ssh -i key.pem ubuntu@

3. Install Packages

sudo apt update
sudo apt install python3-pip python3-venv nginx -y

4. Setup Project

git clone
cd launchpad

python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework gunicorn

5. Migrate

python manage.py migrate

⸻

Gunicorn Setup

Test

gunicorn launchpad.wsgi:application –bind 0.0.0.0:8000

Service

sudo nano /etc/systemd/system/gunicorn.service

Paste:

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/launchpad
ExecStart=/home/ubuntu/launchpad/venv/bin/gunicorn \
–workers 3 \
–bind 127.0.0.1:8000 \
launchpad.wsgi:application

[Install]
WantedBy=multi-user.target

Start

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

⸻

Nginx Configuration

sudo nano /etc/nginx/sites-available/default

Paste:

server {
listen 80;
server*name *;
root /var/www/html;  
index index.html;

location / {  
 try_files $uri $uri/ =404;  
}

location /application/ {  
 proxy_pass http://127.0.0.1:8000;  
 proxy_set_header Host $host;  
 proxy_set_header X-Real-IP $remote_addr;  
}

}

Restart

sudo nginx -t
sudo systemctl restart nginx

⸻
Upload Frontend

scp -i key.pem index.html ubuntu@:/var/www/html/

⸻
Final Result

Frontend: http://
API: http:///application/

Key Concepts
• REST API with Django
• Frontend-backend integration
• EC2 deployment
• Nginx reverse proxy
• Gunicorn process management

⸻

🎯 Conclusion

This project demonstrates a complete full-stack deployment pipeline from development to production using industry-standard tools.
