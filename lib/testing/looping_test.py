# tests/test_looping.py

from looping.looping import happy_new_year, square_integers, fizzbuzz

def test_happy_new_year(capsys):
    happy_new_year()
    captured = capsys.readouterr()
    assert captured.out.strip() == "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nHappy New Year!"

def test_square_integers():
    assert square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_fizzbuzz(capsys):
    fizzbuzz()
    captured = capsys.readouterr()
    expected_output = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz"
    assert captured.out.strip() == expected_output.strip()
