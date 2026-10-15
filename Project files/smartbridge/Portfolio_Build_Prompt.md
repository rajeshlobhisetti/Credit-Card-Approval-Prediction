# Prompt: Build a Professional Software Engineer Portfolio Website

Copy everything below into any AI website builder (Claude, v0.dev, Lovable, Bolt, Claude Code, etc.) to generate the site in one go. All real data is already filled in — no placeholders.

---

## ROLE
Act as a senior frontend engineer and UI/UX designer. Build a modern, professional, animated personal portfolio website for a software developer looking for full-stack developer internships/jobs. The site should look like it was built by a real, current-technology software company — not a generic template.

## TECH STACK
- React (Vite) + Tailwind CSS
- Framer Motion for animations and page/scroll transitions
- React Icons or Lucide React for icons
- Fully responsive (mobile, tablet, desktop)
- Single-page site with smooth-scroll navigation between sections
- Dark mode by default, with a light/dark toggle
- Optimized for fast load and clean code structure (component-based)

## DESIGN DIRECTION
- Professional, minimal, confident — not flashy or cluttered. Think Linear, Vercel, or Stripe's marketing site aesthetic: dark background, one accent color, lots of white space, subtle grid/gradient backgrounds.
- Accent color: deep blue/teal (e.g. #1A5276 or #0EA5E9) against a near-black background (#0B0F19).
- Typography: clean sans-serif (Inter, Space Grotesk, or similar), large confident headings.
- Micro-animations: fade/slide-in on scroll for each section, hover-lift on cards, animated underline on nav links, a subtle typing/cursor animation in the hero for the role title, smooth cursor-following gradient blob or particle background (kept subtle, not distracting).
- Skill bars/tags should animate in when scrolled into view.
- Buttons and cards should have soft shadows and smooth hover transitions (scale/glow).
- Include a working, animated "back to top" button and a sticky/glass-effect navbar that shrinks on scroll.

## SECTIONS TO BUILD

### 1. Hero / Landing
- Name: **Rajesh Lobhisetti**
- Animated role tagline (typing effect cycling through): "Full-Stack Developer", "React & Node.js Developer", "Cloud Practitioner (AWS)", "AI & Automation Enthusiast"
- Short intro line: "Computer Science student building full-stack web apps with React, Node.js and MongoDB. Comfortable working with REST APIs, cloud basics, and always learning something new."
- CTA buttons: "View Projects", "Download Resume", "Contact Me"
- Social icons linking to:
  - LinkedIn: https://www.linkedin.com/in/rajeshlobhis/
  - GitHub: https://github.com/rajeshlobhisetti
  - Email: rajeshlobhisetti@gmail.com
- Animated background (particles, gradient mesh, or subtle grid) behind the hero text.

### 2. About Me
- Computer Science and Engineering student (B.Tech, Lakireddy Bali Reddy College of Engineering, Mylavaram, affiliated to JNTUK), graduating 2027, CGPA 9.1/10.
- Quick learner, enjoys full-stack development, cloud, and automation. Actively practices Java for data structures & algorithms and problem-solving.
- Location: Vijayawada / Hyderabad area, India.
- Include a friendly professional photo placeholder (use an avatar/initials block if no image is supplied) with a soft glow/border animation on hover.

### 3. Technical Skills (animated skill grid, grouped in cards)
- **Languages:** Python, Java, C, SQL
- **Web Development:** React.js, Node.js, Express.js, REST APIs, basic web development in Java
- **Databases:** MongoDB, SQL
- **Cloud & Tools:** AWS, Git, GitHub, Postman
- **Other:** Salesforce (Apex basics, Lightning Web Components), n8n workflow automation
- Display as animated tag pills or progress cards that fade/scale in on scroll, grouped by category with icons (React icon, Node icon, AWS icon, etc.)

### 4. Experience (vertical animated timeline)
**MERN Stack Developer Intern** — Bharat Skillz — Aug 2025
- Built and deployed full-stack web apps using React.js, Node.js, Express.js and MongoDB.
- Connected frontend with backend REST APIs and worked with real data.
- Fixed bugs and improved app speed and user experience.

**Full Stack Development Intern (MERN)** — SmartBridge + APSCHE — Jul 2025
- Built full-stack applications with React.js on the frontend and Node.js on the backend.
- Worked with REST APIs and databases in real project scenarios.
- Learned how to work well in a team using modern web development workflows.

**Salesforce Developer Intern** — SmartBridge (Virtual) — May–Jul 2025
- Learned Salesforce basics: data management, security, and process automation.
- Completed Apex Specialist and Object Relationships badges.
- Practiced building simple workflow automations on the Salesforce platform.

Style as a timeline with animated dots/lines that draw in as the user scrolls, company name, role, duration, and expandable bullet points.

### 5. Projects (animated project cards, 2–3 columns on desktop)
**IoT-Based Smart Accident Prevention System**
- Tech: Raspberry Pi, IoT, Ultrasonic Sensors, IR Sensors, GPS, ThingSpeak
- Built a smart vehicle safety system using Raspberry Pi and multiple sensors.
- Used ultrasonic and IR sensors for obstacle detection and lane monitoring.
- Sent emergency alerts with live GPS location to the ThingSpeak IoT platform.

**Service Agent Automation**
- Tech: n8n, Workflow Automation, APIs, Webhooks
- Built automated workflows to notify and coordinate service agents.
- Used n8n triggers and API/webhook integrations to connect different services.
- Reduced manual work by automating alerts and response handling.

Each card: hover-lift with glow border, tech-stack tags, and a "View on GitHub" link pointing to https://github.com/rajeshlobhisetti (link to the specific repo if the user provides one later — otherwise link to the GitHub profile).

### 6. Certifications (animated badge/logo grid)
- AWS Certified Cloud Practitioner
- Python Essentials 1 & 2 — Cisco Networking Academy
- Introduction to Modern AI — Cisco Networking Academy
- The Joy of Computing using Python — NPTEL (IIT Madras), Elite, 77%
- AI Associate — Salesforce
- Advanced Programming in C — Cisco
- Python Foundation Course — Infosys

### 7. Achievements
- Secured First Prize for Automated Service Agents at Code Crown AI Hackathon.
- Won Second Prize in a Web Development Hackathon using the MERN Stack.
- NSS Coordinator — served during AP 2024 Elections.
- Class Representative — III Semester.

Style as animated stat/achievement cards with a trophy/medal icon.

### 8. Contact
- Simple contact form (Name, Email, Message) with animated focus states — connect to `mailto:rajeshlobhisetti@gmail.com` or a form service (e.g. Formspree) since this is a static site.
- Repeat direct contact details: rajeshlobhisetti@gmail.com | +91 6300321330
- Social links again: LinkedIn (https://www.linkedin.com/in/rajeshlobhis/), GitHub (https://github.com/rajeshlobhisetti)

### 9. Footer
- "Built by Rajesh Lobhisetti" with current year, small social icons, and a "back to top" link.

## FUNCTIONAL REQUIREMENTS
- Sticky navbar with smooth-scroll links to each section, active-section highlighting as the user scrolls.
- Mobile hamburger menu with slide-in animation.
- All animations should use Framer Motion `whileInView` so they trigger once per section as the user scrolls, not just on page load.
- Include a loading/entrance animation on first load (e.g. a short logo/name reveal).
- Keep total page weight light — no huge unoptimized images or libraries beyond what's listed.
- Code should be clean, componentized (Navbar, Hero, About, Skills, Experience, Projects, Certifications, Achievements, Contact, Footer), and easy to extend later (e.g. adding a blog or new projects).

## TONE OF WRITTEN CONTENT
Keep all copy simple and human — not overly formal corporate language. Rajesh is a student, so the tone should read as genuine, confident, and eager to learn, not exaggerated.
