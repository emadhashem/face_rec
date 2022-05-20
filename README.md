# face_recog_in_py
## how to run the code
make sure u r installed c++, cmake

### Run
pip or pip3 install -r requirements.txt

then run python3 index.py

open postman and send post requst to =>
http://localhost:5000/addimg with body like this ===|>  



{
 
	"imgs" : [
		"https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/newscms/2017_05/1832761/161214-trump_techexecutives-1558.jpg",
		
		"https://image.cnbcfm.com/api/v1/image/104236918-GettyImages-632550332.jpg?v=1529473983",
		"https://media.gettyimages.com/photos/trump-advisor-steve-bannon-watches-as-us-president-donald-trump-elon-picture-id633679096?s=612x612"
		]
	,
	"faces" : {
		"1-elon muskss" : "https://upload.wikimedia.org/wikipedia/commons/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg",
		"1-jeff bezos" : "https://cdn.britannica.com/56/199056-050-CCC44482/Jeff-Bezos-2017.jpg",
		"1-donald trumpo" : "https://static.dw.com/image/55598269_303.jpg",
		"2-donald trumpo" : "https://media.npr.org/assets/img/2020/02/10/gettyimages-1197130872_custom-e185dd1d87ce7f21b7bf960a57692f34be2af356.jpg",
		"1-bale" : "https://imageio.forbes.com/specials-images/imageserve/5f4ebe0c87612dab4f12a597/0x0.jpg?format=jpg&crop=3392,3395,x292,y592,safe&fit=crop",
		"2-elon muskss" : "https://cdn.cnn.com/cnnnext/dam/assets/150610124003-01-elon-musk-file-0610-super-169.jpg"
		
	}
}

