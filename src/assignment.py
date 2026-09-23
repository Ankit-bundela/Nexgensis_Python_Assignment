# Assign each package to the nearest agent
from src.distance import calculate_distance


def assign_packages(packages, warehouses, agents):

    assignments = []
    for package in packages:

        warehouse_id = package["warehouse_id"]

        warehouse = next(
            warehouse
            for warehouse in warehouses
            if warehouse["id"] == warehouse_id
        )

        nearest_agent = None
        minimum_distance = float("inf")

        for agent in agents:

            distance = calculate_distance(
                agent["location"],
                warehouse["location"]
            )

            if distance < minimum_distance:
                minimum_distance = distance
                nearest_agent = agent

        assignments.append({
            "package": package,
            "agent": nearest_agent
        })

    return assignments