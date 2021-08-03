# Flask 웹 서버 구축에 필요한 라이브러리를 불러옵니다.
from os import terminal_size
from flask import Flask, render_template, redirect, request, url_for,jsonify
# 네이버 영화 리뷰 크롤링에 필요한 함수를 가져옵니다. 
from app1.Part_1 import *
# 단어구름에 필요한 라이브러리를 불러옵니다.
from wordcloud import WordCloud
# 한국어 자연어 처리 라이브러리를 불러옵니다.
from konlpy.tag import Twitter
# 명사의 출현 빈도를 세는 라이브러리를 불러옵니다.
from collections import Counter
# 그래프 생성에 필요한 라이브러리를 불러옵니다.
import matplotlib.pyplot as plt
import time

# 폰트 경로 설정
font_path = 'NanumGothic.ttf'

# 플라스크 웹 서버 객체를 생성합니다.
app = Flask(__name__)

    # process_from_text(content['text'], 15, 2, words)
    # result = {'result': True}
    # return jsonify(result)






@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wordcloud', methods=['POST','GET'])
def wordcloud(movie=None):
    if request.method == 'POST':
        # movie_title = request.form['movie']
        pass
    elif request.method == 'GET':
        # 넘겨받은 영화 제목
        movie_title = request.args.get('movie')
        
        # 네이버 영화 리뷰 크롤링으로 별점과 리뷰 가져오기 
        avg_stars = get_avg_stars(get_reviews(get_movie_code(movie_title),1))
        review = scrape_by_review_num(movie_title, 500)

        for i in range(len(review)):
            review_text = review[i]['review_text']
            review_star = review[i]['review_star']

        # 영화 리뷰 워드클라우드 
        font_path = 'app1/NanumGothic.ttf'
        wordcloud = WordCloud(font_path=font_path,width=2400, height=1800, ranks_only=None, relative_scaling = 0.8)
        wordcloud2 = wordcloud.generate(review_text)
        fig = plt.figure(figsize=(6,6))
        plt.imshow(wordcloud2)
        plt.axis('off')
        plt.show()
        fig.savefig('static/images/wordcloud.png')
        
        return render_template('wordcloud.html', time=time.time())

    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함
 


if __name__ == '__main__':
    app.run(debug=True)

    