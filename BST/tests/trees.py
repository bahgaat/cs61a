test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2)) # Enter Function if you believe the answer is <function ...>, Error if it errors, and Nothing if nothing is displayed.
          45fc73aa4635e3dec06acb9e15eb8deb
          # locked
          >>> t = Tree(1, [Tree(2)])
          >>> t.label
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          >>> t.branches[0]
          e7fa43b940b66ae602da8c6ce35ed80a
          # locked
          >>> t.branches[0].label
          242a6d3d4ed1b1d1292acd307083f4e0
          # locked
          >>> t.label = t.branches[0].label
          >>> t
          80bb795daf217bd9f9ef793a22c7177c
          # locked
          >>> t.branches.append(Tree(4, [Tree(8)]))
          >>> len(t.branches)
          242a6d3d4ed1b1d1292acd307083f4e0
          # locked
          >>> t.branches[0]
          e7fa43b940b66ae602da8c6ce35ed80a
          # locked
          >>> t.branches[1]
          1e6483162bda2c0066793202a6207170
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
