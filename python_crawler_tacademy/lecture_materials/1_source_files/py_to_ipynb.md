##### .py to .ipynb

1. 파이썬파일 --> 주피터노트북파일

   - 패키지 다운로드

     ```
     mspark@j:~$ pip install ipynb-py-convert
     ```

   - 사용법

     ```
     mspark@j:~$ ipynb-py-convert
     Usage: ipynb-py-convert in.ipynb out.py
     or:    ipynb-py-convert in.py out.ipynb
     ```

   - 변환 (example)

     ```
     mspark@j:~$ ipynb-py-convert run.py run.ipynb
     ```

2. .ipynb 파일을 다른 형식으로 변환

   - .py

     ```
     $ jupyter nbconvert --to script abc.ipynb
     abc.py
     ```

   - .html

     ```
     $ jupyter nbconvert --to html abc.ipynb
     abc.html
     ```

     