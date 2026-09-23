import csv


def export_top_performer(report, output_file="CSV/top_performer.csv"):

    best_agent = report["best_agent"]

    agent_data = report["agents"][best_agent]

    with open(output_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "agent_id",
            "packages_delivered",
            "total_distance",
            "efficiency"
        ])

        writer.writerow([
            best_agent,
            agent_data["packages_delivered"],
            agent_data["total_distance"],
            agent_data["efficiency"]
        ])