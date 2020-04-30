import { Component, OnInit, Input } from '@angular/core';
import { GA } from '../model/GA';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';

@Component({
  selector: 'app-fitness-chart',
  templateUrl: './fitness-chart.component.html',
  styleUrls: ['./fitness-chart.component.css']
})
export class FitnessChartComponent implements OnInit {
  chart: any;
  averageFitnessDataPoints: any[] = [];

  constructor() { }

  ngOnInit() {
    this.initChart();
  }

  initChart(): void {
    this.chart = new CanvasJS.Chart("fitnessChartContainer", {
      animationEnabled: true,
      axisX: {
        title: 'Generation',
        minimum: 0
      },
      axisY: {
        title: 'Fitness',
        minimum: 0
      },
      data: [{
        type: "line",
        color: "teal",
        name: "Average fitness",
        dataPoints: this.averageFitnessDataPoints
      }]
    });
    this.chart.render();
  }

  updateChart(currGenIdx: number, prevAvgFit: number): void {
    if (currGenIdx > this.averageFitnessDataPoints.length) {
      this.averageFitnessDataPoints.push({
        x: this.averageFitnessDataPoints.length,
        y: prevAvgFit
      });
    }
    this.chart.render();
  }

  reset(): void {
    this.averageFitnessDataPoints.length = 0;
    this.chart.render();
  }

}
