# Task Manager App

## Overview
The **Task Manager App** is a simple web application built with Django that allows users to manage personal tasks after logging in. It incorporates Google Login for authentication, token-based login, and email-based user invitations. Additionally, the app includes an admin panel for managing OAuth keys and sending email invitations.

---

## Features

### **1. User Authentication**
- **Google Login**: Users can log in using their Google accounts, and their data is securely stored in the backend.
- **Email-Based Login**: An alternative to Google login, allowing users to register and log in using their email addresses. A JWT token is generated upon successful login.

### **2. Task Management**
- Users can **create**, **view**, **edit**, and **delete tasks**.
- Each task includes:
  - **Title**: A brief description of the task.
  - **Description**: Detailed information about the task.

### **3. Admin Panel**
- Manage Google OAuth keys securely.
- Option to send registration emails:
  - **Via API**: Admin users can invite new users through an API.
  - **Admin Panel**: Add user details directly in the admin panel to send email invitations.

---

## Technical Implementation

### **1. Google Login Flow**
- Google OAuth is implemented to verify tokens and authenticate users.
- Backend verifies the Google token using Google's API and stores user details in the database.

### **2. Email Invitations**
- Admins can send registration links via email:
  - **Option 1**: Using the admin panel interface.
  - **Option 2**: Through a POST API if the admin has valid credentials.

### **3. Token Generation**
- JWT tokens are used for user authentication after a successful login, providing secure access to the app.

---

## API Endpoints

### **User Authentication**
- **Google Login API**: Verifies the Google token and authenticates the user.
- **Email Login API**: Authenticates users using email and returns a JWT token.

### **Task Management**
- **Create Task API**: Adds a new task to the user's account.
- **View Task API**: Lists all tasks created by the user.
- **Edit Task API**: Updates task details.
- **Delete Task API**: Removes a task from the user's account.

---

## Admin Panel Features
- Manage Google OAuth credentials for the app.
- Send user registration emails:
  - Add user details in the admin panel.
  - Trigger emails with a pre-defined registration link.

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   

## Install Dependencies
- **pip install -r requirements.txt**
- Install dependencies from requirements.txt file & start project
