# Md. Muqtadir Fuad - Academic & Engineering Portfolio

A professional, minimalist portfolio website for **Md. Muqtadir Fuad**, an undergraduate student at BUET with interests in machine learning, NLP, operations research, and smart manufacturing.

## Overview

This application is a full-stack web portfolio designed to showcase academic research, engineering projects, and professional experience. It features a clean, high-contrast aesthetic with emerald green accents, smooth animations, and a responsive layout.

## Key Features

- **Minimalist Hero Section:** A striking introduction with custom typography and a profile photo featuring grayscale-to-color hover effects.
- **Featured Work & Research:** Curated sections on the home page for quick access to top projects and publications.
- **Project Portfolio:** Detailed project cards with category filtering, tool tags, and deep-dive detail pages.
- **Academic Publications:** A structured list of research papers, posters, and manuscripts with links to external resources (ResearchGate, DOI, etc.).
- **Professional Experience:** A chronological timeline of internships, research assistantships, and leadership roles.
- **Admin Dashboard:** A secure, Firebase-authenticated interface for managing projects, publications, and experience data in real-time.
- **Contact Integration:** A dedicated contact page with social links and a clear call to action.

## Tech Stack

- **Frontend:** React 18, TypeScript, Vite
- **Styling:** Tailwind CSS (Modern utility-first approach)
- **Animations:** Framer Motion (Smooth page transitions and interactive elements)
- **Icons:** Lucide React
- **Backend/Database:** Firebase (Firestore for real-time data, Firebase Auth for admin security)
- **Server:** Express (Node.js) with Vite middleware for full-stack capabilities

##  Project Structure

```text
├── src/
│   ├── components/      # Reusable UI components (Navbar, Footer, etc.)
│   ├── data/            # Static data files for projects, publications, etc.
│   ├── firebase.ts      # Firebase initialization and service exports
│   ├── pages/           # Main page components (Home, About, Projects, etc.)
│   ├── constants.ts     # Global site content and configuration
│   ├── types.ts         # TypeScript interfaces and types
│   └── main.tsx         # Application entry point
├── server.ts            # Express server with Vite integration
├── firestore.rules      # Security rules for the Firestore database
├── firebase-blueprint.json # Data schema for Firebase entities
└── package.json         # Project dependencies and scripts
```

## Local Development

### Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Environment Configuration:**
   Create a `.env` file based on `.env.example` and add your Firebase configuration if you are setting up your own backend.

4. **Start the development server:**
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:3000`.

## Firebase Configuration

The application uses Firebase for its dynamic content. To connect your own Firebase instance:

1. Create a project in the [Firebase Console](https://console.firebase.google.com/).
2. Enable **Firestore Database** and **Google Authentication**.
3. Create a `firebase-applet-config.json` file in the root directory with your project credentials:
   ```json
   {
     "apiKey": "YOUR_API_KEY",
     "authDomain": "YOUR_PROJECT_ID.firebaseapp.com",
     "projectId": "YOUR_PROJECT_ID",
     "storageBucket": "YOUR_PROJECT_ID.appspot.com",
     "messagingSenderId": "YOUR_SENDER_ID",
     "appId": "YOUR_APP_ID",
     "firestoreDatabaseId": "(default)"
   }
   ```
4. Deploy the security rules provided in `firestore.rules`.

## License

This project is for personal portfolio use. All research content and project data belong to Md. Muqtadir Fuad.

## Contact

- **Email:** mmfuad01@gmail.com
- **LinkedIn:** [md-muqtadir-fuad](https://www.linkedin.com/in/md-muqtadir-fuad/)
- **GitHub:** [md-muqtadir-fuad](https://github.com/md-muqtadir-fuad)
- **ORCID:** [0009-0009-4362-0780](https://orcid.org/0009-0009-4362-0780)
