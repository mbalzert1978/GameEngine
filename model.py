from dataclasses import dataclass
import random


@dataclass
class ModelRateZahl:
    leben: int = 3
    zu_raten: int = random.randint(1, 10)

    def ist_spiel_verloren(self) -> bool:
        return self.leben

    def prüfe_zahl(self, user_eingabe: int) -> bool:
        if user_eingabe != self.zu_raten:
            self.leben -= 1
            return False
        return True

    def ist_kleiner(self, user_eingabe: int) -> bool:
        if user_eingabe > self.zu_raten:
            return False
        return True