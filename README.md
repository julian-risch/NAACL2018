# Popularity Prediction Framework

### Citation

If you use our work, please cite our paper [**Prediction for the Newsroom: Which Articles Will Get the Most Comments?**](https://github.com/julian-risch/NAACL2018/raw/master/ambroselli2018prediction.pdf) as follows:

    @inproceedings{ambroselli2018prediction,
    author = {Ambroselli, Carl and Risch, Julian and Krestel, Ralf and Loos, Andreas},
    booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
    pages = {193-199},
    title = {Prediction for the Newsroom: Which Articles Will Get the Most Comments?},
    year = {2018}
    }

### Start the framework
1. Clone the repository: `git clone https://github.com/CarlAmbroselli/Popularity_Predictor`
2. Open repository: `cd Popularity_Predictor`
3. (optional) Checkout paper/napoles branch: `git checkout paper/napoles`
4. Install requirements: `pip install -r requirements.txt #might be done in a virtualenv`
5. Add `comments.csv` to the `data/datasets/YNACC-Evaluation/train/` and `data/datasets/YNACC-Evaluation/test` folder with the following format: 
```
sdid,commentindex,headline,url,guid,commentid,timestamp,thumbs-up,thumbs-down,text,parentid,constructiveclass,sd_agreement,sd_type,sentiment,tone,commentagreement,topic,intendedaudience,persuasiveness,y_persuasive,y_audience,y_agreement_with_commenter,y_informative,y_mean,y_controversial,y_disagreement_with_commenter,y_off_topic_with_article,y_sentiment,y_sentiment_neutral,y_sentiment_positive,y_sentiment_negative,y_sentiment_mixed
```
6. Add `data/datasets/YNACC/users.csv` file with the following format:
```
index,comment_count,threads_participated_in,threads_initiated,tu_received,td_received,commenting_rate
```
7. Save [word2vec model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) to `model/word2vec/GoogleNews-vectors-negative300.bin`
8. Download en spacy model: `python -m spacy download en`
9. Run using `python .`
