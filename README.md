# SmartTasker

SmartTasker is an AI-driven smart task and productivity tracker designed to help users efficiently manage their tasks, track progress, and analyze productivity statistics.

## Development Status
This project is currently under development, and new features are being actively implemented.

## Implementation Details
### Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Javascript, Bootstrap
- **Database**: SQLite
- **AI & Analytics**: Scikit-learn (for AI-based insights), Pandas & Matplotlib (for data visualization)
- **Authentication**: Flask-Login, OAuth (Google Login), JWT for secure user authentication
- **Task Scheduling & Notifications**: Celery with Redis

### Key Features & Implementation
 **User Authentication & Security**
- Secure login with Flask-Login / OAuth (Google, Facebook authentication).
- JWT-based authentication for API security.
- Password hashing using bcrypt for security.

 **Task Management (CRUD Operations)**
- Users can Create, Read, Update, Delete (CRUD) tasks.
- Tasks can be categorized (Work, Study, Personal, etc.).
- Priority tagging (High, Medium, Low) for better organization.

 **Automated Reminders & Notifications**
- Users set deadlines while adding tasks.
- Send scheduled reminders via Email/SMS/Push Notifications.

 **AI-Based Productivity Insights**
- **Task Prioritization using AI**
  - Uses NLP and ML models to analyze urgency based on deadline, category, and past behaviour.
- **Habit Tracking & Productivity Score**
  - Tracks time spent on tasks using Flask APIs & logs.
  - Uses past data to suggest optimal study/work hours based on user productivity.
  - Generates a "Productivity Score" based on completion rate & efficiency.

 **Graphical Progress Reports**
- Matplotlib & Chart.js for interactive visual analytics.
- Daily/Weekly/Monthly reports with:
  - Task completion rates
  - Efficiency trends
  - Missed deadlines vs. completed tasks

 **Smart Suggestions & Habit Formation**
- Built in pomodoro for focus mode
- Suggests break schedules to improve efficiency.
- Habit tracking with streaks (e.g., “3 days of consistent task completion”).

 **Collaboration & Team Features**
- Shared task lists with teammates.
- Work on shared projects together

### Deployment & Hosting
- **Backend**: Deployed on AWS / Render
- **Frontend**: Deployed on Vercel / Netlify
- **Database**: Hosted on AWS RDS / Supabase
- **Notification Services**: Twilio (SMS), Firebase Cloud Messaging (Push)



