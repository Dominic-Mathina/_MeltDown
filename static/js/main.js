var url = 'http://localhost:8000/api/plist/'
//var url =  'http://transportapi.com/v3/uk/places.json?query=euston&type=train_station&app_id=8b9cd4d9&app_key=69eaf54e2f7d2f279a03077acab2721b'

$.ajax({
	method: "GET",
	url: url,
	success: function(data){
		console.log(data)
	},
	error: function(error_data){
		console.log('error')
	}

})
