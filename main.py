# main.py

def estimate_search_space(password: str) -> int:
    """
    Estimate how many possible combinations exist for passwords
    with the same length and character set as the given password.
    """
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    # "Symbols" = everything else that's not letter or digit
    has_symbol = any(not c.isalnum() for c in password)

    possible_chars = 0
    if has_lower:
        possible_chars += 26
    if has_upper:
        possible_chars += 26
    if has_digit:
        possible_chars += 10
    if has_symbol:
        # Rough estimate for symbols on a keyboard
        possible_chars += 32

    if possible_chars == 0:
        return 0

    return possible_chars ** len(password)


def format_time(seconds: float) -> str:
    """
    Turn a number of seconds into a human-friendly string.
    """
    if seconds < 1:
        return "< 1 second"

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if years >= 1:
        return f"{years:.2f} years"
    elif days >= 1:
        return f"{days:.2f} days"
    elif hours >= 1:
        return f"{hours:.2f} hours"
    elif minutes >= 1:
        return f"{minutes:.2f} minutes"
    else:
        return f"{seconds:.2f} seconds"


def estimate_bruteforce_times(password: str):
    """
    Given a password, estimate brute-force time at different speeds.
    Returns a dict: speed_label -> formatted time.
    """
    space = estimate_search_space(password)
    if space == 0:
        return {}

    speeds = {
        "1,000 guesses/sec": 1_000,
        "1,000,000 guesses/sec": 1_000_000,
        "1,000,000,000 guesses/sec": 1_000_000_000,
    }

    results = {}
    for label, guesses_per_second in speeds.items():
        seconds = space / guesses_per_second
        results[label] = format_time(seconds)

    return results

# Analyze the basic properties of the password
def analyze_basic_properties(password: str) -> list[str]:
    """
    Check basic properties: length, character types, etc.
    Returns a list of text comments.
    """
    comments = []

    length = len(password)
    comments.append(f"Length: {length}")

    if length < 8:
        comments.append("Too short: aim for at least 12+ characters.")
    elif length < 12:
        comments.append("Okay length, but 12+ characters is safer.")
    else:
        comments.append("Good length.")

    if any(c.islower() for c in password):
        comments.append("Contains lowercase letters.")
    else:
        comments.append("No lowercase letters.")

    if any(c.isupper() for c in password):
        comments.append("Contains uppercase letters.")
    else:
        comments.append("No uppercase letters.")

    if any(c.isdigit() for c in password):
        comments.append("Contains digits.")
    else:
        comments.append("No digits.")

    if any(not c.isalnum() for c in password):
        comments.append("Contains symbols.")
    else:
        comments.append("No symbols.")

    return comments


def main():
    password = input("Enter a password to analyze: ").strip()

    if not password:
        print("No password entered. Exiting.")
        return

    print("\n=== Basic Analysis ===")
    for line in analyze_basic_properties(password):
        print("-", line)

    print("\n=== Estimated brute-force times (worst-case) ===")
    times = estimate_bruteforce_times(password)
    if not times:
        print("Could not estimate (no valid characters?).")
    else:
        for label, t in times.items():
            print(f"At {label}: {t}")


if __name__ == "__main__":
    main()
