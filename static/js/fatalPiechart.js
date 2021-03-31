		var config = {
			type: 'pie',
			data: {
				datasets: [{
					data: [
                        3,
                        41,
                        56
					],
					backgroundColor: [
						'red',
						'lightblue',
						'lightgreen',
						
					],
					label: 'Dataset 1'
				}],
				labels: [
					'Fatal',
					'Injury',
					'No Injury',
				]
			},
			options: {
				responsive: true
			}
		};

		window.onload = function() {
			var ctx = document.getElementById('chart-area').getContext('2d');
			window.myPie = new Chart(ctx, config);
		};


			window.myPie.update();

		var colorNames = Object.keys(window.chartColors);