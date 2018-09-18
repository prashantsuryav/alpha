##Examples of alpha expression

1. rank(delay(close,2)-ts_regression(close,vwap,60,0,3))

2. a=sum(open>close,20)/sum(open<close,20);
b=sum(open>close,252)/sum(open<close,252);
rank(a/b)

3. rank(tradewhen(volume>adv20,-returns,-1))

4. rank(sales/assets)

5. bar=(open-close)/(high-low);
a=sum((open>close)*bar,20)/sum((open<close)*(-bar),20);
b=sum((open>close)*bar,252)/sum((open<close)*(-bar),252);
rank(a/b)

6. sum(sign(delta(close,1)),4)==-4?0:rank(-delta(close,2))



