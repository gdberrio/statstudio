Sprint 1:
Implement Poisson Count model with UI

1. Model generated pymc3
2. Fastapi runs the backend
3. Vue.js runs the frontend

Workflow:
1. In the frontend, import csv of data
2. frontend serializes csv, and sends JSON request to the backend through a REST API Request
3. backend send it to pymc3 for simulation
4. when the model is done, the backend returns JSON with results
5. frontend renders results & visuals

Tasks:
1. Reimplement with randomized data and document
2. Create Fastapi backend
3. Implement pymc3 model
4. Create vue.js frontend