# Test all files
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.json_loader import load_data
from src.assignment import assign_packages
from src.simulation import simulate_delivery
from src.report import generate_report


def run_test(file_path):

    data = load_data(file_path)

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

    expected_packages = len(packages)

    delivered_packages = sum(
        data["packages_delivered"]
        for data in report["agents"].values()
    )

    if expected_packages == delivered_packages:
        return True, expected_packages, delivered_packages

    return False, expected_packages, delivered_packages


def main():

    test_folder = "DeliveryTestCases"

    test_files = [
        file
        for file in os.listdir(test_folder)
        if file.endswith(".json")
    ]

    test_files.sort()

    passed = 0
    failed = 0

    for file in test_files:

        file_path = os.path.join(
            test_folder,
            file
        )

        success, expected, delivered = run_test(file_path)

        if success:
            print(
                f"{file}: PASS "
                f"(Packages: {delivered}/{expected})"
            )
            passed += 1

        else:
            print(
                f"{file}: FAIL "
                f"(Packages: {delivered}/{expected})"
            )
            failed += 1

    print()
    print("-" * 40)
    print(f"Total Tests : {len(test_files)}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")
    print("-" * 40)


if __name__ == "__main__":
    main()