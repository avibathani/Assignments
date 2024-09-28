import random

def estimate_pi(total_points):
    points_in_circle = 0

    for _ in range(total_points):
        x_coord = random.uniform(-1, 1)
        y_coord = random.uniform(-1, 1)

        if x_coord**2 + y_coord**2 < 1:
            points_in_circle += 1

    pi_estimate = 4 * (points_in_circle / total_points)
    return pi_estimate

num_random_points = int(input("How many random points would you like to generate? "))

calculated_pi = estimate_pi(num_random_points)

print(f"Estimated value of π using {num_random_points} points: {calculated_pi:.6f}")