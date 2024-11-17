const socket = new WebSocket('ws://localhost:8080');

socket.onmessage = function(event) {
  const trafficData = JSON.parse(event.data);
  updateTrafficMap(trafficData);
};

function updateTrafficMap(data) {
  d3.select('#traffic-map')
    .selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .attr('cx', d => d.longitude)
    .attr('cy', d => d.latitude)
    .attr('r', 5)
    .style('fill', d => (d.congestionLevel > 5 ? 'red' : 'green'));
}