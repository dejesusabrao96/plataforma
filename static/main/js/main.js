window.onload = init;

function init(){
	const mymap = L.map('mapid', {
		center: [-8.56371035, 125.56037373],
		zoom: 4,
		layer:[
			L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
				attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
			})
		]
	})
}