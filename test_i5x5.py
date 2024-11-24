from i5x5 import *

def test_normal():
    assert normal([]) == True
    assert normal([[],[]]) == True
    assert normal([[1]]) == True
    assert normal([[1,2],[3,4]]) == True
    assert normal([[1,2,3],[4,5,6],[7,8,9]]) == True

    assert normal([[1],[]]) == False
    assert normal([[],[1]]) == False
    assert normal([[1],[3,4]]) == False
    assert normal([[1,2,3],[4,6],[7,8,9]]) == False


def test_trans_mpp2():
    assert trans_mpp2([]) == [[]]
    assert trans_mpp2([[]]) == [[]]

    assert trans_mpp2([[1]]) == [[1]]
    assert trans_mpp2([
        [1],
        [2]]) == [[2,1]]
    assert trans_mpp2([
        [1,2],
        [3,4]]) == [
            [3,1],
            [4,2]]
    assert trans_mpp2([
        [1,2],
        [3,4],
        [5,6],
        [7,8]]) == [
            [7,5,3,1],
            [8,6,4,2]]

def test_mirror():
    assert mirror([]) == [[]]
    assert mirror([[]]) == [[]]

    assert mirror([[1]]) == [[1]]
    assert mirror([
        [1],
        [2]]) == [
            [1],
            [2]]
    assert mirror([
        [1,2],
        [3,4]]) == [
            [2,1],
            [4,3]]
    assert mirror([
        [1,2,3],
        [4,5,6],
        [7,8,9]])==[
            [3,2,1],
            [6,5,4],
            [9,8,7]]
