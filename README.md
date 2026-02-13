# 🎵 YouTube Mashup Generator 🎧✨

_This project is submitted as part of_ **Assignment – Mashup**  
for the course **UCS654**.

_Submitted by:_  
**Dhruv Kamboj (102303645)**  
**Section:** 3C45  

---

## 🎯 Objective

The objective of this project is to design and implement a **YouTube Mashup Generator** that automatically collects songs of a selected singer, processes the audio, and generates a combined mashup file.

The system is implemented in two parts:

- A **command-line program** for mashup generation
- A **web-based service** that allows users to generate mashups and receive them via email

The key goals of this project are:

- To automate downloading and processing audio from YouTube
- To demonstrate multimedia processing using Python libraries
- To build a simple web-based mashup generator
- To deploy the application on a cloud platform

---

## 🧩 Problem Description

Creating mashups manually requires:

- Searching for multiple songs
- Downloading each video
- Extracting audio
- Trimming clips
- Merging them into a final track

This process is repetitive and time-consuming.

The proposed system automates the entire workflow using Python, allowing a user to generate a mashup with just a few inputs.

---

## ⚙️ System Overview

The mashup generator performs the following steps:

1. Download **N videos** of a given singer from YouTube
2. Convert each video into an audio file
3. Trim the first **Y seconds** from each audio
4. Merge all trimmed clips into a single mashup file
5. Send the mashup to the user via email (web version)

---

## 🧪 Program 1 – Command Line Mashup

A Python script that accepts input parameters and generates a mashup locally.

### Command Format
```bash
python <rollnumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
```

```bash
python <rollnumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
