document.addEventListener('DOMContentLoaded', function() {
    const divsMetrics = document.querySelectorAll(".metrics-section");
	const divsMetric = divsMetrics[1];
	const divs = divsMetric.querySelectorAll(".metrics-block");

	divs.forEach(div => {
		const span = div.querySelector(".arrow");
		const divZD = div.querySelector(".zd-metric");
		const spanUnit = div.querySelector("span");

			/*Cas des métriques de durée */
			const arrow = div.querySelector(".arrow");
			const zdDiv = div.querySelector(".zd-metric-section");

			if (spanUnit.textContent == "m") {

				const h2s = div.querySelectorAll("h2");
				const h4s = zdDiv.querySelectorAll("h4");

				timeEnq = 60*parseFloat(h2s[0].textContent) + parseFloat(h2s[1].textContent); /* Temps enquêteur*/
				timeZD = 60*parseFloat(h4s[0].textContent) + parseFloat(h4s[1].textContent); /* Temps ZD*/


				if (timeEnq >= timeZD) {
					zdDiv.style.color = "blue";
					arrow.innerHTML = "&#8593;";
				}
				else {
					zdDiv.style.color = "red";
					arrow.innerHTML = "&#8595;";
				}

			}
			else {
				const zdDiv = div.querySelector(".zd-metric-section");
				const h2 = div.querySelector("h2");
				const h4 = zdDiv.querySelector("h4");
				h2Value = parseFloat(h2.textContent);
				h4Value = parseFloat(h4.textContent);

				if (h2Value <= h4Value) {
					zdDiv.style.color = "red";
					arrow.innerHTML = "&#8595;";
				}
				else {
					zdDiv.style.color = "blue";
					arrow.innerHTML = "&#8593;";
				}
			}
	});
});
