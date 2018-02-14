import random


class ItemPiece:

    piece_types = ['helmet', 'chest armor', 'pauldrons', 'pants', 'boots', 'gauntlets', 'weapon']

    @classmethod
    def get_piece_type(cls):
        return random.choice(cls.piece_types)