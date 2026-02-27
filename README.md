# Crew AI Multi-Agent System

## Overview
This project implements a multi-agent system using the Crew AI architecture. It is designed to demonstrate collaboration between multiple agents to solve complex tasks.

## Project Structure
```
calculator.py           # Utility for calculations
crew_ai/
    agent.py           # Agent class definitions and logic
    crew.py            # Crew (multi-agent) orchestration logic
    main.py            # Entry point for running the system
    __pycache__/       # Python cache files
```

## Features
- Modular agent design for extensibility
- Central crew management for agent coordination
- Example utilities (calculator)

## Getting Started
1. **Clone the repository**
2. **Install dependencies** (if any)
3. **Run the main script:**
   ```bash
   python crew_ai/main.py
   ```

## File Descriptions
- **agent.py**: Contains the definition and logic for individual agents.
- **crew.py**: Manages the crew, coordinates agent actions, and task distribution.
- **main.py**: Entry point to initialize and run the multi-agent system.
- **calculator.py**: Provides calculation utilities used by agents.

## Usage
Modify or extend the agents in `agent.py` and crew logic in `crew.py` to suit your multi-agent scenarios.

## License
MIT License
