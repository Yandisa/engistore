# ⚙️ EngiStore – Engineering Inventory & Asset Management System

**EngiStore** is a powerful, scalable, and user-friendly web-based inventory system designed for engineering environments such as factories, workshops, and maintenance departments. It offers complete visibility into parts, assets, and part usage, enabling traceability, accountability, and efficiency in stock management.

Whether you’re managing spare parts for machinery, tools for maintenance, or components for operations — EngiStore empowers your team with streamlined processes, role-based access, and actionable insights.

---

## 🧠 Purpose

Built for technical teams with minimal admin resources, EngiStore allows organizations to:
- Reduce downtime by ensuring parts are available when needed.
- Track usage and consumption of parts per asset or task.
- Empower technicians with quick access to inventory data.
- Enable managers to make data-driven purchasing decisions.
- Maintain a digital audit trail for every part movement.

---

## ✅ Current Core Features

### 🧩 Inventory & Parts Management
- Create, view, and edit parts with details like part number, description, category, and location.
- Structured location: room, aisle, bin number.
- Track stock quantities & reorder thresholds.
- Search and filter by name, part number, category, and low stock.

### 🛠 Asset Tracking
- Manage company assets such as machines, tools, and vehicles.
- View all parts used on each asset.
- Associate part usage with specific assets and users.

### 🧾 Stock Usage Logging
- Take parts from stock via the part detail page.
- Log who took the part, when, why, and for which asset.
- Auto deduct quantity from inventory.
- Prevent overuse through validation.

### 📩 Part Requests System
- Users can request parts not currently available.
- Multi-step request approval flow:
  - Pending → Approved → Delivered → Rejected
- Technicians & Viewers can submit requests.
- Admins/Managers can review and update statuses.

### 📊 Dashboard Overview
- Total number of parts, assets, and low-stock items.
- Recently added parts and recent usage logs.
- Quick links to essential functions.

### 👤 User Roles & Permissions
- 🔐 Role-based control using Django groups:
  - **Admin**: Full access including user management.
  - **Manager**: Approve requests and take parts.
  - **Technician**: Take parts, log usage, request parts.
  - **Viewer**: Read-only access.

### 📋 Usage History
- Log and view who took what, when, why, and for what asset.
- Fully traceable audit trail with user accountability.

---

## 🔮 Planned Features (Future Versions)

The goal is to evolve EngiStore into a full-service operations tool. Upcoming features include:

### 📈 Reporting & Insights
- Downloadable reports (CSV, PDF) for usage, requests, and part levels.
- Charts: Most used parts, low stock trends, usage per asset.

### 💬 In-App Help Assistant (Chatbot)
- Interactive bot to guide users step-by-step.
- Contextual help based on the page (e.g. "How do I take a part?").

### 🧑‍💼 User Management Enhancements
- User creation with email invites.
- Role editing and user activation/deactivation.

### 💰 Procurement Integration
- Link suppliers to parts.
- Create purchase orders for low-stock items.
- Track order history per part.

### 🌍 Multi-Store Locations
- Manage parts across multiple warehouses.
- Assign store locations to users.

### 🎨 UI/UX Improvements
- Dark/light theme toggle.
- Responsive sidebar and mobile-friendly modals.
- Notifications for approvals and stock alerts.

### 🧠 AI Assistant (Future Stretch Goal)
- Suggest parts based on asset history.
- Predict reorder needs using usage trends.

---

## 🧰 Tech Stack

| Component        | Technology              |
|------------------|--------------------------|
| Backend          | Django (Python)          |
| Frontend         | HTML, CSS, Bootstrap 5   |
| Database         | SQLite (default)         |
| User Management  | Django Auth + Groups     |
| Template Engine  | Django Templates (Jinja) |
| Deployment Ready | Render / Railway / Intranet |

---

## ⚙️ Installation Instructions (Plug & Play)

1. **Clone the repository**
```bash
git clone https://github.com/Yandisa/engistore.git
cd engistore
```

2. **Create a virtual environment**
```bash
python -m venv env
env\Scripts\activate  # On Windows
```

3. **Install requirements**
```bash
pip install -r requirements.txt
```

4. **Apply migrations & create a superuser**
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Start the server**
```bash
python manage.py runserver
```

6. **Login and explore**
- Open your browser: `http://127.0.0.1:8000/`
- Default login page: `/accounts/login/`

---

## 🛠 Customization & Deployment

- You can tailor this system for medical supplies, school labs, automotive parts, etc.
- For internal company use, simply host it on a local network (intranet).
- Easily extensible with supplier modules, stock transfer, and QR/barcode scanning.

---

## 📌 Target Users

- Workshop managers
- Maintenance teams
- Engineers
- Storekeepers
- Factory operations personnel
- Technicians and interns

---

## 👨‍💻 Developer

**Yandisa** – Python & Django Developer  
🎓 Background: Mechanical Technician | Software Engineering Bootcamp Graduate  
🚀 Freelancing & building custom internal tools  
🌐 Portfolio: [yandisa.github.io/MyCV](https://yandisa.github.io/MyCV)  
📬 [GitHub](https://github.com/Yandisa)

---

## 📄 License

This project is released for personal, educational, and freelance use.  
For commercial licensing, customization, or company deployment, contact the developer.

---

> **EngiStore** was built to solve a real problem — and it works!  
> Now you can improve part accountability and reduce downtime in your workshop 💪