import unittest
from TradingGame import Player, Product

class TestProduct(unittest.TestCase):

    def test_accessAttributes(self):
        testProduct = Product()
        testProduct.setAttributes(1,1,1,1)
        self.assertEqual(testProduct.price, 1)
        self.assertEqual(testProduct.terms, 1)
        self.assertEqual(testProduct.revenue, 1)
        self.assertEqual(testProduct.risk, 1)
        self.assertEqual(testProduct.getAttributes(), (1,1,1,1))

    def test_accessRoundsRemain(self):
        testProduct = Product()
        testProduct.setAttributes(1,1,1,1)
        testProduct.setRoundsRemain()
        self.assertEqual(testProduct.getRoundsRemain(), testProduct.roundsRemain)
        self.assertEqual(testProduct.roundsRemain, 1)
        self.assertEqual(testProduct.getRoundsRemain(), 1)

    def test_updateRoundsRemain(self):
        testProduct = Product()
        testProduct.setAttributes(1,1,1,0.4)
        testProduct.updateRoundsRemain(0.2)
        self.assertEqual(testProduct.roundsRemain, -1)

        testProduct = Product()
        testProduct.setAttributes(1,1,1,0.4)
        testProduct.updateRoundsRemain(0.4)
        self.assertEqual(testProduct.roundsRemain, 0)

        testProduct = Product()
        testProduct.setAttributes(1,1,1,0.4)
        testProduct.updateRoundsRemain(0.6)
        self.assertEqual(testProduct.roundsRemain, 0)

class TestPlayer(unittest.TestCase):

    def test_createPlayer(self):
        self.assertEqual(Player.playerNum, 0)
        dummyPlayer = Player('dummy')
        self.assertEqual(Player.playerNum, 1)
        self.assertEqual(dummyPlayer.money, Player.INIT_MONEY)
        self.assertEqual(dummyPlayer.myProduct, [])
        self.assertEqual(dummyPlayer.id, 1)

    def test_earnMoney(self):
        dummyPlayer = Player('dummy')
        initMoney = dummyPlayer.money
        testProduct = Product()
        testProduct.setAttributes(1,1,1,1)
        dummyPlayer.earnMoney(testProduct)
        self.assertEqual(dummyPlayer.money, initMoney+testProduct.revenue)

if __name__ == '__main__':
    unittest.main()
