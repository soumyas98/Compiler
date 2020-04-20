import { Component, OnInit, Input } from '@angular/core';
import { GA } from '../model/GA';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';

@Component({
  selector: 'app-benchmark-chart',
  templateUrl: './benchmark-chart.component.html',
  styleUrls: ['./benchmark-chart.component.css']
})
export class BenchmarkChartComponent implements OnInit {
  @Input() data: GA;
  chart: any;

  constructor() { }

  ngOnInit() {
    this.initChart();
  }

  initChart(): void {
    this.chart = new CanvasJS.Chart("benchmarkChartContainer", {
      animationEnabled: true,
      axisX: {
        title: 'Optimization',
      },
      axisY: {
        title: 'Execution time',
        suffix: 'ms'
      },
      toolTip: {
        shared: true
      },
      data: [{
        type: "column",
        name: "Execution Time",
        dataPoints: [
          { y: this.data.benchmark.O0.exec_time * 1000, label: 'O0' },
          { y: this.data.benchmark.O1.exec_time * 1000, label: 'O1' },
          { y: this.data.benchmark.O2.exec_time * 1000, label: 'O2' },
          { y: this.data.benchmark.O3.exec_time * 1000, label: 'O3' },
          { y: this.data.generations[this.data.generation_count - 1].fittest.exec_time * 1000, label: 'GA Flags' }
        ]
      }]
    });
    console.log(this.data);
    this.chart.render();
  }

}
