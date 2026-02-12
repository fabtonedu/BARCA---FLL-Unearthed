# 🏺 Project BARCA — Fabton Team @ FLL Challenge (UNEARTHED)

🌍 **Fabton Team — FLL Challenge / UNEARTHED**  
📦 This repository contains the **complete season documentation**: Innovation Project + Robot Design materials.  
🔓 Open learning, open source, and fully reproducible assets.

---

## 🧠 Innovation Project — Research, Education & Real-World Impact

**Project BARCA** was created as our response to the FLL Innovation Challenge.  
We started with a simple question:

> *How can we help young people connect to their local history — and how can technology support archaeology in real conditions?*

### ✅ Highlights
- Research-based problem discovery (local + real-world context)
- Expert interviews and field visits
- Youth-friendly education materials (**BARCA EDU**)
- A practical prototype concept for preservation (**BARCA Box**)
- Open-source documentation: visuals, renders, models, and materials

### 👥 Experts & Community Involvement
We reached and worked with multiple experts during the season:
- Satellite & archaeology insights (ROSPIN)
- Local excavation field visit with an archaeologist
- Artifact storage & youth engagement guidance
- Conservation/restoration: how fragile findings can be preserved long-term

*(Full details, visuals, and outreach records are included in the Innovation Project folder.)*

---

## 🧩 Our Innovation Solutions

### 📘 BARCA EDU — “Csíki Kincses Könyv”
A youth-focused educational booklet (designed for 0–6 grade, but usable beyond), featuring:
- 12 archaeological artifacts found around Csíkszereda
- Interactive tasks and creative learning activities
- Museum collaboration for accurate selection and high-quality imagery
- Expert review / proofreading before printing

We printed **100 copies**, and **donated 25** to the local hospital as part of community outreach.

### 🧰 BARCA Box — Preservation in the field
During research, we kept returning to one critical issue:  
**oxidation and damage risk** for freshly excavated metal artifacts.

BARCA Box is our proposed field tool concept:
- Airtight container + silica gel + oxygen absorber tablets
- Solar charging system for isolated fieldwork
- Sensor-based monitoring (humidity, battery, time/date)
- Modular documentation workflow for findings

We designed it with practical components in mind (ESP32, display, sensors, SD storage, USB-C).

---

## 🤖 Robot Design — Strategy, Engineering & Competition Execution

Our Robot Game preparation evolved through multiple iterations.  
We built our season around **repeatability**, **fast swaps**, and **low-error starts**.

### 📍 Phase 1 — Regional Strategy
- Everyone created independent mission strategies
- We unified them into a single shared mission plan
- Box-style robot base, widened for stability and attachment space
- Focus on mission coverage and consistency

### 📍 Phase 2 — Iteration & Improvements
- Attachment workflow refined for faster swaps
- Starting positions standardized (wall-starts to reduce error)
- Reliability habits introduced (testing discipline, documentation, backups)

### 📍 Phase 3 — Final / Refined System
Most advanced and competition-ready version:
- Modular attachments with consistent mounting points
- Reduced “wrong run / wrong attachment” risk
- Color-sensor-based identification + calibration workflow
- Systematic testing: runs considered “ready” only after high success rates
- Strong documentation: Studio models, route plans, scripts, test notes

---

## 🎛️ Key Engineering Ideas We’re Proud Of

### 🎨 Color-sensor based attachment safety
To avoid:
- starting the wrong program
- starting with the wrong attachment

We used a **color marker on each attachment** and a **dedicated color sensor** on the robot:
- the robot recognizes the attachment color
- it triggers the correct run selection logic
- calibration is supported to handle changing light conditions

### 🧪 Testing discipline
A run was only considered “ready” when it performed reliably in repeated trials  
(e.g., strong success ratio across many attempts).  
We also monitored battery impact, because performance changes below certain charge levels.

---

## 🧰 Repository Structure

This repository is intentionally split into two main parts:

.
├── Innovation Project/
│ ├── [3D STL Models]/
│ ├── [BARCA_BOX_3D Renders]/
│ └── Csiki_Kincses... Booklet.pdf
│
├── Robot Design/
│ ├── [Building Instructions]/
│ ├── [Render]/
│ ├── [Routes]/
│ ├── [Script]/
│ └── [Studio]/
│
├── LICENSE
└── README.md


### 📁 Where to find what
- **Innovation Project/**
  - STL models & renders for BARCA Box
  - Educational booklet PDF and supporting assets
- **Robot Design/**
  - Building instructions for attachments
  - Route plans / run plans
  - Studio 2.0 models for reproducibility
  - Python files/scripts

---

## 🧩 Open Learning

Team Fabton believes in transparent, collaborative learning.  
Everything we built is published so others can:
- learn from our process
- remix our assets
- build stronger projects faster

---

## 📄 License

🔓 MIT License — free to use, modify, remix, and distribute.

---

## 🙏 Attribution

If you use any part of our code, designs, project structure, visuals, or documentation, please credit:

**Fabton Team — FLL Challenge (UNEARTHED) — Project BARCA**

Open learning works best when we recognize each other’s work.  
Thank you! 💙

— Team Fabton


