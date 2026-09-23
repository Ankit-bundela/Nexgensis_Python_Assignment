import json
from src.json_loader import load_data
from src.assignment import assign_packages
from src.simulation import simulate_delivery
from src.report import generate_report
from src.csv_export import export_top_performer

def main():
    data = load_data("base_case.json")

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    assignments = assign_packages(
        packages,
        warehouses,
        agents
    )
 
    agent_data = simulate_delivery(
        assignments,
        warehouses
    )

    report = generate_report(agent_data)
    export_top_performer(report)
       
    with open("report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("Delivery simulation completed successfully.")
    print("Report saved to report.json")  
    print("Top performer exported to CSV/top_performer.csv")


if __name__ == "__main__":
    main()