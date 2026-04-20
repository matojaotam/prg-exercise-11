import random
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)


    def get_grade(self, index):
        score = self.get_by_index(index)

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        pozice = []

        for i in range(len(self.scores)):
            if self.scores[i] == score:
                pozice.append(i)

        return pozice

    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)

        for i in range(n):

            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores

    def average(self):
        if self.count() == 0:
            return 0
        return sum(self.scores) / self.count()

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def pass_rate(self):
        passed = sum(1 for s in self.scores if s >= 50)
        return passed / self.count()

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentu, prumer {self.average():.1f}"

    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("serazuji...")
            self._sorted_scores = self.get_sorted()
        left = 0
        right = len(self._sorted_scores) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = self._sorted_scores[mid]

            if mid_value == score:
                return mid
            elif mid_value < score:
                left = mid + 1
            else:
                right = mid - 1

        return None




def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())          # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    #
    # print(results.get_grade(2))  # A (91 bodů)
    # print(results.get_grade(6))  # A (100 bodů)
    # print(results.get_grade(7))  # F (38 bodů)
    #
    # print(results.find(100))  # [6]
    # print(results.find(50))   # [4]
    # print(results.find(77))   # []
    #
    # print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    print("Pocet studentu:", results.count())
    print()

    print("Vysledky studentu:")
    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    print("Studenti se 100 body:", results.find(100))

    print("Serazene vysledky (od nejhorsiho):")
    print(results.get_sorted())

    random_results = StudentsGrades(random_numbers(30))
    print("Nahodna skupina – pocet studentu:", random_results.count())
    print("Serazene vysledky:")
    print(random_results.get_sorted())

    print(results.find_sorted(91))  # sorting… → index 7
    print(results.find_sorted(50))  # → index 2 (už neřadí)
    print(results.find_sorted(77))  # → None

print(main())