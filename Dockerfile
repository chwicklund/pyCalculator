FROM python:3

ADD src /src

CMD [ "python", ".tests/test_Calculator.py" ]

CMD [ "python", "-m", "unittest", "discover", "-s", "Tests" ]