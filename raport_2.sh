echo 'ORIGINAL - LENA'

python3 ./main.py --cmean -i ./imgs/lenac.bmp
python3 ./main.py --cvariance -i ./imgs/lenac.bmp
python3 ./main.py --cstdev -i ./imgs/lenac.bmp
python3 ./main.py --cvarcoi -i ./imgs/lenac.bmp
python3 ./main.py --casyco -i ./imgs/lenac.bmp
python3 ./main.py --cflatco -i ./imgs/lenac.bmp
python3 ./main.py --cvarcoii -i ./imgs/lenac.bmp
python3 ./main.py --centropy -i ./imgs/lenac.bmp

echo 'ORIGINAL - MANDRIL'

python3 ./main.py --cmean -i ./imgs/mandrilc.bmp
python3 ./main.py --cvariance -i ./imgs/mandrilc.bmp
python3 ./main.py --cstdev -i ./imgs/mandrilc.bmp
python3 ./main.py --cvarcoi -i ./imgs/mandrilc.bmp
python3 ./main.py --casyco -i ./imgs/mandrilc.bmp
python3 ./main.py --cflatco -i ./imgs/mandrilc.bmp
python3 ./main.py --cvarcoii -i ./imgs/mandrilc.bmp
python3 ./main.py --centropy -i ./imgs/mandrilc.bmp

python3 ./main.py --hraleigh -i ./imgs/lenac.bmp  

echo 'IMPROVED - LENA'

python3 ./main.py --cmean -i ./imgs/output.bmp
python3 ./main.py --cvariance -i ./imgs/output.bmp
python3 ./main.py --cstdev -i ./imgs/output.bmp
python3 ./main.py --cvarcoi -i ./imgs/output.bmp
python3 ./main.py --casyco -i ./imgs/output.bmp
python3 ./main.py --cflatco -i ./imgs/output.bmp
python3 ./main.py --cvarcoii -i ./imgs/output.bmp
python3 ./main.py --centropy -i ./imgs/output.bmp
  
python3 ./main.py --hraleigh -i ./imgs/mandrilc.bmp    

echo 'IMPROVED - MANDRIL'

python3 ./main.py --cmean -i ./imgs/output.bmp
python3 ./main.py --cvariance -i ./imgs/output.bmp
python3 ./main.py --cstdev -i ./imgs/output.bmp
python3 ./main.py --cvarcoi -i ./imgs/output.bmp
python3 ./main.py --casyco -i ./imgs/output.bmp
python3 ./main.py --cflatco -i ./imgs/output.bmp
python3 ./main.py --cvarcoii -i ./imgs/output.bmp
python3 ./main.py --centropy -i ./imgs/output.bmp