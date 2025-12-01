🌊 SmartAqua-Optimizer
AI-Driven Water-Efficient Cooling Optimization System for Data Centers

SmartAqua-Optimizer is an end-to-end machine learning project that simulates, predicts, and optimizes water usage in data center cooling systems.
It combines ML prediction, real-time simulation, database logging, and automated optimization to reduce water waste while maintaining cooling efficiency.

🚀 Key Features
🔹 1. ML-Based Cooling Prediction

Trains a Random Forest model using historical cooling data
to predict required cooling load (kW) based on:

Rack load

Humidity

Outside temperature

Inlet temperature

🔹 2. Water Usage Optimization Engine

A custom mathematical optimizer that:

Ensures correct water allocation

Minimizes wastage

Logs usage per simulation cycle

🔹 3. Real-Time Simulation

Simulates live datacenter operation every second:

Predict cooling requirement

Optimize water required

Log everything into SQLite

Generate water-efficiency graphs

🔹 4. SQLite Logging System

Two databases are generated:

aqualess.db → historical water usage

aqualess_logs.db → real-time simulation logs

🔹 5. Visual Analytics Dashboard

Automatically saves graphs for:

Rack load vs temperature

Required Cooling

Water Used

Water Saved

Stored inside /graphs/.
