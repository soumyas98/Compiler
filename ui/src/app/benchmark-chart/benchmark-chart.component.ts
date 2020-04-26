import { Component, OnInit, Input } from '@angular/core';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';
import { BenchMark } from '../model/BenchMark';

@Component({
  selector: 'app-benchmark-chart',
  templateUrl: './benchmark-chart.component.html',
  styleUrls: ['./benchmark-chart.component.css']
})
export class BenchmarkChartComponent implements OnInit {
  @Input() benchMark: BenchMark;
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
          { y: this.benchMark.O0.exec_time * 1000, label: 'O0' },
          { y: this.benchMark.O1.exec_time * 1000, label: 'O1' },
          { y: this.benchMark.O2.exec_time * 1000, label: 'O2' },
          { y: this.benchMark.O3.exec_time * 1000, label: 'O3' },
          { y: this.benchMark.GAOpt.exec_time * 1000, label: 'GA found flags' }
        ]
      }]
    });
    this.chart.render();
  }

}
