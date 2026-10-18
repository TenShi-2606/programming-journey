"""TP — Validate user input before processing it."""


def classify_score(score: float) -> str:
    """Classify a score from 0 to 20, rejecting invalid values."""
    if not 0 <= score <= 20:
        return "Note invalide : saisir une valeur de 0 à 20."
    if score >= 10:
        return "Admis"
    return "Ajourné"


def main() -> None:
    raw = input("Saisir une note entre 0 et 20 : ").strip()
    try:
        score = float(raw)
    except ValueError:
        print("Entrée invalide : saisir un nombre.")
        return
    print(classify_score(score))


if __name__ == "__main__":
    main()
