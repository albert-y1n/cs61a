test = {
  'name': 'Question 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pigs_on_prime_strategy(15, 34, threshold=3, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(30, 54, threshold=10, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(19, 32, threshold=7, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(24, 5, threshold=8, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(pigs_on_prime_strategy)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> pigs_on_prime_strategy(97, 22, 15, 7)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(36, 3, 3, 2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(78, 14, 13, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(46, 87, 5, 1)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(78, 64, 7, 10)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(0, 19, 14, 10)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(39, 10, 13, 10)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(34, 8, 11, 10)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(0, 23, 9, 9)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(56, 0, 9, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(26, 62, 13, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(1, 69, 11, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(25, 72, 11, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(43, 15, 0, 5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(13, 15, 18, 7)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(61, 47, 1, 1)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(75, 51, 11, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(41, 94, 3, 2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(28, 50, 11, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(46, 21, 18, 1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(40, 29, 9, 8)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(57, 21, 1, 3)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(29, 50, 16, 2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(40, 74, 5, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(51, 0, 10, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(70, 7, 12, 2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(50, 94, 1, 10)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(13, 79, 18, 1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(40, 8, 19, 8)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(89, 32, 19, 8)
          8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(21, 20, 7, 8)
          8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(92, 71, 16, 2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(1, 5, 15, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(71, 39, 2, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(59, 56, 14, 2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(59, 61, 15, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(5, 94, 16, 10)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(62, 70, 16, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(83, 9, 5, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(96, 54, 5, 3)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(54, 8, 15, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(13, 4, 3, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(66, 25, 2, 8)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(56, 55, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(64, 21, 0, 5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(71, 37, 12, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(32, 20, 6, 7)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(36, 45, 8, 10)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(65, 72, 18, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(82, 23, 2, 7)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(79, 12, 15, 9)
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(2, 66, 16, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(87, 71, 8, 7)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(92, 7, 13, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(87, 38, 12, 4)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(1, 2, 5, 9)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(37, 49, 17, 10)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(41, 55, 3, 7)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(57, 8, 13, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(85, 75, 16, 8)
          8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(73, 89, 5, 5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(48, 54, 18, 4)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(96, 45, 1, 2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(95, 63, 1, 9)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(59, 33, 15, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(46, 50, 2, 4)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(96, 23, 11, 9)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(80, 63, 11, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(3, 9, 15, 4)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(73, 2, 7, 2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(5, 81, 1, 1)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(81, 73, 10, 6)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(79, 69, 12, 10)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(4, 67, 16, 10)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(80, 27, 2, 4)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(46, 18, 3, 7)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(25, 45, 9, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(12, 35, 10, 8)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(36, 14, 12, 4)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(24, 30, 8, 8)
          8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(82, 84, 18, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(81, 76, 10, 7)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(75, 44, 6, 4)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(90, 31, 17, 4)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(27, 4, 10, 6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(86, 7, 3, 9)
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(91, 55, 7, 7)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(45, 14, 16, 2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(78, 31, 10, 10)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(8, 92, 7, 2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(7, 55, 8, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(69, 93, 19, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(40, 60, 5, 1)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(97, 51, 10, 10)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(9, 40, 17, 2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(13, 79, 17, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(57, 5, 2, 2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(7, 32, 5, 7)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(96, 40, 15, 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> pigs_on_prime_strategy(50, 59, 4, 1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
