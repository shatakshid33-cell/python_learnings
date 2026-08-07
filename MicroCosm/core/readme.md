🧬 MicroCosm
What is MicroCosm?
MicroCosm is a python-based biological simulation engine that models a cell as a dynamic, self-sustaining ecosystem rather than a static collection of variables.

Most biological scripts look at fixed data or run basic if/else checks to output a static result. MicroCosm works differently: it builds a low-level engine where biological variables (like ATP, oxidative stress, repair capacity, and DNA integrity) constantly react to each other over time.

Instead of hardcoding how a drug or disease forces an outcome, we build the underlying rules of cellular homeostasis first. Once the core engine works, external events—whether that's radiation, viral infection, or chemotherapy—simply push parameters out of balance and let the cascading effects play out naturally.

---Tech Stack
Core Engine: Python 3 (OOP, custom dynamic state updates)

Data Logging: Pandas (planned for trajectory tracking)

Visualization: Matplotlib / Seaborn (planned for live state plots)

Predictive Modeling: Scikit-Learn / XGBoost (future phase to predict cell death vs. recovery)

---Phase 1 Focus — A Single Living Cell
Before adding complex drug pipelines or multi-cell interactions, Phase 1 focuses entirely on getting one cell to feel alive.

Right now, the goal is simple: if you instantiate a cell and let time pass, it should naturally consume energy, manage stress, repair its DNA, and attempt to maintain balance on its own—even if the user does nothing.

---Phase 1 Deliverables:
Core Cell class with interdependent state variables (ATP, DNA Integrity, Stress, Repair, Protein Production)

Time-step loop that runs continuous homeostatic updates

Natural decay rates and baseline energy consumption

Basic event injection (e.g., triggering a sudden spike in oxidative stress to test repair mechanics)

A clean terminal status readout