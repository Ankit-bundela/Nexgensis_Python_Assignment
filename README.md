# Mystery Delivery System

A Python-based logistics simulator for FastBox that simulates package delivery using multiple warehouses and delivery agents.

## Project Overview

The system reads warehouse, agent, and package information from a JSON file.

For each package, the system:

1. Finds the warehouse from which the package should be picked up.
2. Assigns the package to the nearest delivery agent.
3. Simulates the delivery from the agent's current location to the warehouse    and then to the package destination.
4. Calculates the total distance travelled by each agent.
5. Generates a delivery report.
6. Identifies the most efficient agent.
7. Exports the top performer to a CSV file as a bonus feature.

## Technologies Used

* Python
* JSON
* CSV
* `math` module
* Python standard library

## Project Structure

```text
Nexgensis_Python_Assignment/
│
├── base_case.json
├── DeliveryTestCases/
│   ├── test_case_1.json
│   ├── test_case_2.json
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── json_loader.py
│   ├── distance.py
│   ├── assignment.py
│   ├── simulation.py
│   ├── report.py
│   └── csv_export.py
│
├── tests/
│   └── test_runner.py
│
├── CSV/
│   └── top_performer.csv
│
├── main.py
├── report.json
└── README.md
```

## How to Run

Run the main program from the project root directory:

```bash
py main.py
```

The program generates:

```text
report.json
CSV/top_performer.csv
```

## Package Assignment

Each package is assigned to the nearest delivery agent.

The distance between an agent and the package's warehouse is calculated using Euclidean distance.

The agent with the minimum distance from the warehouse is selected.

## Distance Calculation

Euclidean distance is calculated using:

```text
distance = √((x2 - x1)² + (y2 - y1)²)
```

The simulation calculates:

```text
Agent → Warehouse
+
Warehouse → Package Destination
```

The distances are added to the agent's total distance.

## Delivery Simulation

The simulation keeps track of each agent's:

* Number of packages delivered
* Total distance travelled
* Current location

After delivering a package, the agent's current location is updated to that package's destination.

This allows the next delivery to start from the agent's latest location.

## Report

The generated `report.json` contains:

* `packages_delivered`
* `total_distance`
* `efficiency`
* `best_agent`

Efficiency is calculated as:

```text
efficiency = total_distance / packages_delivered
```

The agent with the lowest efficiency value is selected as the best agent.

## CSV Bonus Feature

As an additional bonus feature, the top-performing agent is exported to:

```text
CSV/top_performer.csv
```

Example:

```text
agent_id,packages_delivered,total_distance,efficiency
A3,1,14.14,14.14
```

## Testing

The project includes 10 different JSON test cases.

Run:

```bash
py tests/test_runner.py
```

All 10 test cases currently pass.

```text
Total Tests : 10
Passed      : 10
Failed      : 0
```

The test runner also verifies that the total number of delivered packages matches the total number of packages in each test case.

## Assumptions

* Each package is assigned to the nearest agent based on the agent's current location and the package's warehouse location.
* When an agent has multiple packages, deliveries are processed in the order in which packages appear in the input JSON.
* After completing a delivery, the agent's current location becomes the package destination.
* If two agents have the same minimum distance, the first agent encountered in the input order is selected.
* Efficiency is calculated as total distance divided by packages delivered.
* The agent with the lowest efficiency value is considered the best agent.
