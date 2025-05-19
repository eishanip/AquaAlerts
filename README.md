# IoT-Based Water Quality Monitoring Project: pH, Turbidity, and Total Dissolved Solids (TDS)

## Overview

An interactive Spanish language learning application that helps users learn vocabulary related to dates, weather, and seasons in Spanish. This React-based web application features audio pronunciation, interactive calendar selection, weather information, and visual elements to enhance the learning experience.

## Features

- **Current Date Display**: Shows today's date in both English and Spanish with audio pronunciation
- **Weather Information**: Displays the current temperature in both numeric format and Spanish words
- **Interactive Calendar**: Allows users to select any date and see it translated into Spanish
- **Season Information**: Shows the current season in Spanish based on the selected date
- **Audio Playback**: Includes spoken Spanish pronunciations for dates, weather, and seasons
- **Image Slideshow**: Displays rotating images of Spanish-speaking countries and cultural scenes

## Technologies Used

- **React**: Frontend library for building the user interface
- **Tailwind CSS**: Utility-first CSS framework for styling
- **Framer Motion**: Animation library for smooth transitions and effects
- **Day.js**: Modern JavaScript date utility library
- **Axios**: Promise-based HTTP client for API requests
- **Open-Meteo API**: Weather data integration
- **React-Calendar**: Calendar component for date selection

## Live Website

The website is currently deployed on -
https://iot-water-quality-monitor-2.onrender.com/

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eishanip/AquaAlerts.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AquaAlerts
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Start the development server:

   ```bash
   npm run dev
   ```

5. Open your browser and navigate to `http://localhost:3000`

## Usage

- The main page displays three cards: Current Date, Current Weather, and Date Selection
- Click on the "Escuchar" buttons to hear Spanish pronunciations
- Use the calendar to select different dates and learn their Spanish translations
- The weather card automatically detects your location to display the current temperature
- Explore the image slideshow to see visual representations of Spanish-speaking cultures

## Project Structure

```
FechaFinder/
├── components/
│   └── ui/               # UI components (calendar, cards, buttons)
├── public/
│   ├── audio/            # Spanish pronunciation audio files
│   └── images/           # Slideshow and background images
├── src/
│   ├── App.jsx           # Main application component
│   └── index.js          # Entry point
└── README.md             # Project documentation
```

## Audio Functionality

The application includes Spanish audio pronunciations for:

- Days of the week
- Months
- Numbers
- Weather-related terms
- Seasons

The audio playback system sequentially plays word-by-word pronunciations to help users learn proper Spanish pronunciation.

## Spanish Number Translation

The application includes a comprehensive system for translating numbers into Spanish words, supporting values up to 9999, and following Spanish numerical grammar rules.

## Weather Integration

Weather data is obtained using the Open-Meteo API, which provides temperature information based on the user's geolocation. The application then converts this numerical data into Spanish words.

## Team Members

- **Eishani Purohit** (22BIT0362)
- **Aaryan Malik** (22BIT0520)
- **Siddhartha Pal** (22BIT0024)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Special thanks to our Value-Added Course professor for guidance.
