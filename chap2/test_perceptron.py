import perceptron
import unittest


class TestPerceptron(unittest.TestCase):
    def test_and(self):
        print("[*]test AND")
        self.assertEqual(perceptron.AND(0, 0), 0)
        self.assertEqual(perceptron.AND(0, 1), 0)
        self.assertEqual(perceptron.AND(1, 0), 0)
        self.assertEqual(perceptron.AND(1, 1), 1)

    def test_nand(self):
        print("[*]test NAND")
        self.assertEqual(perceptron.NAND(0, 0), 1)
        self.assertEqual(perceptron.NAND(0, 1), 1)
        self.assertEqual(perceptron.NAND(1, 0), 1)
        self.assertEqual(perceptron.NAND(1, 1), 0)

    def test_or(self):
        print("[*]test OR")
        self.assertEqual(perceptron.OR(0, 0), 0)
        self.assertEqual(perceptron.OR(0, 1), 1)
        self.assertEqual(perceptron.OR(1, 0), 1)
        self.assertEqual(perceptron.OR(1, 1), 1)

    def test_xor(self):
        print("[*]test XOR")
        self.assertEqual(perceptron.XOR(0, 0), 0)
        self.assertEqual(perceptron.XOR(0, 1), 1)
        self.assertEqual(perceptron.XOR(1, 0), 1)
        self.assertEqual(perceptron.XOR(1, 1), 0)


if __name__=='__main__':
    unittest.main()
