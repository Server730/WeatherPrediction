<<<<<<< HEAD
# 🌤️ Weather Prediction App

A modern, ML-powered weather forecasting web application with real-time data and dynamic visual themes.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🎯 Features

### 🌡️ Weather Data
- Real-time weather from **Open-Meteo API** (no API key required!)
- Current conditions: Temperature, humidity, wind speed, pressure, visibility
- 5-day forecast with detailed metrics

### 🤖 Machine Learning
- **Random Forest Regressor** for temperature prediction
- **97% prediction accuracy** on test data
- Automated model training with synthetic weather data

### 🎨 Dynamic Themes (7 Weather Themes)
| Theme | Background | Effects |
|-------|-----------|---------|
| ☀️ Sunny | Blue sky gradient | Animated pulsing sun |
| 🌧️ Rainy | Dark blue-grey | 100 CSS animated raindrops |
| ⛈️ Thunderstorm | Dark purple-grey | Rain + random lightning flashes |
| ☁️ Cloudy | Grey-blue gradient | Floating cloud animations |
| ❄️ Snowy | White-grey gradient | 50 falling snowflakes |
| 🌫️ Foggy | Pale grey gradient | Drifting fog layers |
| 💨 Windy | Teal-blue gradient | Fast-moving wind streaks |

### 🎨 UI/UX Design
- **Glassmorphism** - Frosted glass left panel with blur effects
- **Two-panel layout** - Narrow glass card (left) + Sky background (right)
- **Responsive design** - Works on desktop, tablet, and mobile
- **Smooth transitions** - 0.8s CSS theme animations

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python, Flask |
| ML | Scikit-learn, NumPy, Pandas |
| API | Open-Meteo (Free, no key) |
| Styling | Custom CSS (Glassmorphism) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Server730/WeatherPrediction.git

# 2. Navigate to project folder
cd WeatherPrediction

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Train ML model
python train_model.py

# 7. Run the app
python app.py
=======
\# 🌤️ Weather Prediction App



A modern, ML-powered weather forecasting web application with real-time data and dynamic visual themes.



!\[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

!\[Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)

!\[Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)

!\[License](https://img.shields.io/badge/License-MIT-yellow.svg)



\---



\## 🎯 Features



\### 🌡️ Weather Data

\- Real-time weather from \*\*Open-Meteo API\*\* (no API key required!)

\- Current conditions: Temperature, humidity, wind speed, pressure, visibility

\- 5-day forecast with detailed metrics



\### 🤖 Machine Learning

\- \*\*Random Forest Regressor\*\* for temperature prediction

\- \*\*97% prediction accuracy\*\* on test data

\- Automated model training with synthetic weather data



\### 🎨 Dynamic Themes (7 Weather Themes)

| Theme | Background | Effects |

|-------|-----------|---------|

| ☀️ Sunny | Blue sky gradient | Animated pulsing sun |

| 🌧️ Rainy | Dark blue-grey | 100 CSS animated raindrops |

| ⛈️ Thunderstorm | Dark purple-grey | Rain + random lightning flashes |

| ☁️ Cloudy | Grey-blue gradient | Floating cloud animations |

| ❄️ Snowy | White-grey gradient | 50 falling snowflakes |

| 🌫️ Foggy | Pale grey gradient | Drifting fog layers |

| 💨 Windy | Teal-blue gradient | Fast-moving wind streaks |



\### 🎨 UI/UX Design

\- \*\*Glassmorphism\*\* - Frosted glass left panel with blur effects

\- \*\*Two-panel layout\*\* - Narrow glass card (left) + Sky background (right)

\- \*\*Responsive design\*\* - Works on desktop, tablet, and mobile

\- \*\*Smooth transitions\*\* - 0.8s CSS theme animations



\---



\## 🛠️ Tech Stack



| Layer | Technology |

|-------|------------|

| Frontend | HTML5, CSS3, Vanilla JavaScript |

| Backend | Python, Flask |

| ML | Scikit-learn, NumPy, Pandas |

| API | Open-Meteo (Free, no key) |

| Styling | Custom CSS (Glassmorphism) |



\---



\## 🚀 Quick Start



\### Prerequisites

\- Python 3.8 or higher

\- pip (Python package manager)



\### Installation



```bash

\# 1. Clone the repository

git clone https://github.com/Server730/WeatherPrediction.git



\# 2. Navigate to project folder

cd WeatherPrediction



\# 3. Create virtual environment

python -m venv venv



\# 4. Activate virtual environment

\# Windows:

venv\\Scripts\\activate

\# Mac/Linux:

source venv/bin/activate



\# 5. Install dependencies

pip install -r requirements.txt



\# 6. Train ML model

python train\_model.py



\# 7. Run the app

python app.py



>>>>>>> e4924bb (Updated UI - Dynamic weather themes, hourly temperature chart, glassmorphism design)
