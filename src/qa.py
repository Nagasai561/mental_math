import yaml
import random


# Validate configuration file
def validate_config(config):
    if "operations" not in config:
        raise ValueError("Config must contain 'operations' key.")
    operators_probabilities = sum(
        op["probability"] for op in config["operations"].values()
    )

    if operators_probabilities < 0.99 or operators_probabilities > 1.01:
        raise ValueError("Sum of operation probabilities must be 1.0.")

    for op_name, op_data in config["operations"].items():
        if "sizes" not in op_data:
            raise ValueError(f"Operation '{op_name}' must contain 'sizes' key.")
        sizes_probabilities = sum(prob for prob in op_data["sizes"].values())
        if sizes_probabilities < 0.99 or sizes_probabilities > 1.01:
            raise ValueError(
                f"Sum of size probabilities for operation '{op_name}' must be 1.0."
            )


# Generate question and answer based on configuration
def generate_qa():
    operation_types = list(config["operations"].keys())
    operation_probs = [
        config["operations"][op]["probability"] for op in operation_types
    ]
    operation = random.choices(operation_types, weights=operation_probs)[0]

    digit_pairs = config["operations"][operation]["sizes"]
    digit_pair_types = list(digit_pairs.keys())
    digit_pair_probs = list(digit_pairs.values())
    digit_pair = random.choices(digit_pair_types, weights=digit_pair_probs)[0]

    big_number_digits, small_number_digits = map(int, digit_pair.split("/"))
    big_number = random.randint(
        10 ** (big_number_digits - 1), 10**big_number_digits - 1
    )
    small_number = random.randint(
        10 ** (small_number_digits - 1), 10 ** (small_number_digits) - 1
    )

    numbers = [big_number, small_number]
    random.shuffle(numbers)

    question = f"{numbers[0]} {operation} {numbers[1]}"
    answer = big_number + small_number

    return question, answer


with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

validate_config(config)

if __name__ == "__main__":
    from rich import print as rprint

    for i in range(5):
        question, answer = generate_qa()
        rprint(
            f"[green bold] Question {i+1}: [cyan bold] {question}, [magenta bold] Answer: {answer}"
        )
