# From Present & Past Simple to Past Perfect (A2)
### Complete Interactive ESL Teaching Package & Web Service

A complete, self-contained educational web application and lightweight web services designed for CEFR A2 learners and 1:1 online tutoring sessions.

## 🚀 Key Features

- **Interactive Curriculum & Exercises (Part A, B, C):**
  - Summarized reviews of Present Simple and Past Simple.
  - S1–S4 Speaking activation tasks with countdown timers and progressive starter reveals.
  - Past Perfect grammar bridge, timelines, form transformations, and minimal pairs.
  - Turkish L1 interference alerts and error tagging ([F] Form, [P] Participle, [S] Sequence, [W] Signal-word, [R] Review-tense).
  - 40 graded practice items across Types 0–7, reading and noticing story, and guided production.
  - Real-time diagnostic error breakdown and study recommendations.
  - **Teacher Mode:** Instant projection toggle for master answer keys and explanations.

- **1:1 Live Online Session Notes Suite:**
  - Slide-over live notes drawer with auto-save to localStorage.
  - Dedicated fields for student goals, live pronunciation drills, and Delayed Error Correction (DEC).
  - One-click quick-chips for common A2 slips.
  - Instant summary copying for Zoom/Skype/Meet/WhatsApp chat and downloadable .txt reports.

- **Offline & Standalone:**
  - index.html runs 100% offline with zero external CDNs, fonts, or network requests.

- **Web Service Backends:**
  - **Node.js:** 
ode server.js (serves app and /api/curriculum, /api/verbs on port 3000)
  - **Python:** python server.py (native HTTP server on port 8080)
  - **Java:** EslServer.java (Java HttpServer implementation on port 8000)

## 📦 File Overview

- index.html: The complete interactive web application.
- curriculum_data.json: Structured curriculum dataset with verbs, exercises, and error metadata.
- server.js: Node.js ES module web server.
- server.py: Python 3 native HTTP server.
- EslServer.java: Standard Java HTTP server.
