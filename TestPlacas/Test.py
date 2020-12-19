import unittest
import PlacVehi

PROBAR = {
    'CP': 'CP0000',
    'CD': 'CD0000',
    'CC': 'CC0000',
    'RCD': 'RCD000',
    'MCD': 'MCD000',
    'MADM': 'MADM00',
    'ADM': 'ADM000',
    'PH': 'PH0000',
    'PE': 'PE0000',
    'MMI': 'MMI000',
    'RMI': 'RMI000',
    'PR': 'PR0000',
    'HP': 'HP0000',
    'D': 'D00000',
    'E': 'E00000',
    'G': 'G00000',
    'MA': 'MA0000',
    'MB': 'MB0000',
    'CH': 'CH0000',
    'MI': 'MI0000',
    'AA': 'AA0000',
    'AB': 'AB0000',
    'AC': 'AC0000',
    'AD': 'AD0000',
    'AE': 'AE0000',
    'AF': 'AF0000',
    'AG': 'AG0000',
    'AH': 'AH0000',
    'AI': 'AI0000',
    'AJ': 'AJ0000',
    'AK': 'AK0000',
    'AL': 'AL0000',
    'AM': 'AM0000',
    'AN': 'AN0000',
    'AO': 'AO0000',
    'AP': 'AP0000',
    'AQ': 'AQ0000',
    'AR': 'AR0000',
    'AS': 'AS0000',
    'AT': 'AT0000',
    'AU': 'AU0000',
    'AV': 'AV0000',
    'AW': 'AW0000',
    'AX': 'AX0000',
    'AY': 'AY0000',
    'AZ': 'AZ0000',
    '.1': '000000',
    'T': 'T00000',
    '#T': '5T0000',
    '#B': '8B0000',
    'BA0000': 'BA0000'}

class PruebaCadena(unittest.TestCase):

    def testplacas(self):
        for k in PROBAR.values():
            print(k)
            self.assertEqual(PlacVehi.Valida(k), None)

unittest.main()