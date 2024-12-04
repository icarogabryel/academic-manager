class Test:
    def __init__(self, score, weight) -> None:
        self.score = score
        self.weight = weight

    def calculate_score(self) -> float:
        return self.score * self.weight
    
    def __repr__(self) -> str:
        return f"Score: {self.score}, Weight: {self.weight}"
