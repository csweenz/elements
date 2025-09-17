# Infra

This folder is for infrastructure as code, deployment scripts, and related resources.

- Add Terraform, Ansible, Docker, or other infra scripts here as needed.



cd ./backend
source venv/bin/activate
python manage.py runserver

cd ./frontend
pnpm dev

GET /api/elements/ (DRF viewset)
GET /api/elements/Cu/ (lookup by symbol)
GET /api/element-prices/?symbol=Cu&latest=true
GET /api/elements/Cu/echo/ (simple function view)