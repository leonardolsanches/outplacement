# Overview

This is a digital outplacement platform designed to assist executives in their career transition journey. The platform provides individualized support for career planning, professional development, and job placement assistance. It offers comprehensive services including professional profile assessment, resume optimization, interview training, networking guidance, and progress tracking. The system manages the entire outplacement process from initial consultation through successful job placement, with built-in KPI monitoring and SLA compliance tracking.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Backend Framework
- **Flask-based Python web application** - Chosen for rapid development and simplicity, suitable for the platform's requirements of user management, session scheduling, and reporting
- **Flask-Login integration** - Provides user session management and authentication with role-based access control (admin, consultant, executive)
- **JSON file-based data storage** - Uses local JSON files for data persistence, eliminating database setup complexity while maintaining data structure

## Frontend Architecture
- **Server-side rendered templates** - Uses Jinja2 templating engine for dynamic HTML generation
- **Bootstrap 5 responsive framework** - Ensures mobile-friendly interface with consistent styling across devices
- **Font Awesome icons** - Provides professional iconography throughout the interface
- **Vanilla JavaScript** - Handles client-side interactions, form validation, and UI enhancements without framework dependencies

## Data Management
- **File-based JSON storage** - Separate JSON files for different data entities (users, executives, sessions, reports, KPIs)
- **Auto-initialization system** - Creates necessary data directories and files on first run
- **Structured data models** - Clear separation between user accounts, executive profiles, session records, and performance metrics

## Authentication & Security
- **Werkzeug password hashing** - Uses secure scrypt algorithm for password storage
- **Session-based authentication** - Flask-Login manages user sessions with secure session cookies
- **Role-based access control** - Three user roles (admin, consultant, executive) with different permission levels
- **Secret key configuration** - Application uses configured secret key for session security

## Core Modules
- **User Management** - Registration, login, role assignment, and profile management
- **Executive Tracking** - Complete executive profile management with competency mapping
- **Session Scheduling** - Calendar-based appointment system with different session types
- **Interview Simulator** - Training module with different interview scenarios (behavioral, technical, leadership)
- **Progress Reporting** - KPI tracking and performance analytics with export capabilities
- **SLA Monitoring** - Automated tracking of response times and service level compliance

## Design Patterns
- **MVC Architecture** - Clear separation of models (JSON data), views (templates), and controllers (Flask routes)
- **Component-based UI** - Reusable template blocks and consistent styling patterns
- **RESTful API structure** - Following REST principles for route organization and data handling

# External Dependencies

## Frontend Libraries
- **Bootstrap 5.1.3** - CSS framework for responsive design and component styling
- **Font Awesome 6.0.0** - Icon library for consistent visual elements
- **Bootstrap JavaScript** - Interactive components like dropdowns, alerts, and tooltips

## Python Packages
- **Flask** - Core web framework for application structure
- **Flask-Login** - User session management and authentication
- **Werkzeug** - Password hashing utilities and security features

## Development Tools
- **JSON file system** - No external database required, uses local file storage
- **Static file serving** - CSS and JavaScript served through Flask's static file handling

## Browser Requirements
- **Modern web browsers** - Requires JavaScript support for interactive features
- **Bootstrap compatibility** - Supports all browsers compatible with Bootstrap 5

Note: The application is designed to be self-contained with minimal external dependencies, making deployment straightforward without requiring database setup or complex external service integrations.